"""
Module for handling measurements in different units.

This module provides classes to work with both absolute and relative measurements,
supporting various units like millimeters, inches, points, and pixels.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class Measure(ABC):
    """
    Abstract base class for measurement units.

    This class defines the interface for all measurement types in the CardCrafter system.
    Measurements can be either absolute (with specific units) or relative (proportional).
    """

    ###############################################################################
    # Abstract Methods

    @abstractmethod
    def absolute(self, reference: AbsoluteMeasure) -> AbsoluteMeasure:
        """
        Converts this measurement to an absolute measurement.

        Args:
            reference: The reference absolute measurement to use for conversion.
                      For relative measures, this defines the 100% base value.

        Returns:
            An AbsoluteMeasure instance representing this measurement in absolute terms.
        """
        pass

    @abstractmethod
    def __add__(self, other: Measure) -> Measure:
        """
        Adds two Measure instances together.

        Args:
            other: Another Measure instance to add to this one.

        Returns:
            A new Measure instance representing the sum.
        """
        pass



class RelativeMeasure(Measure):
    """
    Represents a measurement as a proportion of a reference size.

    This class is used for relative positioning where measurements are expressed
    as fractions of a reference size (e.g., 0.5 for 50%, 1.0 for 100%).
    """

    def __init__(self, proportion: float):
        """
        Initialize a relative measurement.

        Args:
            proportion: The proportion value (e.g., 0.5 for 50%, 1.0 for 100%).
        """
        self._proportion = proportion

    @property
    def proportion(self) -> float:
        """
        Gets the proportion value of this measurement.

        Returns:
            The proportion as a float (e.g., 0.5 for 50%).
        """
        return self._proportion

    ###############################################################################
    # Overridden Methods

    def absolute(self, reference: AbsoluteMeasure) -> AbsoluteMeasure:
        """
        Converts this relative measure to an absolute measure.

        Args:
            reference: The absolute measurement to use as the base (100%).

        Returns:
            An AbsoluteMeasure calculated as proportion * reference.
        """
        return AbsoluteMeasure(reference._value * self.proportion, reference._unit)

    def __add__(self, other: Measure) -> Measure:
        """
        Adds two measure instances.

        Args:
            other: Another Measure to add. Can be RelativeMeasure or AbsoluteMeasure.

        Returns:
            If other is RelativeMeasure: Returns RelativeMeasure with summed proportions.
            If other is AbsoluteMeasure: Delegates to AbsoluteMeasure's __add__ method.
        """
        if isinstance(other, RelativeMeasure):
            return RelativeMeasure(self.proportion + other.proportion)
        else:
            return other + self  # Delegate to AbsoluteMeasure's __add__


class MeasureUnit(Enum):
    """
    Enumeration of supported measurement units.

    Attributes:
        MM: Millimeters
        INCH: Inches
        PT: Points (1/72 of an inch)
        PX: Pixels (default DPI: 96)
    """
    MM = "mm"
    INCH = "inch"
    PT = "pt"
    PX = "px"


class AbsoluteMeasure(Measure):
    """
    Represents an absolute measurement with a specific unit.

    This class handles conversions between different measurement units commonly
    used in graphic design and printing (mm, inches, points, pixels).
    """

    def __init__(self, value: int|float, unit: MeasureUnit = MeasureUnit.MM):
        """
        Initialize an absolute measurement.

        Args:
            value: The numeric value of the measurement.
            unit: The unit of measurement (default: millimeters).
        """
        self._value = value
        self._unit = unit

    def to(self, unit: MeasureUnit) -> int|float:
        """
        Converts the measurement to the specified unit.

        Args:
            unit: The target unit to convert to.

        Returns:
            The measurement value in the target unit.

        Raises:
            ValueError: If the unit is not supported.
        """
        if unit == MeasureUnit.MM:
            return self.to_mm()
        elif unit == MeasureUnit.INCH:
            return self.to_inches()
        elif unit == MeasureUnit.PT:
            return self.to_pts()
        elif unit == MeasureUnit.PX:
            return self.to_px()
        else:
            raise ValueError(f"Unsupported unit: {unit}")


    def to_mm(self) -> float:
        """
        Converts the measurement to millimeters.

        Returns:
            The measurement value in millimeters.

        Raises:
            ValueError: If the unit is not supported.
        """
        if self._unit == MeasureUnit.MM:
            return float(self._value)
        elif self._unit == MeasureUnit.INCH:
            return float(self._value) * 25.4
        elif self._unit == MeasureUnit.PT:
            return float(self._value) * 0.352778
        elif self._unit == MeasureUnit.PX:
            # Assuming default DPI of 96 for pixel to mm conversion
            return (float(self._value) / 96.0) * 25.4
        else:
            raise ValueError(f"Unsupported unit: {self._unit}")

    def to_cm(self) -> float:
        """
        Converts the measurement to centimeters.

        Returns:
            The measurement value in centimeters.
        """
        return self.to_mm() / 10.0

    def to_pts(self) -> int:
        """
        Converts the measurement to points (1/72 of an inch).

        Returns:
            The measurement value in points as an integer.
        """
        if self._unit == "pt":
            return int(self._value)
        return int(self.to_mm() / 0.352778)

    def to_inches(self) -> float:
        """
        Converts the measurement to inches.

        Returns:
            The measurement value in inches.
        """
        if self._unit == "inch":
            return float(self._value)
        return float(self.to_mm() / 25.4)

    def to_px(self, dpi: float = 96.0) -> int:
        """
        Converts the measurement to pixels.

        Args:
            dpi: Dots per inch for conversion (default: 96).

        Returns:
            The measurement value in pixels as an integer.
        """
        if self._unit == "px":
            return int(self._value)
        return int((self.to_mm() / 25.4) * dpi)

    ###############################################################################
    # Factory Methods

    @classmethod
    def from_unit(cls, value: float, unit: MeasureUnit) -> Measure:
        """
        Creates an AbsoluteMeasure instance from a value and unit.

        Args:
            value: The numeric value of the measurement.
            unit: The unit of measurement.

        Returns:
            A new AbsoluteMeasure instance.
        """
        return cls(value=value, unit=unit)

    @classmethod
    def from_mm(cls, mm: float) -> Measure:
        """
        Creates an AbsoluteMeasure instance from millimeters.

        Args:
            mm: The value in millimeters.

        Returns:
            A new AbsoluteMeasure instance.
        """
        return cls(value=mm, unit=MeasureUnit.MM)

    @classmethod
    def from_cm(cls, cm: float) -> Measure:
        """
        Creates an AbsoluteMeasure instance from centimeters.

        Args:
            cm: The value in centimeters.

        Returns:
            A new AbsoluteMeasure instance (stored internally as mm).
        """
        return cls(value=cm*10, unit=MeasureUnit.MM)

    @classmethod
    def from_inch(cls, inch: float) -> Measure:
        """
        Creates an AbsoluteMeasure instance from inches.

        Args:
            inch: The value in inches.

        Returns:
            A new AbsoluteMeasure instance.
        """
        return cls(value=inch, unit=MeasureUnit.INCH)

    @classmethod
    def from_pt(cls, pt: int) -> Measure:
        """
        Creates an AbsoluteMeasure instance from points.

        Args:
            pt: The value in points (1/72 of an inch).

        Returns:
            A new AbsoluteMeasure instance.
        """
        return cls(value=pt, unit=MeasureUnit.PT)

    @classmethod
    def from_px(cls, int: float) -> Measure:
        """
        Creates an AbsoluteMeasure instance from pixels.

        Args:
            int: The value in pixels (assumes 96 DPI).

        Returns:
            A new AbsoluteMeasure instance.
        """
        return cls(value=int, unit=MeasureUnit.PX)

    ###############################################################################
    # Overridden Methods
    def absolute(self, reference: AbsoluteMeasure) -> AbsoluteMeasure:
        """
        Returns itself as it is already an absolute measure.

        Args:
            reference: Not used for absolute measures (kept for interface consistency).

        Returns:
            Self, as this measurement is already absolute.
        """
        return self

    def __add__(self, other: Measure) -> Measure:
        """
        Adds two Measure instances.

        Args:
            other: Another Measure to add. Can be RelativeMeasure or AbsoluteMeasure.

        Returns:
            A new AbsoluteMeasure with the sum.
            - If both measures have the same unit, the result uses that unit.
            - Otherwise, the result is in millimeters.

        Raises:
            TypeError: If other is not a Measure instance.
        """
        if isinstance(other, RelativeMeasure):
            return AbsoluteMeasure(self.to_mm() + other.absolute(self).to_mm())
        elif isinstance(other, AbsoluteMeasure):
            if self._unit == other._unit:
                return AbsoluteMeasure(self._value + other._value, self._unit)
            else:
                return AbsoluteMeasure(value=self.to_mm() + other.to_mm(), unit=MeasureUnit.MM)
        else:
            raise TypeError("Can only add AbsoluteMeasure to AbsoluteMeasure or RelativeMeasure")
