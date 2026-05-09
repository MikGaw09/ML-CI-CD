import pytest
import pickle
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# pytest.fixture spowoduje utworzenie zależności z modelu, która zostanie wstrzyknieta w kazdy z testów zamiast 
#ładować model od nowa
@pytest.fixture(scope="module")
def setup_model_and_data():
    #wczytywanie pliku pickle
    with open('model_iris_v1.pkl', 'rb') as f:
        model = pickle.load(f)

    # zbior do testowania
    iris = load_iris()
    # dzielenie danych na podzbiory
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # predykcja modelu
    preds = model.predict(X_test)

    return model, preds, y_test


def test_predictions_not_none(setup_model_and_data):
    """Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję."""
    model, preds, y_test = setup_model_and_data

    assert preds is not None, "Predictions should not be None."


def test_predictions_length(setup_model_and_data):
    """Test 2: Sprawdza, czy długość listy predykcji jest większa od 0
    i czy odpowiada przewidywanej liczbie próbek testowych."""
    model, preds, y_test = setup_model_and_data

    assert len(preds) > 0, "Lista predykcji jest pusta (długość wynosi 0)."
    assert len(preds) == len(y_test), f"Oczekiwano {len(y_test)} predykcji, ale otrzymano {len(preds)}."


def test_predictions_value_range(setup_model_and_data):
    """Test 3: Sprawdza, czy wartości w predykcjach mieszczą się w spodziewanym zakresie (0, 1, 2)."""
    model, preds, y_test = setup_model_and_data

    dozwolone_klasy = {0, 1, 2}
    unikalne_predykcje = set(preds)

    assert unikalne_predykcje.issubset(dozwolone_klasy), \
        f"Znaleziono niedozwolone wartości klas: {unikalne_predykcje - dozwolone_klasy}"


def test_model_accuracy(setup_model_and_data):
    """Test 4: Sprawdza, czy model osiąga co najmniej 70% dokładności."""
    model, preds, y_test = setup_model_and_data

    # Obliczenie dokładności porównując predykcje z prawdziwymi etykietami
    accuracy = accuracy_score(y_test, preds)

    assert accuracy >= 0.70, f"Dokładność modelu wynosi {accuracy:.2f}, co jest poniżej wymaganego 0.70."
