"""
Value objects and enums for CardCrafter.

This module contains basic value objects like BBox and Resolution,
as well as enums for Anchor, Align, FitMode, and Unit.
"""

from enum import Enum
from typing import NamedTuple


class BBox(NamedTuple):
    """
    Bounding box with position and size.

    Attributes:
        x: X-coordinate of the bounding box
        y: Y-coordinate of the bounding box
        w: Width of the bounding box
        h: Height of the bounding box
    """

    x: int
    y: int
    w: int
    h: int


class Anchor(Enum):
    """
    Anchor positions for aligning features within their bounding boxes.

    Defines where a feature should be anchored relative to its container.
    """

    TopLeft = "top_left"
    Top = "top"
    TopRight = "top_right"
    Left = "left"
    Center = "center"
    Right = "right"
    BottomLeft = "bottom_left"
    Bottom = "bottom"
    BottomRight = "bottom_right"
    Bleed = "bleed"


class Align(Enum):
    """
    Text alignment options.

    Defines how text should be aligned within its bounding box.
    """

    Left = "left"
    Center = "center"
    Right = "right"


class FitMode(Enum):
    """
    Image fitting modes.

    Defines how an image should be fitted within its bounding box.
    """

    Cover = "cover"
    Contain = "contain"
    ScaleDown = "scale_down"


class Unit(Enum):
    """
    Measurement units.

    Defines the units used for measurements in the card design.
    """

    Px = "px"
    Pt = "pt"
    Mm = "mm"


class Resolution(NamedTuple):
    """
    Image resolution with width and height.

    Attributes:
        width: Width in pixels
        height: Height in pixels
    """

    width: int
    height: int

    def aspect(self) -> str:
        """
        Calculate the aspect ratio as a string.

        Returns:
            Aspect ratio in the format "width:height" (simplified)
        """
        from math import gcd

        divisor = gcd(self.width, self.height)
        return f"{self.width // divisor}:{self.height // divisor}"
