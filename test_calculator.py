import pytest
from calculator import add , subtract , multiply , divide

def test_add() :
  assert add(5,4) == 9

def test_subtract() :
  assert subtract(10,4) == 6

def test_multiply():
  assert multiply(3,7) == 21

def test_divide() :
  assert divide(10,2) == 5

def test_zero_divide() :
  with pytest.raises(ValueError):
    divide(9,0)
