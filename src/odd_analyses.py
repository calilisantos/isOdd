class OddAnalyses:
  @staticmethod
  def is_odd(integer_value):
    return f"{integer_value} is even" if integer_value % 2 == 0 else f"{integer_value} is odd"
