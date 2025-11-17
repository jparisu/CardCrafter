"""
Unit tests for the positioning.position module.
"""

import pytest

from CardCrafter.positioning.measure import AbsoluteMeasure, MeasureUnit, RelativeMeasure
from CardCrafter.positioning.point import AbsolutePoint, Point
from CardCrafter.positioning.position import AbsolutePosition, Position
from CardCrafter.positioning.size import AbsoluteSize, Size


class Test_Position:
    """Tests for Position class."""

    def test_init(self):
        """Test Position initialization."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = Size(width, height)

        position = Position(point, size, layer=5)
        assert position._point == point
        assert position._size == size
        assert position._layer == 5

    def test_init_default_layer(self):
        """Test Position initialization with default layer."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = Size(width, height)

        position = Position(point, size)
        assert position._layer == 0

    def test_layer_property(self):
        """Test layer property getter."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = Size(width, height)

        position = Position(point, size, layer=3)
        assert position.layer == 3


class Test_AbsolutePosition:
    """Tests for AbsolutePosition class."""

    def test_init_valid(self):
        """Test initialization with valid absolute instances."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        position = AbsolutePosition(point, size, layer=2)
        assert position._point == point
        assert position._size == size
        assert position._layer == 2

    def test_init_invalid_point(self):
        """Test that initialization fails with non-AbsolutePoint."""
        x = RelativeMeasure(0.5)
        y = RelativeMeasure(0.3)
        point = Point(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        with pytest.raises(TypeError):
            AbsolutePosition(point, size)

    def test_init_invalid_size(self):
        """Test that initialization fails with non-AbsoluteSize."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = RelativeMeasure(0.5)
        height = RelativeMeasure(0.3)
        size = Size(width, height)

        with pytest.raises(TypeError):
            AbsolutePosition(point, size)

    def test_x_property(self):
        """Test x property getter."""
        x = AbsoluteMeasure(15, MeasureUnit.MM)
        y = AbsoluteMeasure(25, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        position = AbsolutePosition(point, size)
        assert position.x == x

    def test_y_property(self):
        """Test y property getter."""
        x = AbsoluteMeasure(15, MeasureUnit.MM)
        y = AbsoluteMeasure(25, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        position = AbsolutePosition(point, size)
        assert position.y == y

    def test_size_property(self):
        """Test size property getter."""
        x = AbsoluteMeasure(15, MeasureUnit.MM)
        y = AbsoluteMeasure(25, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        position = AbsolutePosition(point, size)
        assert position.size == size

    def test_width_property(self):
        """Test width property getter."""
        x = AbsoluteMeasure(15, MeasureUnit.MM)
        y = AbsoluteMeasure(25, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        position = AbsolutePosition(point, size)
        assert position.width == width

    def test_height_property(self):
        """Test height property getter."""
        x = AbsoluteMeasure(15, MeasureUnit.MM)
        y = AbsoluteMeasure(25, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        position = AbsolutePosition(point, size)
        assert position.height == height

    def test_start_corner(self):
        """Test start_corner method."""
        x = AbsoluteMeasure(15, MeasureUnit.MM)
        y = AbsoluteMeasure(25, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)

        position = AbsolutePosition(point, size)
        assert position.start_corner() == point

    def test_to_box(self):
        """Test conversion to bounding box."""
        x = AbsoluteMeasure(25.4, MeasureUnit.MM)  # 96 pixels
        y = AbsoluteMeasure(25.4, MeasureUnit.MM)  # 96 pixels
        point = AbsolutePoint(x, y)
        width = AbsoluteMeasure(25.4, MeasureUnit.MM)  # 96 pixels
        height = AbsoluteMeasure(50.8, MeasureUnit.MM)  # 192 pixels
        size = AbsoluteSize(width, height)

        position = AbsolutePosition(point, size)
        box = position.to_box()
        assert box == (96, 96, 192, 288)  # (x1, y1, x2, y2)
