from itertools import chain

from hypothesis import given
from hypothesis.strategies import builds, integers, lists

from nametable_pil.Color import Color, generate_from_bytes


def color_data():
    return lists(integers(0, 0xFF), min_size=3, max_size=4)


def rgb_color():
    return builds(Color, integers(0, 0xFF), integers(0, 0xFF), integers(0, 0xFF))


def rgba_color():
    return builds(Color, integers(0, 0xFF), integers(0, 0xFF), integers(0, 0xFF), integers(0, 0xFF))


@given(color_data())
def test_color_initialization(color_data):
    Color(*color_data)


@given(lists(rgb_color()))
def test_rgb_to_bytes(rgb_colors: tuple[Color]):
    color_groups = ((c.red, c.green, c.blue) for c in rgb_colors)
    color_data = bytes(chain(*color_groups))
    colors = generate_from_bytes(color_data, mode="RGB")
    for color, group in zip(colors, color_groups):
        assert color == Color(*group)


@given(lists(rgba_color()))
def test_rgba_to_bytes(rgba_colors: tuple[Color]):
    color_groups = ((c.red, c.green, c.blue, c.alpha) for c in rgba_colors)
    color_data = bytes(chain(*color_groups))
    colors = generate_from_bytes(color_data, mode="RGBA")
    for color, group in zip(colors, color_groups):
        assert color == Color(*group)
