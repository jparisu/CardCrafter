"""
TODO
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class Measure(ABC):
    """
    Represents a measurement unit for positioning elements.
    """

    ###############################################################################
    # Abstract Methods

    @abstractmethod
    def absolute(self, reference: AbsoluteMeasure) -> AbsoluteMeasure:
        """
        Calculates the absolute position based on a reference point.
        """
        pass

    @abstractmethod
    def __add__(self, other: Measure) -> Measure:
        """
        Adds two Measure instances.
        """
        pass



class RelativeMeasure(Measure):
    """
    Represents a relative measurement unit for positioning elements.
    """

    def __init__(self, proportion: float):
        self._proportion = proportion

    @property
    def proportion(self) -> float:
        """
        Returns the measurement as a proportion.
        """
        return self._proportion

    ###############################################################################
    # Overridden Methods

    def absolute(self, reference: AbsoluteMeasure) -> AbsoluteMeasure:
        """
        Converts the relative measure to an absolute measure based on the reference.
        """
        return AbsoluteMeasure(reference._value * self.proportion, reference._unit)

    def __add__(self, other: Measure) -> Measure:
        """
        Adds two measure instances.

        If the other instance is a RelativeMeasure, their proportions are added.
        If the other instance is an AbsoluteMeasure, the relative measure is
         converted using other as reference, and then their absolute values are added.
        """
        if isinstance(other, RelativeMeasure):
            return RelativeMeasure(self.proportion + other.proportion)
        else:
            return other + self  # Delegate to AbsoluteMeasure's __add__


class MeasureUnit(Enum):
    MM = "mm"
    INCH = "inch"
    PT = "pt"
    PX = "px"


class AbsoluteMeasure(Measure):
    """
    Represents an absolute measurement unit for positioning elements.
    """

    def __init__(self, value: int|float, unit: MeasureUnit = MeasureUnit.MM):
        self._value = value
        self._unit = unit

    def to(self, unit: MeasureUnit) -> int|float:
        """
        Converts the measurement to the specified unit.
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
        """
        return self.to_mm() / 10.0

    def to_pts(self) -> int:
        """
        Converts the measurement to points.
        """
        if self._unit == "pt":
            return int(self._value)
        return int(self.to_mm() / 0.352778)

    def to_inches(self) -> float:
        """
        Converts the measurement to inches.
        """
        if self._unit == "inch":
            return float(self._value)
        return float(self.to_mm() / 25.4)

    def to_px(self, dpi: float = 96.0) -> int:
        """
        Converts the measurement to pixels.
        Default DPI is set to 96.
        """
        if self._unit == "px":
            return int(self._value)
        return int((self.to_mm() / 25.4) * dpi)

    ###############################################################################
    # Factory Methods

    @classmethod
    def from_unit(cls, value: float, unit: MeasureUnit) -> "Measure":
        """
        Creates a Measure instance from the specified unit.
        """
        return cls(value=value, unit=unit)

    @classmethod
    def from_mm(cls, mm: float) -> "Measure":
        """
        Creates a Measure instance from millimeters.
        """
        return cls(value=mm, unit=MeasureUnit.MM)

    @classmethod
    def from_cm(cls, cm: float) -> "Measure":
        """
        Creates a Measure instance from centimeters.
        """
        return cls(value=cm*10, unit=MeasureUnit.MM)

    @classmethod
    def from_inch(cls, inch: float) -> "Measure":
        """
        Creates a Measure instance from inches.
        """
        return cls(value=inch, unit=MeasureUnit.INCH)

    @classmethod
    def from_pt(cls, pt: int) -> "Measure":
        """
        Creates a Measure instance from points.
        """
        return cls(value=pt, unit=MeasureUnit.PT)

    @classmethod
    def from_px(cls, int: float) -> "Measure":
        """
        Creates a Measure instance from pixels.
        Default DPI is set to 96.
        """
        return cls(value=int, unit=MeasureUnit.PX)

    ###############################################################################
    # Overridden Methods
    def absolute(self, reference: AbsoluteMeasure) -> AbsoluteMeasure:
        """
        Returns itself as it is already an absolute measure.
        """
        return self

    def __add__(self, other: Measure) -> Measure:
        """
        Adds two Measure instances.

        If the other instance is a RelativeMeasure, it is converted to an absolute measure.
        If the other instance is an AbsoluteMeasure:
            if they share the same unit, their values are added directly.
            otherwise, move them to mm and add.
        """
        if isinstance(other, RelativeMeasure):
            return AbsoluteMeasure(self.mm + other.absolute(self).mm)
        elif isinstance(other, AbsoluteMeasure):
            if self._unit == other.unit:
                return AbsoluteMeasure(self._value + other._value, self._unit)
            else:
                return AbsoluteMeasure(value=self.mm + other.mm, unit=MeasureUnit.MM)
        else:
            raise TypeError("Can only add AbsoluteMeasure to AbsoluteMeasure or RelativeMeasure")
