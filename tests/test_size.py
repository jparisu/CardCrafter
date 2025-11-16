"""
Unit tests for the positioning.size module.
"""

import pytest
from CardCrafter.positioning.size import Size, AbsoluteSize
from CardCrafter.positioning.measure import AbsoluteMeasure, RelativeMeasure, MeasureUnit


class Test_Size:
    """Tests for Size class."""

    def test_init(self):
        """Test Size initialization."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = Size(width, height)
        assert size._width == width
        assert size._height == height

    def test_absolute_conversion(self):
        """Test conversion to absolute size."""
        width = RelativeMeasure(0.5)
        height = RelativeMeasure(0.3)
        size = Size(width, height)
        
        reference_width = AbsoluteMeasure(100, MeasureUnit.MM)
        reference_height = AbsoluteMeasure(200, MeasureUnit.MM)
        reference = AbsoluteSize(reference_width, reference_height)
        
        abs_size = size.absolute(reference)
        
        assert isinstance(abs_size, AbsoluteSize)
        assert abs_size.width._value == 50
        assert abs_size.height._value == 60


class Test_AbsoluteSize:
    """Tests for AbsoluteSize class."""

    def test_init_valid(self):
        """Test initialization with valid AbsoluteMeasure instances."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        assert size._width == width
        assert size._height == height

    def test_init_invalid_width(self):
        """Test that initialization fails with non-AbsoluteMeasure width."""
        width = RelativeMeasure(0.5)
        height = AbsoluteMeasure(200, MeasureUnit.MM)
        with pytest.raises(TypeError, match="Width and height must be AbsoluteMeasure instances"):
            AbsoluteSize(width, height)

    def test_init_invalid_height(self):
        """Test that initialization fails with non-AbsoluteMeasure height."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = RelativeMeasure(0.5)
        with pytest.raises(TypeError, match="Width and height must be AbsoluteMeasure instances"):
            AbsoluteSize(width, height)

    def test_width_property(self):
        """Test width property getter."""
        width = AbsoluteMeasure(150, MeasureUnit.MM)
        height = AbsoluteMeasure(250, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        assert size.width == width

    def test_height_property(self):
        """Test height property getter."""
        width = AbsoluteMeasure(150, MeasureUnit.MM)
        height = AbsoluteMeasure(250, MeasureUnit.MM)
        size = AbsoluteSize(width, height)
        assert size.height == height

    def test_to_tuple(self):
        """Test conversion to tuple of pixels."""
        width = AbsoluteMeasure(25.4, MeasureUnit.MM)  # 1 inch = 96 pixels at 96 DPI
        height = AbsoluteMeasure(50.8, MeasureUnit.MM)  # 2 inches = 192 pixels at 96 DPI
        size = AbsoluteSize(width, height)
        result = size.to_tuple()
        assert result == (96, 192)

    def test_to_tuple_different_units(self):
        """Test to_tuple with different measurement units."""
        width = AbsoluteMeasure(1, MeasureUnit.INCH)
        height = AbsoluteMeasure(2, MeasureUnit.INCH)
        size = AbsoluteSize(width, height)
        result = size.to_tuple()
        assert result == (96, 192)
