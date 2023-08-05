from src.random_generator import RandomGenerator

class TestRandomGenerator:
  def test_generate_random_number_sum(self, integer_odd_value):
    random_result = RandomGenerator.generate_random_number(integer_odd_value)
    assert random_result > integer_odd_value

  def test_generate_random_number_type(self, integer_odd_value):
    random_result = RandomGenerator.generate_random_number(integer_odd_value)
    assert isinstance(random_result, int) == True
