from src.max import myFunction


def test_myFunction():
    assert myFunction(2, 3, 6) == "groß"
    assert myFunction(-1, 5, 0) == "klein"
    assert myFunction(0, 0, 0) == "klein"