import numpy as np

class RandomGenerator:
  def generate_random_number(integer_odd_value):
    random_generator = np.random.randint(1, 1000)
    return integer_odd_value + random_generator
