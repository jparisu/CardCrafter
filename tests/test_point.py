"""
Unit tests for the positioning.point module.
"""

import pytest
from CardCrafter.positioning.point import Point, AbsolutePoint
from CardCrafter.positioning.measure import AbsoluteMeasure, RelativeMeasure, MeasureUnit


class Test_Point:
    """Tests for Point class."""

    def test_init(self):
        """Test Point initialization."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        assert point._x == x
        assert point._y == y

    def test_absolute_conversion(self):
        """Test conversion to absolute point."""
        x = RelativeMeasure(0.5)
        y = RelativeMeasure(0.3)
        point = Point(x, y)
        
        reference = AbsoluteMeasure(100, MeasureUnit.MM)
        abs_point = point.absolute(reference)
        
        assert isinstance(abs_point, AbsolutePoint)
        assert abs_point.x._value == 50
        assert abs_point.y._value == 30


class Test_AbsolutePoint:
    """Tests for AbsolutePoint class."""

    def test_init_valid(self):
        """Test initialization with valid AbsoluteMeasure instances."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        assert point._x == x
        assert point._y == y

    def test_init_invalid_x(self):
        """Test that initialization fails with non-AbsoluteMeasure x."""
        x = RelativeMeasure(0.5)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        with pytest.raises(TypeError, match="x and y must be AbsoluteMeasure instances"):
            AbsolutePoint(x, y)

    def test_init_invalid_y(self):
        """Test that initialization fails with non-AbsoluteMeasure y."""
        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = RelativeMeasure(0.5)
        with pytest.raises(TypeError, match="x and y must be AbsoluteMeasure instances"):
            AbsolutePoint(x, y)

    def test_x_property(self):
        """Test x property getter."""
        x = AbsoluteMeasure(15, MeasureUnit.MM)
        y = AbsoluteMeasure(25, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        assert point.x == x

    def test_y_property(self):
        """Test y property getter."""
        x = AbsoluteMeasure(15, MeasureUnit.MM)
        y = AbsoluteMeasure(25, MeasureUnit.MM)
        point = AbsolutePoint(x, y)
        assert point.y == y

    def test_to_tuple(self):
        """Test conversion to tuple of pixels."""
        x = AbsoluteMeasure(25.4, MeasureUnit.MM)  # 1 inch = 96 pixels at 96 DPI
        y = AbsoluteMeasure(50.8, MeasureUnit.MM)  # 2 inches = 192 pixels at 96 DPI
        point = AbsolutePoint(x, y)
        result = point.to_tuple()
        assert result == (96, 192)

    def test_to_tuple_different_units(self):
        """Test to_tuple with different measurement units."""
        x = AbsoluteMeasure(1, MeasureUnit.INCH)
        y = AbsoluteMeasure(2, MeasureUnit.INCH)
        point = AbsolutePoint(x, y)
        result = point.to_tuple()
        assert result == (96, 192)
