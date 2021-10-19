class InvalidRangeError(ValueError):
    ...


def range_validator(min_value: int, max_value: int):
    def range_validator(instace, attribute, value):
        real_length = value
        if not min_value <= real_length <= max_value:
            raise InvalidRangeError(f"Value {value} must be between {min_value} and {max_value}")

    return range_validator


color_validator = range_validator(0, 0xFF)


class InvalidModeError(ValueError):
    ...


def rgb_validator(instance, attribute, value):
    if value.mode != "RGB" and value.mode != "RGBA":
        raise InvalidModeError(f"{value.mode} must be either RGB or RGBA")
