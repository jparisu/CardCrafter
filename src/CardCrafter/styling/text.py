"""
Module for handling text styling.

This module provides enumerations and classes for configuring text appearance,
including alignment, formatting, font properties, and colors.
"""

from dataclasses import dataclass
from enum import Enum

from CardCrafter.styling.color import Color


class TextAlignment(Enum):
    """
    Enumeration of text alignment options.

    Attributes:
        LEFT: Align text to the left.
        CENTER: Center the text.
        RIGHT: Align text to the right.
    """
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'

class TextFormatting(Enum):
    """
    Enumeration of text formatting options.

    Attributes:
        PLAIN: Plain text without any formatting.
        MARKDOWN: Text formatted using Markdown syntax.
    """
    PLAIN = 'plain'
    MARKDOWN = 'markdown'


@dataclass
class TextStyle:
    """
    Represents the styling options for a text element.

    Attributes:
        alignment: The horizontal alignment of the text (default: LEFT).
        formatting: The text formatting type (default: PLAIN).
        font_name: The font file name to use (default: "arial.ttf").
        font_size: The font size in points (default: 12).
        font_color: The color of the text (default: black).
    """

    alignment: TextAlignment = TextAlignment.LEFT
    formatting: TextFormatting = TextFormatting.PLAIN
    font_name: str = "arial.ttf"
    font_size: int = 12
    font_color: Color = Color("#000000")
