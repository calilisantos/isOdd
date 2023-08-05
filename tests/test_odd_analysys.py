from pytest import raises
from src.odd_analysis import OddAnalysys

class TestOddAnalysys:
  def test_is_integer_with_valid_value(self, integer_odd_value):
    assert OddAnalysys.is_integer(integer_odd_value) == True

  def test_is_integer_with_a_double(self, double_value):
    with raises(ValueError):
      OddAnalysys.is_integer(double_value)

  def test_is_integer_with_a_string(self, string_value):
    with raises(ValueError):
      OddAnalysys.is_integer(string_value)

  def test_is_odd_with_an_odd_integer(self, integer_odd_value):
    assert OddAnalysys.is_odd(integer_odd_value) == f'{integer_odd_value} is odd'
  
  def test_is_odd_with_an_even_integer(self, integer_even_value):
    assert OddAnalysys.is_odd(integer_even_value) == f'{integer_even_value} is even'
