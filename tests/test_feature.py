"""
Unit tests for the carding.feature module.
"""

import pytest
from CardCrafter.carding.feature import Feature, TextFeature, ImageFeature
from CardCrafter.rendering.element import TextElement, ImageElement
from CardCrafter.positioning.position import Position
from CardCrafter.positioning.point import Point
from CardCrafter.positioning.size import Size, AbsoluteSize
from CardCrafter.positioning.measure import AbsoluteMeasure, MeasureUnit
from CardCrafter.styling.text import TextStyle


class Test_Feature:
    """Tests for abstract Feature class."""

    def test_cannot_instantiate_directly(self):
        """Test that Feature cannot be instantiated directly."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        with pytest.raises(TypeError):
            Feature("name", position)


class Test_TextFeature:
    """Tests for TextFeature class."""

    def test_init_minimal(self):
        """Test TextFeature initialization with minimal args."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("title", position)
        assert feature._name == "title"
        assert feature._position == position
        assert feature._description == ""
        assert isinstance(feature._style, TextStyle)

    def test_init_with_description(self):
        """Test TextFeature initialization with description."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("title", position, description="Card title")
        assert feature.description == "Card title"

    def test_init_with_style(self):
        """Test TextFeature initialization with custom style."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        style = TextStyle(font_size=24)
        feature = TextFeature("title", position, style=style)
        assert feature.style == style

    def test_name_property(self):
        """Test name property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("test_name", position)
        assert feature.name == "test_name"

    def test_position_property(self):
        """Test position property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("title", position)
        assert feature.position == position

    def test_description_property(self):
        """Test description property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("title", position, description="Test description")
        assert feature.description == "Test description"

    def test_style_property(self):
        """Test style property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        style = TextStyle(font_size=18)
        feature = TextFeature("title", position, style=style)
        assert feature.style == style

    def test_generate_element_valid(self):
        """Test generating element with valid string value."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("title", position)
        
        card_width = AbsoluteMeasure(100, MeasureUnit.MM)
        card_height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(card_width, card_height)
        
        element = feature.generate_element(card_size, "Test Text")
        assert isinstance(element, TextElement)
        assert element.text == "Test Text"

    def test_generate_element_invalid_type(self):
        """Test that generating element with wrong type raises TypeError."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("title", position)
        
        card_width = AbsoluteMeasure(100, MeasureUnit.MM)
        card_height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(card_width, card_height)
        
        with pytest.raises(TypeError, match="Expected value of type str"):
            feature.generate_element(card_size, 123)

    def test_default_not_set(self):
        """Test default method when no default is set."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("title", position)
        
        card_width = AbsoluteMeasure(100, MeasureUnit.MM)
        card_height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(card_width, card_height)
        
        result = feature.default(card_size)
        assert result is None

    def test_set_default_and_use(self):
        """Test setting and using default value."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = TextFeature("title", position)
        feature.set_default(value="Default Title")
        
        card_width = AbsoluteMeasure(100, MeasureUnit.MM)
        card_height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(card_width, card_height)
        
        result = feature.default(card_size)
        assert isinstance(result, TextElement)
        assert result.text == "Default Title"


class Test_ImageFeature:
    """Tests for ImageFeature class."""

    def test_init_minimal(self):
        """Test ImageFeature initialization with minimal args."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = ImageFeature("icon", position)
        assert feature._name == "icon"
        assert feature._position == position
        assert feature._description == ""

    def test_init_with_description(self):
        """Test ImageFeature initialization with description."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = ImageFeature("icon", position, description="Card icon")
        assert feature.description == "Card icon"

    def test_generate_element_valid(self):
        """Test generating element with valid image path."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = ImageFeature("icon", position)
        
        card_width = AbsoluteMeasure(100, MeasureUnit.MM)
        card_height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(card_width, card_height)
        
        element = feature.generate_element(card_size, "/path/to/image.png")
        assert isinstance(element, ImageElement)
        assert element.image_path == "/path/to/image.png"

    def test_generate_element_invalid_type(self):
        """Test that generating element with wrong type raises TypeError."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(50, MeasureUnit.MM)
        height = AbsoluteMeasure(30, MeasureUnit.MM)
        size = Size(width, height)
        position = Position(point, size)
        
        feature = ImageFeature("icon", position)
        
        card_width = AbsoluteMeasure(100, MeasureUnit.MM)
        card_height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(card_width, card_height)
        
        with pytest.raises(TypeError, match="Expected value of type str"):
            feature.generate_element(card_size, 123)
