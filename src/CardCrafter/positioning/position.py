"""
TODO
"""

from __future__ import annotations

from CardCrafter.positioning.measure import Measure, AbsoluteMeasure
from CardCrafter.positioning.size import Size, AbsoluteSize
from CardCrafter.positioning.point import Point, AbsolutePoint


class Position:
    """
    Represents a 2D position of an element.
    """

    def __init__(
            self,
            point: Point,
            size: Measure,
            layer: int = 0,
    ):
        self._point = point
        self._size = size
        self._layer = layer


    def absolute(self, reference: AbsoluteSize) -> AbsolutePosition:
        """
        Converts the position to absolute measurements based on reference dimensions.
        """
        abs_point = self._point.absolute(reference.width)
        abs_size = self._size.absolute(reference)
        return AbsolutePosition(abs_point, abs_size, self._layer)

    @property
    def layer(self) -> int:
        """
        Returns the layer of the position.
        """
        return self._layer


class AbsolutePosition(Position):
    """
    Represents the absolute 2D position of an element.
    """
    def __init__(
            self,
            point: AbsolutePoint,
            size: AbsoluteSize,
            layer: int = 0,
    ):
        # Check arguments are absolute
        if not isinstance(point, AbsolutePoint) or not isinstance(size, AbsoluteSize):
            raise TypeError("x, y, and size must be AbsoluteMeasure and AbsoluteSize instances.")
        super().__init__(point, size, layer)

    @property
    def x(self) -> AbsoluteMeasure:
        """
        Returns the x position in millimeters.
        """
        return self._point.x

    @property
    def y(self) -> AbsoluteMeasure:
        """
        Returns the y position in millimeters.
        """
        return self._point.y

    @property
    def size(self) -> AbsoluteSize:
        """
        Returns the size.
        """
        return self._size

    @property
    def width(self) -> AbsoluteMeasure:
        """
        Returns the width in millimeters.
        """
        return self._size.width

    @property
    def height(self) -> AbsoluteMeasure:
        """
        Returns the height in millimeters.
        """
        return self._size.height


    def start_corner(self) -> AbsolutePoint:
        """
        Returns the top-left corner (x, y) of the position.
        """
        return self._point

    def to_box(self) -> tuple[int, int, int, int]:
        """
        Returns the absolute position as a tuple (x, y, width, height).
        """
        return (
            self._point.x.to_px(),
            self._point.y.to_px(),
            self._point.x.to_px() + self._size.width.to_px(),
            self._point.y.to_px() + self._size.height.to_px(),
        )
