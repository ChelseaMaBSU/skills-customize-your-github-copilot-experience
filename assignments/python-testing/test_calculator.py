import pytest

from calculator import add, apply_discount, calculate_average, split_bill


def test_adds_two_numbers():
    assert add(2, 3) == 5


def test_adds_negative_numbers():
    # TODO: Add an assertion for adding two negative numbers.
    pass


def test_calculates_average():
    # TODO: Test the average of a list with at least three numbers.
    pass


def test_applies_discount():
    # TODO: Test a 15 percent discount on a price of 100.
    pass


def test_splits_bill_evenly():
    # TODO: Test splitting a 30 dollar bill between 3 people.
    pass


def test_splits_bill_and_rounds_result():
    # TODO: Test that a result with more than two decimal places is rounded.
    pass


def test_average_of_empty_list_raises_value_error():
    # TODO: Use pytest.raises to describe the expected behavior.
    pass


def test_invalid_number_of_people_raises_value_error():
    # TODO: Check both zero and negative people counts.
    pass