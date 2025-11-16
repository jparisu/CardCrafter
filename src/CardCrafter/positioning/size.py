"""
Module for handling 2D size dimensions.

This module provides classes to represent sizes (width and height) with support
for both relative and absolute measurements.
"""

from __future__ import annotations

from CardCrafter.positioning.measure import Measure, AbsoluteMeasure


class Size:
    """
    Represents the size of an element with width and height dimensions.
    
    The dimensions can be either absolute or relative measurements.
    """

    def __init__(self, width: Measure, height: Measure):
        """
        Initialize a size with width and height.
        
        Args:
            width: The width as a Measure.
            height: The height as a Measure.
        """
        self._width = width
        self._height = height

    def absolute(self, reference: AbsoluteSize) -> AbsoluteSize:
        """
        Converts the size to absolute measurements.
        
        Args:
            reference: The reference size to use for converting relative measurements.
                      Relative width is calculated against reference width,
                      and relative height against reference height.
        
        Returns:
            An AbsoluteSize with all dimensions in absolute measurements.
        """
        abs_width = self._width.absolute(reference.width)
        abs_height = self._height.absolute(reference.height)
        return AbsoluteSize(abs_width, abs_height)


class AbsoluteSize(Size):
    """
    Represents a size with absolute width and height dimensions.
    
    Both width and height must be AbsoluteMeasure instances.
    """

    def __init__(self, width: AbsoluteMeasure, height: AbsoluteMeasure):
        """
        Initialize an absolute size.
        
        Args:
            width: The width as an AbsoluteMeasure.
            height: The height as an AbsoluteMeasure.
        
        Raises:
            TypeError: If width or height are not AbsoluteMeasure instances.
        """
        # Check arguments are absolute
        if not isinstance(width, AbsoluteMeasure) or not isinstance(height, AbsoluteMeasure):
            raise TypeError("Width and height must be AbsoluteMeasure instances.")
        super().__init__(width, height)

    @property
    def width(self) -> AbsoluteMeasure:
        """
        Gets the width dimension.
        
        Returns:
            The width as an AbsoluteMeasure.
        """
        return self._width

    @property
    def height(self) -> AbsoluteMeasure:
        """
        Gets the height dimension.
        
        Returns:
            The height as an AbsoluteMeasure.
        """
        return self._height

    def to_tuple(self) -> tuple[int, int]:
        """
        Converts the size to a tuple of pixel dimensions.
        
        Returns:
            A tuple (width, height) with dimensions in pixels as integers.
        """
        return (int(self.width.to_px()), int(self.height.to_px()))
