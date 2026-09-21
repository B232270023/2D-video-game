import pytest
from sum import sum

def test_sum():
    assert sum(1, 2) == 3

def test_sum_invalid_input():
    with pytest.raises(TypeError, match="Тоо оруулах шаардлагатай!"):
        sum(1, "2")