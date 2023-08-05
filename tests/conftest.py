from pytest import fixture

@fixture
def integer_odd_value():
  return 1

@fixture
def integer_even_value():
  return 2

@fixture
def double_value():
  return 1.1

@fixture
def string_value():
  return '1'
