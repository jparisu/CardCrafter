"""
Unit tests for the styling.shape module.
"""

from CardCrafter.styling.color import Color
from CardCrafter.styling.shape import BorderStyle, LineStyle, Shape


class Test_Shape:
    """Tests for Shape enum."""

    def test_rectangle_value(self):
        """Test that RECTANGLE has correct value."""
        assert Shape.RECTANGLE.value == 'rectangle'


class Test_LineStyle:
    """Tests for LineStyle enum."""

    def test_solid_value(self):
        """Test that SOLID has correct value."""
        assert LineStyle.SOLID.value == 'solid'

    def test_dashed_value(self):
        """Test that DASHED has correct value."""
        assert LineStyle.DASHED.value == 'dashed'

    def test_dotted_value(self):
        """Test that DOTTED has correct value."""
        assert LineStyle.DOTTED.value == 'dotted'


class Test_BorderStyle:
    """Tests for BorderStyle class."""

    def test_init_with_defaults(self):
        """Test initialization with default line style."""
        color = Color("#ff0000")
        border = BorderStyle(color, 5)
        assert border._color == color
        assert border._width == 5
        assert border._line_style == LineStyle.SOLID

    def test_init_with_custom_line_style(self):
        """Test initialization with custom line style."""
        color = Color("#00ff00")
        border = BorderStyle(color, 10, LineStyle.DASHED)
        assert border._color == color
        assert border._width == 10
        assert border._line_style == LineStyle.DASHED

    def test_color_property(self):
        """Test color property getter."""
        color = Color("#0000ff")
        border = BorderStyle(color, 3)
        assert border.color == color

    def test_width_property(self):
        """Test width property getter."""
        color = Color("#ff0000")
        border = BorderStyle(color, 7)
        assert border.width == 7

    def test_line_style_property(self):
        """Test line_style property getter."""
        color = Color("#ff0000")
        border = BorderStyle(color, 5, LineStyle.DOTTED)
        assert border.line_style == LineStyle.DOTTED

    def test_different_widths(self):
        """Test border with different widths."""
        color = Color("#000000")
        for width in [1, 5, 10, 20]:
            border = BorderStyle(color, width)
            assert border.width == width

    def test_all_line_styles(self):
        """Test border with all line styles."""
        color = Color("#ffffff")
        for style in [LineStyle.SOLID, LineStyle.DASHED, LineStyle.DOTTED]:
            border = BorderStyle(color, 5, style)
            assert border.line_style == style
