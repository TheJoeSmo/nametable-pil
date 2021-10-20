from itertools import chain

from hypothesis import given
from hypothesis.strategies import builds, composite, lists
from PIL.ImagePalette import ImagePalette

from nametable_pil.Palette import Palette
from tests.test_color import rgb_color, rgba_color


@composite
def rgb_palette_data(draw):
    colors = draw(lists(rgb_color()))
    return ImagePalette("RGB", bytes(chain(*(bytes([c.red, c.green, c.blue]) for c in colors))))


def rgb_palette():
    return builds(Palette, rgb_palette_data())


@composite
def rgba_palette_data(draw):
    colors = draw(lists(rgba_color()))
    return ImagePalette("RGBA", bytes(chain(*((c.red, c.green, c.blue, c.alpha) for c in colors))))


def rgba_palette():
    return builds(Palette, rgba_palette_data())


@given(rgb_palette_data())
def test_initialization_rgb(data: ImagePalette):
    Palette(data)


@given(rgba_palette_data())
def test_initialization_rgba(data: ImagePalette):
    Palette(data)


@given(rgb_palette_data())
def test_rgb_colors_are_the_same(palette: ImagePalette):
    colors = Palette(palette).colors
    old_colors = palette.colors

    # Since the ImagePalette class stores the palette as an index, we just check if its there
    for c in colors:
        assert (c.red, c.green, c.blue) in old_colors


@given(rgba_palette_data())
def test_rgba_colors_are_the_same(palette: ImagePalette):
    colors = Palette(palette).colors
    old_colors = palette.colors

    # Since the ImagePalette class stores the palette as an index, we just check if its there
    for c in colors:
        assert (c.red, c.green, c.blue, c.alpha) in old_colors
