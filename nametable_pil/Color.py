from typing import Protocol
from collections.abc import Iterable

from attr import attrs, attrib

from nametable_pil.validators import color_validator


class ColorProtocol(Protocol):
    """
    A representation of a RGBA or RGB color.
    """

    red: int
    blue: int
    green: int
    alpha: int


@attrs(slots=True, frozen=True)
class Color:
    """
    Creates a Color from a basic attrs class, using the color_validator.
    """

    red = attrib(type=int, validator=color_validator)
    blue = attrib(type=int, validator=color_validator)
    green = attrib(type=int, validator=color_validator)
    alpha = attrib(type=int, validator=color_validator, default=0xFF)


def _get_color_size(mode: str):
    if mode == "RGB":
        return 3
    if mode == "RGBA":
        return 4
    raise NotImplementedError(f"{mode}'s size is unsupported")


def generate_from_bytes(data: bytes, mode: str) -> Iterable[Color]:
    size = _get_color_size(mode)
    while len(data):
        color = Color(*data[:size])
        data = data[size:]
        yield color
