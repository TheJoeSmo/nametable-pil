from hypothesis import given
from hypothesis.strategies import binary, builds, composite
from nametable import Pattern as PatternMeta
from nametable import PatternMeta as PatternMetaMeta
from nametable_pil.Palette import Palette
from nametable_pil.Pattern import Pattern
from numpy import array_equal, asarray
from PIL import Image
from pytest import fixture

from tests.test_palette import rgb_palette, rgba_palette


def pattern_meta_meta():
    return builds(PatternMetaMeta, binary(min_size=16, max_size=16))


def pattern_meta():
    return builds(PatternMeta, pattern_meta_meta())


@composite
def pattern_rgb_data(draw):
    return draw(pattern_meta()), draw(rgb_palette())


def pattern_rgb():
    return builds(Pattern, pattern_meta(), rgb_palette())


@composite
def pattern_rgba_data(draw):
    return draw(pattern_meta()), draw(rgba_palette())


def pattern_rgba():
    return builds(Pattern, pattern_meta(), rgba_palette())


@fixture
def pattern_image():
    return Image.open("tests/static/test_pattern.png").quantize()


@fixture
def pattern_pattern(pattern_image):
    return Pattern(
        PatternMeta(PatternMetaMeta(bytes.fromhex("fefdfbf7e9debd78bf3fbfbff9fefdf8"))),
        Palette(pattern_image.palette),
    )


@given(pattern_rgb_data())
def test_initialization_rgb(data):
    Pattern(*data)


@given(pattern_rgba_data())
def test_initialization_rgba(data):
    Pattern(*data)


@given(pattern_rgb())
def test_creating_image_rgb(pattern):
    pattern.image


@given(pattern_rgba())
def test_creating_image_rgba(pattern):
    pattern.image


def test_image_correct(pattern_pattern: Pattern, pattern_image: Image.Image):
    assert pattern_pattern.image.mode == pattern_image.mode
    assert array_equal(asarray(pattern_pattern.image), asarray(pattern_image))
