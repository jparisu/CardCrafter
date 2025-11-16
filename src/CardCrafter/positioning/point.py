"""
Module for handling 2D point coordinates.

This module provides classes to represent points in 2D space with support
for both relative and absolute positioning.
"""

from __future__ import annotations

from CardCrafter.positioning.measure import AbsoluteMeasure, Measure


class Point:
    """
    Represents a point in 2D space with x and y coordinates.

    The coordinates can be either absolute or relative measurements.
    """

    def __init__(self, x: Measure, y: Measure):
        """
        Initialize a 2D point.

        Args:
            x: The x-coordinate as a Measure.
            y: The y-coordinate as a Measure.
        """
        self._x = x
        self._y = y

    def absolute(self, reference: AbsolutePoint) -> AbsolutePoint:
        """
        Converts the Point to absolute measurements.

        Args:
            reference: The reference point to use for converting relative measurements.
                      For relative coordinates, this defines the reference dimensions.

        Returns:
            An AbsolutePoint with all coordinates in absolute measurements.
        """
        abs_x = self._x.absolute(reference)
        abs_y = self._y.absolute(reference)
        return AbsolutePoint(abs_x, abs_y)


class AbsolutePoint(Point):
    """
    Represents a point in 2D space with absolute coordinates.

    Both x and y coordinates must be AbsoluteMeasure instances.
    """

    def __init__(self, x: AbsoluteMeasure, y: AbsoluteMeasure):
        """
        Initialize an absolute 2D point.

        Args:
            x: The x-coordinate as an AbsoluteMeasure.
            y: The y-coordinate as an AbsoluteMeasure.

        Raises:
            TypeError: If x or y are not AbsoluteMeasure instances.
        """
        # Check arguments are absolute
        if not isinstance(x, AbsoluteMeasure) or not isinstance(y, AbsoluteMeasure):
            raise TypeError("x and y must be AbsoluteMeasure instances.")
        super().__init__(x, y)

    @property
    def x(self) -> AbsoluteMeasure:
        """
        Gets the x-coordinate.

        Returns:
            The x-coordinate as an AbsoluteMeasure.
        """
        return self._x

    @property
    def y(self) -> AbsoluteMeasure:
        """
        Gets the y-coordinate.

        Returns:
            The y-coordinate as an AbsoluteMeasure.
        """
        return self._y

    def to_tuple(self) -> tuple[int, int]:
        """
        Converts the point to a tuple of pixel coordinates.

        Returns:
            A tuple (x, y) with coordinates in pixels as integers.
        """
        return (self._x.to_px(), self._y.to_px())
