"""
TODO
"""

from __future__ import annotations

from CardCrafter.positioning.measure import Measure, AbsoluteMeasure


class Size:
    """
    Represents the size of an element with width and height.
    """

    def __init__(self, width: Measure, height: Measure):
        self._width = width
        self._height = height

    def absolute(self, reference: AbsoluteSize) -> AbsoluteSize:
        """
        Converts the size to absolute measurements based on reference dimensions.
        """
        abs_width = self._width.absolute(reference.width)
        abs_height = self._height.absolute(reference.height)
        return AbsoluteSize(abs_width, abs_height)


class AbsoluteSize(Size):
    """
    Represents the absolute size of an element with absolute width and height.
    """

    def __init__(self, width: AbsoluteMeasure, height: AbsoluteMeasure):
        # Check arguments are absolute
        if not isinstance(width, AbsoluteMeasure) or not isinstance(height, AbsoluteMeasure):
            raise TypeError("Width and height must be AbsoluteMeasure instances.")
        super().__init__(width, height)

    @property
    def width(self) -> AbsoluteMeasure:
        """
        Returns the width in millimeters.
        """
        return self._width

    @property
    def height(self) -> AbsoluteMeasure:
        """
        Returns the height in millimeters.
        """
        return self._height

    def to_tuple(self) -> tuple[int, int]:
        """
        Returns the size as a tuple of integers (width, height) in millimeters.
        """
        return (int(self.width.to_px()), int(self.height.to_px()))
