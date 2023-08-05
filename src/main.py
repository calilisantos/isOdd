from src.odd_analysis import OddAnalysys
from src.random_generator import RandomGenerator

class Main:
  def __init__(self):
    self.odd_analysis = OddAnalysys()
    self.random_generator = RandomGenerator()

  def main(self, integer_odd_value):
    random_number = self.random_generator.generate_random_number(integer_odd_value)
    odd_analysis = self.odd_analysis.is_odd(random_number)
    return odd_analysis
