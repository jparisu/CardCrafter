"""
Module for handling shapes and border styles.

This module provides enumerations for shape types and line styles,
as well as a class for defining border styling.
"""

from enum import Enum

from CardCrafter.styling.color import Color


class Shape(Enum):
    """
    Enumeration of supported shape types.

    Attributes:
        RECTANGLE: A rectangular shape.
    """
    RECTANGLE = 'rectangle'


class LineStyle(Enum):
    """
    Enumeration of line styling options for borders.

    Attributes:
        SOLID: A solid continuous line.
        DASHED: A dashed line.
        DOTTED: A dotted line.
    """
    SOLID = 'solid'
    DASHED = 'dashed'
    DOTTED = 'dotted'


class BorderStyle:
    """
    Represents the styling for a border.

    Defines the visual appearance of borders including color, width, and line style.
    """

    def __init__(
            self,
            color: Color,
            width: int,
            line_style: LineStyle = LineStyle.SOLID
    ):
        """
        Initialize a border style.

        Args:
            color: The color of the border.
            width: The width of the border in pixels.
            line_style: The style of the line (default: solid).
        """
        self._color = color
        self._width = width
        self._line_style = line_style


    @property
    def color(self) -> Color:
        """
        Gets the border color.

        Returns:
            The border color.
        """
        return self._color

    @property
    def width(self) -> int:
        """
        Gets the border width.

        Returns:
            The border width in pixels.
        """
        return self._width

    @property
    def line_style(self) -> LineStyle:
        """
        Gets the line style of the border.

        Returns:
            The line style.
        """
        return self._line_style
