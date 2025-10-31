"""
Style classes for CardCrafter features.

This module contains style definitions for text and image features.
"""

from typing import Optional

from CardCrafter.value_objects import Align, FitMode


class Style:
    """
    Base class for feature styles.

    Attributes:
        color: Color as a string (e.g., "#FFFFFF", "rgb(255,255,255)")
        opacity: Opacity value between 0.0 (transparent) and 1.0 (opaque)
    """

    def __init__(self, color: str = "#000000", opacity: float = 1.0):
        """
        Initialize a Style.

        Args:
            color: Color as a string (default: black)
            opacity: Opacity value (default: 1.0)

        Raises:
            ValueError: If opacity is not between 0.0 and 1.0
        """
        if not 0.0 <= opacity <= 1.0:
            raise ValueError(f"Opacity must be between 0.0 and 1.0, got {opacity}")
        self.color = color
        self.opacity = opacity


class TextStyle(Style):
    """
    Style definition for text features.

    Attributes:
        color: Text color
        opacity: Text opacity
        fontPath: Path to the font file
        fontSize: Font size in points
        lineHeight: Line height multiplier (e.g., 1.5 for 1.5x line spacing)
        align: Text alignment (Left, Center, Right)
        wrap: Whether to wrap text within the bounding box
        ellipsis: Whether to add ellipsis (...) when text is truncated
        strokeColor: Stroke (outline) color for text
        strokeWidth: Stroke width in pixels
        letterSpacing: Letter spacing in pixels
    """

    def __init__(
        self,
        color: str = "#000000",
        opacity: float = 1.0,
        fontPath: str = "",
        fontSize: int = 12,
        lineHeight: float = 1.0,
        align: Align = Align.Left,
        wrap: bool = True,
        ellipsis: bool = False,
        strokeColor: Optional[str] = None,
        strokeWidth: int = 0,
        letterSpacing: float = 0.0,
    ):
        """
        Initialize a TextStyle.

        Args:
            color: Text color (default: black)
            opacity: Text opacity (default: 1.0)
            fontPath: Path to the font file (default: empty string)
            fontSize: Font size in points (default: 12)
            lineHeight: Line height multiplier (default: 1.0)
            align: Text alignment (default: Left)
            wrap: Whether to wrap text (default: True)
            ellipsis: Whether to add ellipsis for truncated text (default: False)
            strokeColor: Stroke color (default: None)
            strokeWidth: Stroke width (default: 0)
            letterSpacing: Letter spacing (default: 0.0)

        Raises:
            ValueError: If fontSize is not positive or lineHeight is not positive
        """
        super().__init__(color, opacity)
        if fontSize <= 0:
            raise ValueError(f"fontSize must be positive, got {fontSize}")
        if lineHeight <= 0:
            raise ValueError(f"lineHeight must be positive, got {lineHeight}")
        if strokeWidth < 0:
            raise ValueError(f"strokeWidth must be non-negative, got {strokeWidth}")

        self.fontPath = fontPath
        self.fontSize = fontSize
        self.lineHeight = lineHeight
        self.align = align
        self.wrap = wrap
        self.ellipsis = ellipsis
        self.strokeColor = strokeColor
        self.strokeWidth = strokeWidth
        self.letterSpacing = letterSpacing


class ImageStyle(Style):
    """
    Style definition for image features.

    Attributes:
        color: Tint color (for backwards compatibility, same as tint)
        opacity: Image opacity
        fit: How the image should fit in the bounding box
        radius: Corner radius in pixels for rounded corners
        tint: Tint color to apply to the image
        contrast: Contrast adjustment (-1.0 to 1.0, 0 is no change)
        brightness: Brightness adjustment (-1.0 to 1.0, 0 is no change)
    """

    def __init__(
        self,
        color: str = "#FFFFFF",
        opacity: float = 1.0,
        fit: FitMode = FitMode.Cover,
        radius: int = 0,
        tint: Optional[str] = None,
        contrast: float = 0.0,
        brightness: float = 0.0,
    ):
        """
        Initialize an ImageStyle.

        Args:
            color: Base color (default: white)
            opacity: Image opacity (default: 1.0)
            fit: Fit mode (default: Cover)
            radius: Corner radius (default: 0)
            tint: Tint color (default: None)
            contrast: Contrast adjustment (default: 0.0)
            brightness: Brightness adjustment (default: 0.0)

        Raises:
            ValueError: If radius is negative or contrast/brightness out of range
        """
        super().__init__(color, opacity)
        if radius < 0:
            raise ValueError(f"radius must be non-negative, got {radius}")
        if not -1.0 <= contrast <= 1.0:
            raise ValueError(f"contrast must be between -1.0 and 1.0, got {contrast}")
        if not -1.0 <= brightness <= 1.0:
            raise ValueError(f"brightness must be between -1.0 and 1.0, got {brightness}")

        self.fit = fit
        self.radius = radius
        self.tint = tint
        self.contrast = contrast
        self.brightness = brightness
