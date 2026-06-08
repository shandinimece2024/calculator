import pytest
from calculator import add, sub, mul, div

def test_add():
  assert add(2,3)==5
def test_sub():
  assert sub(10,4)==6
def test_mul():
  assert mul(3,5)==15
def test_div():
  assert div(10,2)==5
def test_errorcase():
  with pytest.raises(ValueError):
    div(10,0)
