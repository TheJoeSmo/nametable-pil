from typing import Protocol

from attr import attrs
from nametable import PatternProtocol as MetaPatternProtocol
from PIL.Image import Image, fromarray

from nametable_pil.Palette import PaletteProtocol


class PatternProtocol(Protocol):
    pattern: MetaPatternProtocol
    palette: PaletteProtocol

    @property
    def image(self) -> Image:
        ...


@attrs(frozen=True, auto_attribs=True)
class Pattern:
    pattern: MetaPatternProtocol
    palette: PaletteProtocol

    @property
    def image(self) -> Image:
        image = fromarray(self.pattern.numpy_array, mode="P")
        image.palette = self.palette.palette
        return image
