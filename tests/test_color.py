"""
Unit tests for the styling.color module.
"""

import pytest
from CardCrafter.styling.color import Color, COLORS


class Test_Color:
    """Tests for Color class."""

    def test_init(self):
        """Test Color initialization."""
        color = Color("#ff0000")
        assert color._hex == "#ff0000"

    def test_from_rgb(self):
        """Test creating color from RGB values."""
        color = Color.from_rgb(255, 0, 0)
        assert color.to_hex() == "#ff0000"

    def test_from_rgb_mixed(self):
        """Test creating color from mixed RGB values."""
        color = Color.from_rgb(128, 64, 32)
        assert color.to_hex() == "#804020"

    def test_from_hex(self):
        """Test creating color from hex string."""
        color = Color.from_hex("#00ff00")
        assert color.to_hex() == "#00ff00"

    def test_from_name_red(self):
        """Test creating color from name 'red'."""
        color = Color.from_name("red")
        assert color.to_hex() == "#ff0000"

    def test_from_name_blue(self):
        """Test creating color from name 'blue'."""
        color = Color.from_name("blue")
        assert color.to_hex() == "#0000ff"

    def test_from_name_case_insensitive(self):
        """Test that color names are case-insensitive."""
        color1 = Color.from_name("RED")
        color2 = Color.from_name("red")
        assert color1.to_hex() == color2.to_hex()

    def test_from_name_invalid(self):
        """Test that invalid color name raises ValueError."""
        with pytest.raises(ValueError, match="Color name 'invalid' is not defined"):
            Color.from_name("invalid")

    def test_to_rgb(self):
        """Test conversion to RGB."""
        color = Color("#ff8040")
        assert color.to_rgb() == (255, 128, 64)

    def test_to_rgb_black(self):
        """Test conversion to RGB for black."""
        color = Color("#000000")
        assert color.to_rgb() == (0, 0, 0)

    def test_to_rgb_white(self):
        """Test conversion to RGB for white."""
        color = Color("#ffffff")
        assert color.to_rgb() == (255, 255, 255)

    def test_to_hex(self):
        """Test to_hex method."""
        color = Color("#abcdef")
        assert color.to_hex() == "#abcdef"

    def test_define_color(self):
        """Test defining a new color."""
        Color.define_color("custom", "#123456")
        assert "custom" in COLORS
        assert COLORS["custom"] == "#123456"
        
        # Create color from newly defined name
        color = Color.from_name("custom")
        assert color.to_hex() == "#123456"

    def test_define_color_case_insensitive(self):
        """Test that define_color is case-insensitive."""
        Color.define_color("MyColor", "#abcdef")
        assert "mycolor" in COLORS
        color = Color.from_name("MYCOLOR")
        assert color.to_hex() == "#abcdef"

    def test_predefined_colors(self):
        """Test that all predefined colors exist."""
        expected_colors = ["red", "green", "blue", "black", "white", "yellow", "cyan", "magenta"]
        for color_name in expected_colors:
            assert color_name in COLORS
            color = Color.from_name(color_name)
            assert isinstance(color, Color)
