import pytest
from src.main import add


def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_sign_numbers():
    assert add(-2, 3) == 1

def test_add_zeros():
    assert add(0, 0) == 0
