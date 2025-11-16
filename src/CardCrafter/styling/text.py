"""
TODO
"""

from enum import Enum
from dataclasses import dataclass

from CardCrafter.styling.color import Color

class TextAlignment(Enum):
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'

class TextFormatting(Enum):
    PLAIN = 'plain'
    MARKDOWN = 'markdown'


@dataclass
class TextStyle:

    alignment: TextAlignment = TextAlignment.LEFT
    formatting: TextFormatting = TextFormatting.PLAIN
    font_name: str = "arial.ttf"
    font_size: int = 12
    font_color: Color = Color("#000000")
