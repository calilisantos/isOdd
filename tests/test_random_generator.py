from src.random_generator import RandomGenerator

class TestRandomGenerator:
  def test_generate_random_number__less_or_equal__entries_sum(self, odd_int, max_random_limit):
    entries_sum = odd_int + max_random_limit
    
    random_result = RandomGenerator.generate_random_number(odd_int, max_random_limit)

    assert random_result <= entries_sum

  def test_generate_random_number__type(self, odd_int, max_random_limit):
    random_result = RandomGenerator.generate_random_number(odd_int, max_random_limit)
    assert isinstance(random_result, int) == True
