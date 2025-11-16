"""
TODO
"""

from __future__ import annotations

from CardCrafter.positioning.measure import Measure, AbsoluteMeasure, RelativeMeasure


class Point:
    """
    Represents the point of a 2D element with x and y coordinates.
    """

    def __init__(self, x: Measure, y: Measure):
        self._x = x
        self._y = y

    def absolute(self, reference: AbsolutePoint) -> AbsolutePoint:
        """
        Converts the Point to absolute measurements based on reference dimensions.
        """
        abs_x = self._x.absolute(reference)
        abs_y = self._y.absolute(reference)
        return AbsolutePoint(abs_x, abs_y)


class AbsolutePoint(Point):
    """
    Represents an absolute 2D point.
    """

    def __init__(self, x: AbsoluteMeasure, y: AbsoluteMeasure):
        # Check arguments are absolute
        if not isinstance(x, AbsoluteMeasure) or not isinstance(y, AbsoluteMeasure):
            raise TypeError("x and y must be AbsoluteMeasure instances.")
        super().__init__(x, y)

    @property
    def x(self) -> AbsoluteMeasure:
        """
        Returns x as measure.
        """
        return self._x

    @property
    def y(self) -> AbsoluteMeasure:
        """
        Returns y as measure.
        """
        return self._y

    def to_tuple(self) -> tuple[int, int]:
        """
        Returns the absolute point as a tuple (x, y).
        """
        return (self._x.to_px(), self._y.to_px())
