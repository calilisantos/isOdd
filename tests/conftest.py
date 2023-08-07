from .constants import valid_values, wrong_values
from pytest import fixture

@fixture
def odd_int_in_string():
  return valid_values.ODD_INT_IN_STRING

@fixture
def even_int_in_string():
  return valid_values.EVEN_INT_IN_STRING

@fixture
def max_limit_in_string():
  return valid_values.MAX_LIMIT_IN_STRING

@fixture
def odd_int():
  return valid_values.ODD_INT

@fixture
def even_int():
  return valid_values.EVEN_INT

@fixture
def max_random_limit():
  return valid_values.MAX_RANDOM_LIMIT

@fixture
def double_in_string():
  return wrong_values.DOUBLE_IN_STRING

@fixture
def number_name():
  return wrong_values.NUMBER_NAME

@fixture
def negative_int_in_string():
  return wrong_values.NEGATIVE_INT_IN_STRING
