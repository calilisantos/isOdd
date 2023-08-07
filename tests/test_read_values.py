from pytest import raises
from src.read_values import ReadValues

class TestReadValues:
    def test_check_entry_value__with_valid_value(self, odd_int_in_string, odd_int):
        assert ReadValues.check_entry_value(odd_int_in_string) == odd_int

    def test_check_entry_value__with_a_double(self, double_in_string):
        with raises(ValueError):
            ReadValues.check_entry_value(double_in_string)

    def test_check_entry_value__with_a_string(self, number_name):
        with raises(ValueError):
            ReadValues.check_entry_value(number_name)

    def test_check_entry_value__with_a_negative_int(self, negative_int_in_string):
        with raises(ValueError):
            ReadValues.check_entry_value(negative_int_in_string)
