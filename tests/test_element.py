"""
Unit tests for the rendering.element module.
"""

import pytest
from unittest.mock import Mock, MagicMock
from CardCrafter.rendering.element import Element, TextElement, ImageElement
from CardCrafter.positioning.position import AbsolutePosition
from CardCrafter.positioning.point import AbsolutePoint
from CardCrafter.positioning.size import AbsoluteSize
from CardCrafter.positioning.measure import AbsoluteMeasure, MeasureUnit
from CardCrafter.styling.text import TextStyle
from CardCrafter.styling.image import ImageStyle


class Test_Element:
    """Tests for abstract Element class."""

    def test_cannot_instantiate_directly(self):
        """Test that Element cannot be instantiated directly."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        with pytest.raises(TypeError):
            Element(position)


class Test_TextElement:
    """Tests for TextElement class."""

    def test_init(self):
        """Test TextElement initialization."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size, layer=1)
        
        style = TextStyle()
        text = "Hello World"
        
        element = TextElement(position, text, style)
        assert element._position == position
        assert element._text == text
        assert element._style == style

    def test_position_property(self):
        """Test position property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        element = TextElement(position, "Test", TextStyle())
        assert element.position == position

    def test_layer_property(self):
        """Test layer property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size, layer=3)
        
        element = TextElement(position, "Test", TextStyle())
        assert element.layer == 3

    def test_style_property(self):
        """Test style property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        style = TextStyle(font_size=24)
        element = TextElement(position, "Test", style)
        assert element.style == style

    def test_text_property(self):
        """Test text property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        text = "Sample Text"
        element = TextElement(position, text, TextStyle())
        assert element.text == text

    def test_render(self):
        """Test render method calls canvas.add_text."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        element = TextElement(position, "Test", TextStyle())
        
        # Mock canvas
        canvas = Mock()
        element.render(canvas)
        
        canvas.add_text.assert_called_once_with(element)


class Test_ImageElement:
    """Tests for ImageElement class."""

    def test_init(self):
        """Test ImageElement initialization."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size, layer=2)
        
        style = ImageStyle()
        image_path = "/path/to/image.png"
        
        element = ImageElement(position, image_path, style)
        assert element._position == position
        assert element._image_path == image_path
        assert element._style == style

    def test_position_property(self):
        """Test position property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        element = ImageElement(position, "test.png", ImageStyle())
        assert element.position == position

    def test_layer_property(self):
        """Test layer property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size, layer=5)
        
        element = ImageElement(position, "test.png", ImageStyle())
        assert element.layer == 5

    def test_image_path_property(self):
        """Test image_path property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        image_path = "/path/to/image.jpg"
        element = ImageElement(position, image_path, ImageStyle())
        assert element.image_path == image_path

    def test_style_property(self):
        """Test style property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        style = ImageStyle()
        element = ImageElement(position, "test.png", style)
        assert element.style == style

    def test_render(self):
        """Test render method calls canvas.add_image."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(50, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        position = AbsolutePosition(point, size)
        
        element = ImageElement(position, "test.png", ImageStyle())
        
        # Mock canvas
        canvas = Mock()
        element.render(canvas)
        
        canvas.add_image.assert_called_once_with(element)
