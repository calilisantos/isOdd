class OddAnalysys:
  def is_integer(value):
    check_value = isinstance(value, int)

    if check_value is False:
      raise ValueError('The value must be an integer')
    return check_value

  def is_odd(integer_value):
    return f"{integer_value} is even" if integer_value % 2 == 0 else f"{integer_value} is odd"
