from typing import Optional

from pytest import raises
from hypothesis import given
from hypothesis.strategies import integers, composite

from nametable_pil.validators import range_validator, InvalidRangeError, rgb_validator


@composite
def range_validator_data(draw, min_value: Optional[int] = 0, max_value: Optional[int] = 50):
    min_range = draw(integers(min_value=min_value, max_value=max_value))
    max_range = draw(integers(min_value=min_range, max_value=max_value))
    return min_range, max_range


@given(range_validator_data())
def test_initialization(validator_data: tuple[int, int]):
    range_validator(*validator_data)


@given(range_validator_data())
def test_valid_replies(validator_data: tuple[int, int]):
    validator = range_validator(*validator_data)
    for i in range(validator_data[0], validator_data[1]):
        validator(None, None, i)


@given(range_validator_data())
def test_invalid_replies(validator_data: tuple[int, int]):
    validator = range_validator(*validator_data)
    with raises(InvalidRangeError):
        validator(None, None, validator_data[0] - 1)
    with raises(InvalidRangeError):
        validator(None, None, validator_data[1] + 1)


def test_rgb_mode():
    class A:
        mode = "RGB"

    rgb_validator(None, None, A())


def test_rgba_mode():
    class A:
        mode = "RGBA"

    rgb_validator(None, None, A())
