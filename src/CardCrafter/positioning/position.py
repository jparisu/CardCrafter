"""
Module for handling 2D positions with location and size.

This module provides classes to represent positions of elements in 2D space,
combining a point location with a size and an optional layer.
"""

from __future__ import annotations

from CardCrafter.positioning.measure import AbsoluteMeasure, Measure
from CardCrafter.positioning.point import AbsolutePoint, Point
from CardCrafter.positioning.size import AbsoluteSize


class Position:
    """
    Represents a 2D position of an element with location, size, and layer.

    This combines a point (x, y coordinates), a size (width, height),
    and an optional layer value for z-ordering.
    """

    def __init__(
            self,
            point: Point,
            size: Measure,
            layer: int = 0,
    ):
        """
        Initialize a position.

        Args:
            point: The top-left corner point of the element.
            size: The size of the element.
            layer: The z-order layer (higher values appear on top). Default is 0.
        """
        self._point = point
        self._size = size
        self._layer = layer


    def absolute(self, reference: AbsoluteSize) -> AbsolutePosition:
        """
        Converts the position to absolute measurements.

        Args:
            reference: The reference size to use for converting relative measurements.

        Returns:
            An AbsolutePosition with all measurements in absolute values.
        """
        abs_point = self._point.absolute(reference.width)
        abs_size = self._size.absolute(reference)
        return AbsolutePosition(abs_point, abs_size, self._layer)

    @property
    def layer(self) -> int:
        """
        Gets the layer (z-order) of the position.

        Returns:
            The layer as an integer.
        """
        return self._layer


class AbsolutePosition(Position):
    """
    Represents a 2D position with absolute measurements.

    All measurements (point coordinates and size) are in absolute units.
    """
    def __init__(
            self,
            point: AbsolutePoint,
            size: AbsoluteSize,
            layer: int = 0,
    ):
        """
        Initialize an absolute position.

        Args:
            point: The top-left corner as an AbsolutePoint.
            size: The size as an AbsoluteSize.
            layer: The z-order layer (higher values appear on top). Default is 0.

        Raises:
            TypeError: If point or size are not absolute instances.
        """
        # Check arguments are absolute
        if not isinstance(point, AbsolutePoint) or not isinstance(size, AbsoluteSize):
            raise TypeError("x, y, and size must be AbsoluteMeasure and AbsoluteSize instances.")
        super().__init__(point, size, layer)

    @property
    def x(self) -> AbsoluteMeasure:
        """
        Gets the x-coordinate of the position.

        Returns:
            The x-coordinate as an AbsoluteMeasure.
        """
        return self._point.x

    @property
    def y(self) -> AbsoluteMeasure:
        """
        Gets the y-coordinate of the position.

        Returns:
            The y-coordinate as an AbsoluteMeasure.
        """
        return self._point.y

    @property
    def size(self) -> AbsoluteSize:
        """
        Gets the size of the positioned element.

        Returns:
            The size as an AbsoluteSize.
        """
        return self._size

    @property
    def width(self) -> AbsoluteMeasure:
        """
        Gets the width of the positioned element.

        Returns:
            The width as an AbsoluteMeasure.
        """
        return self._size.width

    @property
    def height(self) -> AbsoluteMeasure:
        """
        Gets the height of the positioned element.

        Returns:
            The height as an AbsoluteMeasure.
        """
        return self._size.height


    def start_corner(self) -> AbsolutePoint:
        """
        Gets the top-left corner point of the position.

        Returns:
            The top-left corner as an AbsolutePoint.
        """
        return self._point

    def to_box(self) -> tuple[int, int, int, int]:
        """
        Converts the position to a bounding box in pixels.

        Returns:
            A tuple (x1, y1, x2, y2) representing the box coordinates in pixels,
            where (x1, y1) is the top-left corner and (x2, y2) is the bottom-right corner.
        """
        return (
            self._point.x.to_px(),
            self._point.y.to_px(),
            self._point.x.to_px() + self._size.width.to_px(),
            self._point.y.to_px() + self._size.height.to_px(),
        )
