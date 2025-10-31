"""
Tests for style classes.
"""

import pytest

from CardCrafter.styles import ImageStyle, Style, TextStyle
from CardCrafter.value_objects import Align, FitMode


class TestStyle:
    """Tests for base Style class."""

    def test_style_creation(self):
        """Test creating a Style with default values."""
        style = Style()
        assert style.color == "#000000"
        assert style.opacity == 1.0

    def test_style_with_custom_values(self):
        """Test creating a Style with custom values."""
        style = Style(color="#FF0000", opacity=0.5)
        assert style.color == "#FF0000"
        assert style.opacity == 0.5

    def test_style_invalid_opacity_high(self):
        """Test that opacity > 1.0 raises ValueError."""
        with pytest.raises(ValueError, match="Opacity must be between 0.0 and 1.0"):
            Style(opacity=1.5)

    def test_style_invalid_opacity_low(self):
        """Test that opacity < 0.0 raises ValueError."""
        with pytest.raises(ValueError, match="Opacity must be between 0.0 and 1.0"):
            Style(opacity=-0.1)


class TestTextStyle:
    """Tests for TextStyle class."""

    def test_textstyle_creation_default(self):
        """Test creating a TextStyle with default values."""
        style = TextStyle()
        assert style.color == "#000000"
        assert style.opacity == 1.0
        assert style.fontPath == ""
        assert style.fontSize == 12
        assert style.lineHeight == 1.0
        assert style.align == Align.Left
        assert style.wrap is True
        assert style.ellipsis is False
        assert style.strokeColor is None
        assert style.strokeWidth == 0
        assert style.letterSpacing == 0.0

    def test_textstyle_creation_custom(self):
        """Test creating a TextStyle with custom values."""
        style = TextStyle(
            color="#FFFFFF",
            opacity=0.8,
            fontPath="/path/to/font.ttf",
            fontSize=24,
            lineHeight=1.5,
            align=Align.Center,
            wrap=False,
            ellipsis=True,
            strokeColor="#000000",
            strokeWidth=2,
            letterSpacing=1.2,
        )
        assert style.color == "#FFFFFF"
        assert style.opacity == 0.8
        assert style.fontPath == "/path/to/font.ttf"
        assert style.fontSize == 24
        assert style.lineHeight == 1.5
        assert style.align == Align.Center
        assert style.wrap is False
        assert style.ellipsis is True
        assert style.strokeColor == "#000000"
        assert style.strokeWidth == 2
        assert style.letterSpacing == 1.2

    def test_textstyle_invalid_fontsize(self):
        """Test that invalid fontSize raises ValueError."""
        with pytest.raises(ValueError, match="fontSize must be positive"):
            TextStyle(fontSize=0)

        with pytest.raises(ValueError, match="fontSize must be positive"):
            TextStyle(fontSize=-10)

    def test_textstyle_invalid_lineheight(self):
        """Test that invalid lineHeight raises ValueError."""
        with pytest.raises(ValueError, match="lineHeight must be positive"):
            TextStyle(lineHeight=0)

        with pytest.raises(ValueError, match="lineHeight must be positive"):
            TextStyle(lineHeight=-1.0)

    def test_textstyle_invalid_strokewidth(self):
        """Test that invalid strokeWidth raises ValueError."""
        with pytest.raises(ValueError, match="strokeWidth must be non-negative"):
            TextStyle(strokeWidth=-1)


class TestImageStyle:
    """Tests for ImageStyle class."""

    def test_imagestyle_creation_default(self):
        """Test creating an ImageStyle with default values."""
        style = ImageStyle()
        assert style.color == "#FFFFFF"
        assert style.opacity == 1.0
        assert style.fit == FitMode.Cover
        assert style.radius == 0
        assert style.tint is None
        assert style.contrast == 0.0
        assert style.brightness == 0.0

    def test_imagestyle_creation_custom(self):
        """Test creating an ImageStyle with custom values."""
        style = ImageStyle(
            color="#000000",
            opacity=0.7,
            fit=FitMode.Contain,
            radius=10,
            tint="#FF0000",
            contrast=0.5,
            brightness=-0.2,
        )
        assert style.color == "#000000"
        assert style.opacity == 0.7
        assert style.fit == FitMode.Contain
        assert style.radius == 10
        assert style.tint == "#FF0000"
        assert style.contrast == 0.5
        assert style.brightness == -0.2

    def test_imagestyle_invalid_radius(self):
        """Test that invalid radius raises ValueError."""
        with pytest.raises(ValueError, match="radius must be non-negative"):
            ImageStyle(radius=-5)

    def test_imagestyle_invalid_contrast_high(self):
        """Test that contrast > 1.0 raises ValueError."""
        with pytest.raises(ValueError, match="contrast must be between -1.0 and 1.0"):
            ImageStyle(contrast=1.5)

    def test_imagestyle_invalid_contrast_low(self):
        """Test that contrast < -1.0 raises ValueError."""
        with pytest.raises(ValueError, match="contrast must be between -1.0 and 1.0"):
            ImageStyle(contrast=-1.5)

    def test_imagestyle_invalid_brightness_high(self):
        """Test that brightness > 1.0 raises ValueError."""
        with pytest.raises(ValueError, match="brightness must be between -1.0 and 1.0"):
            ImageStyle(brightness=1.5)

    def test_imagestyle_invalid_brightness_low(self):
        """Test that brightness < -1.0 raises ValueError."""
        with pytest.raises(ValueError, match="brightness must be between -1.0 and 1.0"):
            ImageStyle(brightness=-1.5)
