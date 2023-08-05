class OddAnalysys:
  def is_integer(value):
    check_value = isinstance(value, int)

    if check_value is False:
      raise ValueError('The value must be an integer')
    return check_value

  def is_odd(integer_value):
    if integer_value % 2 == 0:
      return f"{integer_value} is even"
    return f"{integer_value} is odd"
