from functools import cached_property
from typing import Protocol

from attr import attrib, attrs
from PIL.ImagePalette import ImagePalette

from nametable_pil.Color import Color, generate_from_bytes
from nametable_pil.validators import rgb_validator


class PaletteProtocol(Protocol):
    palette: ImagePalette

    colors: tuple[Color, ...]


@attrs(frozen=True)
class Palette:
    palette: ImagePalette = attrib(validator=rgb_validator)

    @cached_property
    def colors(self) -> tuple[Color, ...]:
        return tuple(generate_from_bytes(self.palette.tobytes(), self.palette.mode))
