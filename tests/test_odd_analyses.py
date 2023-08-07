from src.odd_analyses import OddAnalyses

class TestOddAnalysys:
  def test_is_odd_with_an_odd_integer(self, odd_int):
    assert OddAnalyses.is_odd(odd_int) == f'{odd_int} is odd'
  
  def test_is_odd_with_an_even_integer(self, even_int):
    assert OddAnalyses.is_odd(even_int) == f'{even_int} is even'
