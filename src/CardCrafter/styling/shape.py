"""
TODO
"""

from enum import Enum

from CardCrafter.styling.color import Color

class Shape(Enum):
    RECTANGLE = 'rectangle'


class LineStyle(Enum):
    SOLID = 'solid'
    DASHED = 'dashed'
    DOTTED = 'dotted'


class BorderStyle:

    def __init__(
            self,
            color: Color,
            width: int,
            line_style: LineStyle = LineStyle.SOLID
    ):
        """
        TODO
        """
        self._color = color
        self._width = width
        self._line_style = line_style


    @property
    def color(self) -> Color:
        """
        TODO
        """
        return self._color

    @property
    def width(self) -> int:
        """
        TODO
        """
        return self._width

    @property
    def line_style(self) -> LineStyle:
        """
        TODO
        """
        return self._line_style
