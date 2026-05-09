
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field
import pickle
import numpy as np

iris_names = {0: "setosa", 1: "versicolor", 2: "virginica"}
app = FastAPI()

import pickle
import numpy as np
import sklearn

with open('model_iris_v1.pkl', 'rb') as f:
        model = pickle.load(f)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    error_list = []
    for error in errors:
        field = error.get("loc")[-1]
        msg = "Brak wymaganej wartości" if error.get("type") == "value_error.missing" else error.get("msg")
        error_list.append({"cecha": field, "blad": msg})

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"status": "error", "message": "Nieprawidłowe dane wejściowe", "szczegoly": error_list},
    )
class Item(BaseModel):
    sl: float = Field(..., description="Sepal Length")
    sw: float = Field(..., description="Sepal Width")
    pl: float = Field(..., description="Petal Length")
    pw: float = Field(..., description="Petal Width")
@app.post("/predict")
async def predict(item : Item):
    try:
        predict=model.predict([[item.sl,item.sw,item.pl,item.pw]])
        prediction = int(predict[0])
        return {"predict": prediction,
            "name": iris_names[prediction]}
    except Exception as e:
        return JSONResponse(
        status_code=500,
        content={"status": "error", "message": f"Błąd modelu: {str(e)}"}
        )
@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/info")
async def model_info():
    return {
        "model_type": str(type(model).__name__),
        "n_features": getattr(model, "n_features_in_", 4),
        "classes": iris_names
    }