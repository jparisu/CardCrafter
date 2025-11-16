"""
TODO
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
    TODO
    """

    def __init__(
            self,
            hex: str
    ):
        """
        TODO
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
        TODO
        """
        hex_value = f"#{r:02x}{g:02x}{b:02x}"
        return cls(hex_value)

    @classmethod
    def from_hex(
            cls,
            hex: str
    ) -> "Color":
        """
        TODO
        """
        return cls(hex)

    @classmethod
    def from_name(
            cls,
            name: str
    ) -> "Color":
        """
        TODO
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
        TODO
        """
        return (
            int(self._hex[1:3], 16),
            int(self._hex[3:5], 16),
            int(self._hex[5:7], 16)
        )

    def to_hex(self) -> str:
        """
        TODO
        """
        return self._hex

    @staticmethod
    def define_color(
            name: str,
            hex: str
    ):
        """
        TODO
        """
        COLORS[name.lower()] = hex
