import numpy as np

class RandomGenerator:
  @staticmethod
  def generate_random_number(integer_odd_value, max_random_limit):
    random_generator = np.random.randint(1, max_random_limit)
    return integer_odd_value + random_generator
