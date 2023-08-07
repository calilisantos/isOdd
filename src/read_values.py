class ReadValues:
  @staticmethod
  def _entry_to_integer(value):
    if isinstance(int(value), int) is False:
      raise ValueError('The entry value must be an integer')
    return int(value)

  @staticmethod
  def check_entry_value(entry_value):
    int_value = ReadValues._entry_to_integer(entry_value)
    if int_value <= 0:
      raise ValueError('The entry value must be greater than zero')
    return int_value
