"""
Unit tests for the styling.text module.
"""

from CardCrafter.styling.color import Color
from CardCrafter.styling.text import TextAlignment, TextFormatting, TextStyle


class Test_TextAlignment:
    """Tests for TextAlignment enum."""

    def test_left_value(self):
        """Test that LEFT has correct value."""
        assert TextAlignment.LEFT.value == 'left'

    def test_center_value(self):
        """Test that CENTER has correct value."""
        assert TextAlignment.CENTER.value == 'center'

    def test_right_value(self):
        """Test that RIGHT has correct value."""
        assert TextAlignment.RIGHT.value == 'right'


class Test_TextFormatting:
    """Tests for TextFormatting enum."""

    def test_plain_value(self):
        """Test that PLAIN has correct value."""
        assert TextFormatting.PLAIN.value == 'plain'

    def test_markdown_value(self):
        """Test that MARKDOWN has correct value."""
        assert TextFormatting.MARKDOWN.value == 'markdown'


class Test_TextStyle:
    """Tests for TextStyle dataclass."""

    def test_default_values(self):
        """Test all default values."""
        style = TextStyle()
        assert style.alignment == TextAlignment.LEFT
        assert style.formatting == TextFormatting.PLAIN
        assert style.font_name == "arial.ttf"
        assert style.font_size == 12
        assert isinstance(style.font_color, Color)
        assert style.font_color.to_hex() == "#000000"

    def test_custom_alignment(self):
        """Test creating style with custom alignment."""
        style = TextStyle(alignment=TextAlignment.CENTER)
        assert style.alignment == TextAlignment.CENTER

    def test_custom_formatting(self):
        """Test creating style with custom formatting."""
        style = TextStyle(formatting=TextFormatting.MARKDOWN)
        assert style.formatting == TextFormatting.MARKDOWN

    def test_custom_font_name(self):
        """Test creating style with custom font name."""
        style = TextStyle(font_name="times.ttf")
        assert style.font_name == "times.ttf"

    def test_custom_font_size(self):
        """Test creating style with custom font size."""
        style = TextStyle(font_size=24)
        assert style.font_size == 24

    def test_custom_font_color(self):
        """Test creating style with custom font color."""
        color = Color("#ff0000")
        style = TextStyle(font_color=color)
        assert style.font_color == color
        assert style.font_color.to_hex() == "#ff0000"

    def test_all_custom_values(self):
        """Test creating style with all custom values."""
        color = Color("#0000ff")
        style = TextStyle(
            alignment=TextAlignment.RIGHT,
            formatting=TextFormatting.MARKDOWN,
            font_name="custom.ttf",
            font_size=18,
            font_color=color
        )
        assert style.alignment == TextAlignment.RIGHT
        assert style.formatting == TextFormatting.MARKDOWN
        assert style.font_name == "custom.ttf"
        assert style.font_size == 18
        assert style.font_color == color

    def test_is_dataclass(self):
        """Test that TextStyle is a dataclass."""
        style1 = TextStyle()
        style2 = TextStyle()
        # Dataclasses should be equal if their fields are equal
        assert style1.alignment == style2.alignment
        assert style1.formatting == style2.formatting
        assert style1.font_name == style2.font_name
        assert style1.font_size == style2.font_size
