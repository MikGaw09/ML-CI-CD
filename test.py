import numpy as np
from model import train_and_predict, get_accuracy

def test_predictions_not_none():
    """
    Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    """
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."

def test_predictions_length():
    """
    Test 2 (na maksymalną ocenę 5): Sprawdza, czy długość listy predykcji jest większa od 0 
    i czy odpowiada przewidywanej liczbie próbek testowych.
    """
    preds, y_test = train_and_predict()
    
    assert len(preds) > 0, "Lista predykcji jest pusta (długość wynosi 0)."
    # Sprawdzenie, czy dla każdej próbki testowej mamy predykcję
    assert len(preds) == len(y_test), f"Oczekiwano {len(y_test)} predykcji, ale otrzymano {len(preds)}."

def test_predictions_value_range():
    """
    Test 3 (na maksymalną ocenę 5): Sprawdza, czy wartości w predykcjach mieszczą się 
    w spodziewanym zakresie: Dla zbioru Iris mamy 3 klasy (0, 1, 2).
    """
    preds, _ = train_and_predict()
    dozwolone_klasy = {0, 1, 2}
    
    # Przekształcamy predykcje na zbiór (set), aby łatwo sprawdzić, czy wszystkie 
    # wygenerowane wartości zawierają się w zbiorze dozwolonych klas.
    unikalne_predykcje = set(preds)
    
    assert unikalne_predykcje.issubset(dozwolone_klasy), \
        f"Znaleziono niedozwolone wartości klas w predykcjach: {unikalne_predykcje - dozwolone_klasy}"

def test_model_accuracy():
    """
    Test 4 (na maksymalną ocenę 5): Sprawdza, czy model osiąga co najmniej 70% dokładności 
    (przykładowy warunek, można dostosować do potrzeb).
    """
    accuracy = get_accuracy()
    
    assert accuracy >= 0.70, f"Dokładność modelu ({accuracy:.2f}) jest niższa niż wymagane minimum 0.70."
