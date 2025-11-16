"""
Module for handling colors.

This module provides a Color class that supports multiple color representations
(RGB, hexadecimal) and a set of predefined named colors.
"""

COLORS = {
    "red": "#ff0000",
    "green": "#00ff00",
    "blue": "#0000ff",
    "black": "#000000",
    "white": "#ffffff",
    "yellow": "#ffff00",
    "cyan": "#00ffff",
    "magenta": "#ff00ff",
}

class Color:
    """
    Represents a color with support for multiple representations.
    
    Colors can be created from RGB values, hexadecimal strings, or predefined names.
    """

    def __init__(
            self,
            hex: str
    ):
        """
        Initialize a color from a hexadecimal string.
        
        Args:
            hex: The color in hexadecimal format (e.g., "#ff0000" for red).
        """
        self._hex = hex

    ####################################################
    # Factory Methods

    @classmethod
    def from_rgb(
            cls,
            r: int,
            g: int,
            b: int
    ) -> "Color":
        """
        Creates a Color from RGB values.
        
        Args:
            r: Red component (0-255).
            g: Green component (0-255).
            b: Blue component (0-255).
        
        Returns:
            A new Color instance.
        """
        hex_value = f"#{r:02x}{g:02x}{b:02x}"
        return cls(hex_value)

    @classmethod
    def from_hex(
            cls,
            hex: str
    ) -> "Color":
        """
        Creates a Color from a hexadecimal string.
        
        Args:
            hex: The color in hexadecimal format (e.g., "#ff0000").
        
        Returns:
            A new Color instance.
        """
        return cls(hex)

    @classmethod
    def from_name(
            cls,
            name: str
    ) -> "Color":
        """
        Creates a Color from a predefined color name.
        
        Args:
            name: The name of a predefined color (case-insensitive).
        
        Returns:
            A new Color instance.
        
        Raises:
            ValueError: If the color name is not defined.
        """
        # Check if the name is in the predefined colors
        if name.lower() in COLORS:
            hex_value = COLORS[name.lower()]
            return cls(hex_value)

        raise ValueError(f"Color name '{name}' is not defined.")


    ####################################################
    # Conversion Methods

    def to_rgb(self) -> tuple[int, int, int]:
        """
        Converts the color to RGB format.
        
        Returns:
            A tuple (r, g, b) with values from 0 to 255.
        """
        return (
            int(self._hex[1:3], 16),
            int(self._hex[3:5], 16),
            int(self._hex[5:7], 16)
        )

    def to_hex(self) -> str:
        """
        Gets the color in hexadecimal format.
        
        Returns:
            The color as a hexadecimal string (e.g., "#ff0000").
        """
        return self._hex

    @staticmethod
    def define_color(
            name: str,
            hex: str
    ):
        """
        Defines a new named color or updates an existing one.
        
        Args:
            name: The name for the color (case-insensitive).
            hex: The color in hexadecimal format.
        """
        COLORS[name.lower()] = hex
