from .odd_analyses import OddAnalyses
from .random_generator import RandomGenerator
from .read_values import ReadValues

class Orchestrator:
  def __init__(self, entry_value, limit_value):
    self.integer_odd_value = ReadValues.check_entry_value(entry_value)
    self.max_random_limit = ReadValues.check_entry_value(limit_value)

  def show_result(self):
    random_number = RandomGenerator.generate_random_number(self.integer_odd_value, self.max_random_limit)
    odd_analyses = OddAnalyses.is_odd(random_number)
    return odd_analyses
