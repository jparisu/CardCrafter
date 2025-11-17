"""
Unit tests for the carding.card module.
"""

from unittest.mock import Mock

from CardCrafter.carding.card import Card
from CardCrafter.positioning.measure import AbsoluteMeasure, MeasureUnit
from CardCrafter.positioning.point import AbsolutePoint
from CardCrafter.positioning.position import AbsolutePosition
from CardCrafter.positioning.size import AbsoluteSize
from CardCrafter.rendering.element import TextElement
from CardCrafter.styling.text import TextStyle


class Test_Card:
    """Tests for Card class."""

    def test_init(self):
        """Test Card initialization."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        elements = []
        card = Card(size, elements)
        assert card._size == size
        assert card._elements == elements

    def test_init_with_elements(self):
        """Test Card initialization with elements."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        elem_width = AbsoluteMeasure(50, MeasureUnit.MM)
        elem_height = AbsoluteMeasure(30, MeasureUnit.MM)
        elem_size = AbsoluteSize(elem_width, elem_height)
        position = AbsolutePosition(point, elem_size)

        element = TextElement(position, "Test", TextStyle())
        elements = [element]

        card = Card(size, elements)
        assert len(card._elements) == 1
        assert card._elements[0] == element

    def test_render_empty(self):
        """Test rendering card with no elements."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        card = Card(size, [])
        canvas = Mock()
        card.render(canvas)
        # No elements, so no render calls should be made

    def test_render_single_element(self):
        """Test rendering card with single element."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        elem_width = AbsoluteMeasure(50, MeasureUnit.MM)
        elem_height = AbsoluteMeasure(30, MeasureUnit.MM)
        elem_size = AbsoluteSize(elem_width, elem_height)
        position = AbsolutePosition(point, elem_size)

        element = TextElement(position, "Test", TextStyle())
        card = Card(size, [element])

        canvas = Mock()
        card.render(canvas)

        # Element should call canvas.add_text via its render method
        canvas.add_text.assert_called_once()

    def test_render_multiple_elements_by_layer(self):
        """Test rendering card with elements sorted by layer."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        # Create elements with different layers
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        elem_width = AbsoluteMeasure(50, MeasureUnit.MM)
        elem_height = AbsoluteMeasure(30, MeasureUnit.MM)
        elem_size = AbsoluteSize(elem_width, elem_height)

        AbsolutePosition(point, elem_size, layer=2)
        AbsolutePosition(point, elem_size, layer=0)
        AbsolutePosition(point, elem_size, layer=1)

        element1 = Mock(layer=2)
        element1.render = Mock()

        element2 = Mock(layer=0)
        element2.render = Mock()

        element3 = Mock(layer=1)
        element3.render = Mock()

        # Add in unsorted order
        card = Card(size, [element1, element2, element3])

        canvas = Mock()
        card.render(canvas)

        # Check that render was called on all elements
        element1.render.assert_called_once_with(canvas)
        element2.render.assert_called_once_with(canvas)
        element3.render.assert_called_once_with(canvas)
