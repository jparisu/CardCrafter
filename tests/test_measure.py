"""
Unit tests for the positioning.measure module.
"""

import pytest
from CardCrafter.positioning.measure import (
    Measure,
    AbsoluteMeasure,
    RelativeMeasure,
    MeasureUnit,
)


class Test_AbsoluteMeasure:
    """Tests for AbsoluteMeasure class."""

    def test_init_default_unit(self):
        """Test initialization with default unit (MM)."""
        measure = AbsoluteMeasure(10)
        assert measure._value == 10
        assert measure._unit == MeasureUnit.MM

    def test_init_with_unit(self):
        """Test initialization with specific unit."""
        measure = AbsoluteMeasure(5, MeasureUnit.INCH)
        assert measure._value == 5
        assert measure._unit == MeasureUnit.INCH

    def test_to_mm_from_mm(self):
        """Test conversion from millimeters to millimeters."""
        measure = AbsoluteMeasure(10, MeasureUnit.MM)
        assert measure.to_mm() == 10.0

    def test_to_mm_from_inch(self):
        """Test conversion from inches to millimeters."""
        measure = AbsoluteMeasure(1, MeasureUnit.INCH)
        assert measure.to_mm() == 25.4

    def test_to_mm_from_pt(self):
        """Test conversion from points to millimeters."""
        measure = AbsoluteMeasure(10, MeasureUnit.PT)
        assert abs(measure.to_mm() - 3.52778) < 0.001

    def test_to_mm_from_px(self):
        """Test conversion from pixels to millimeters."""
        measure = AbsoluteMeasure(96, MeasureUnit.PX)
        assert measure.to_mm() == 25.4

    def test_to_cm(self):
        """Test conversion to centimeters."""
        measure = AbsoluteMeasure(100, MeasureUnit.MM)
        assert measure.to_cm() == 10.0

    def test_to_pts(self):
        """Test conversion to points."""
        measure = AbsoluteMeasure(10, MeasureUnit.MM)
        result = measure.to_pts()
        assert isinstance(result, int)
        assert result > 0

    def test_to_inches(self):
        """Test conversion to inches."""
        measure = AbsoluteMeasure(25.4, MeasureUnit.MM)
        assert abs(measure.to_inches() - 1.0) < 0.001

    def test_to_px_default_dpi(self):
        """Test conversion to pixels with default DPI."""
        measure = AbsoluteMeasure(25.4, MeasureUnit.MM)
        assert measure.to_px() == 96

    def test_to_px_custom_dpi(self):
        """Test conversion to pixels with custom DPI."""
        measure = AbsoluteMeasure(25.4, MeasureUnit.MM)
        assert measure.to_px(dpi=300.0) == 300

    def test_to_method(self):
        """Test the to() method with different units."""
        measure = AbsoluteMeasure(100, MeasureUnit.MM)
        assert measure.to(MeasureUnit.MM) == 100.0
        assert measure.to(MeasureUnit.INCH) == measure.to_inches()

    def test_to_method_unsupported_unit(self):
        """Test that to() raises ValueError for unsupported units."""
        measure = AbsoluteMeasure(10, MeasureUnit.MM)
        with pytest.raises(ValueError, match="Unsupported unit"):
            measure.to("invalid_unit")

    def test_from_mm(self):
        """Test factory method from_mm."""
        measure = AbsoluteMeasure.from_mm(50.0)
        assert measure._value == 50.0
        assert measure._unit == MeasureUnit.MM

    def test_from_cm(self):
        """Test factory method from_cm."""
        measure = AbsoluteMeasure.from_cm(5.0)
        assert measure._value == 50.0
        assert measure._unit == MeasureUnit.MM

    def test_from_inch(self):
        """Test factory method from_inch."""
        measure = AbsoluteMeasure.from_inch(2.0)
        assert measure._value == 2.0
        assert measure._unit == MeasureUnit.INCH

    def test_from_pt(self):
        """Test factory method from_pt."""
        measure = AbsoluteMeasure.from_pt(72)
        assert measure._value == 72
        assert measure._unit == MeasureUnit.PT

    def test_from_px(self):
        """Test factory method from_px."""
        measure = AbsoluteMeasure.from_px(96)
        assert measure._value == 96
        assert measure._unit == MeasureUnit.PX

    def test_from_unit(self):
        """Test factory method from_unit."""
        measure = AbsoluteMeasure.from_unit(10, MeasureUnit.INCH)
        assert measure._value == 10
        assert measure._unit == MeasureUnit.INCH

    def test_absolute_returns_self(self):
        """Test that absolute() returns itself."""
        measure = AbsoluteMeasure(10, MeasureUnit.MM)
        result = measure.absolute(AbsoluteMeasure(100, MeasureUnit.MM))
        assert result is measure

    def test_add_same_unit(self):
        """Test adding two measures with the same unit."""
        m1 = AbsoluteMeasure(10, MeasureUnit.MM)
        m2 = AbsoluteMeasure(5, MeasureUnit.MM)
        result = m1 + m2
        assert result._value == 15
        assert result._unit == MeasureUnit.MM

    def test_add_different_units(self):
        """Test adding two measures with different units."""
        m1 = AbsoluteMeasure(10, MeasureUnit.MM)
        m2 = AbsoluteMeasure(1, MeasureUnit.INCH)
        result = m1 + m2
        assert result._unit == MeasureUnit.MM
        assert abs(result._value - 35.4) < 0.001

    def test_add_relative_measure(self):
        """Test adding an absolute and relative measure."""
        absolute = AbsoluteMeasure(100, MeasureUnit.MM)
        relative = RelativeMeasure(0.5)
        result = absolute + relative
        assert isinstance(result, AbsoluteMeasure)

    def test_add_invalid_type(self):
        """Test that adding invalid type raises TypeError."""
        measure = AbsoluteMeasure(10, MeasureUnit.MM)
        with pytest.raises(TypeError):
            measure + "invalid"


class Test_RelativeMeasure:
    """Tests for RelativeMeasure class."""

    def test_init(self):
        """Test initialization."""
        measure = RelativeMeasure(0.5)
        assert measure._proportion == 0.5

    def test_proportion_property(self):
        """Test proportion property."""
        measure = RelativeMeasure(0.75)
        assert measure.proportion == 0.75

    def test_absolute_conversion(self):
        """Test conversion to absolute measure."""
        relative = RelativeMeasure(0.5)
        reference = AbsoluteMeasure(100, MeasureUnit.MM)
        result = relative.absolute(reference)
        assert isinstance(result, AbsoluteMeasure)
        assert result._value == 50
        assert result._unit == MeasureUnit.MM

    def test_add_relative_measures(self):
        """Test adding two relative measures."""
        m1 = RelativeMeasure(0.3)
        m2 = RelativeMeasure(0.2)
        result = m1 + m2
        assert isinstance(result, RelativeMeasure)
        assert result.proportion == 0.5

    def test_add_absolute_measure(self):
        """Test adding relative to absolute measure."""
        relative = RelativeMeasure(0.5)
        absolute = AbsoluteMeasure(100, MeasureUnit.MM)
        result = relative + absolute
        assert isinstance(result, AbsoluteMeasure)


class Test_MeasureUnit:
    """Tests for MeasureUnit enum."""

    def test_enum_values(self):
        """Test that all expected units are defined."""
        assert MeasureUnit.MM.value == "mm"
        assert MeasureUnit.INCH.value == "inch"
        assert MeasureUnit.PT.value == "pt"
        assert MeasureUnit.PX.value == "px"
