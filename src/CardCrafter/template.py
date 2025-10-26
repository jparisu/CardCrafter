"""
Template class for CardCrafter.

This module contains the Template class which defines a card template.
"""

from typing import Optional

from CardCrafter.features import Feature
from CardCrafter.value_objects import Resolution


class Template:
    """
    Card template definition.

    A template defines the structure and layout of a card, including
    its resolution, features, and print settings.

    Attributes:
        name: Template name
        resolution: Output resolution (width x height in pixels)
        dpi: Dots per inch for print quality
        safeMargin: Safe margin in pixels (area that should contain important content)
        bleed: Bleed area in pixels (extends beyond the card edge for printing)
        features: List of features (text, images, etc.) on the card
    """

    def __init__(
        self,
        name: str,
        resolution: Resolution,
        dpi: int = 300,
        safeMargin: int = 0,
        bleed: int = 0,
        features: Optional[list[Feature]] = None,
    ):
        """
        Initialize a Template.

        Args:
            name: Template name
            resolution: Output resolution
            dpi: Dots per inch (default: 300)
            safeMargin: Safe margin in pixels (default: 0)
            bleed: Bleed area in pixels (default: 0)
            features: List of features (default: None, will create empty list)

        Raises:
            ValueError: If dpi, safeMargin, or bleed are negative
        """
        if dpi <= 0:
            raise ValueError(f"dpi must be positive, got {dpi}")
        if safeMargin < 0:
            raise ValueError(f"safeMargin must be non-negative, got {safeMargin}")
        if bleed < 0:
            raise ValueError(f"bleed must be non-negative, got {bleed}")

        self.name = name
        self.resolution = resolution
        self.dpi = dpi
        self.safeMargin = safeMargin
        self.bleed = bleed
        self.features = features if features is not None else []

    def getFeaturesByLayer(self) -> list[Feature]:
        """
        Get features sorted by layer order.

        Features with lower layer numbers are drawn first.

        Returns:
            List of features sorted by layer (ascending)
        """
        return sorted(self.features, key=lambda f: f.layer)

    def validate(self) -> None:
        """
        Validate the template configuration.

        Validates the template and all its features.

        Raises:
            ValueError: If the template or any of its features is invalid
        """
        if not self.name:
            raise ValueError("Template name cannot be empty")
        if self.resolution.width <= 0 or self.resolution.height <= 0:
            raise ValueError(f"Template resolution must be positive: {self.resolution}")

        # Validate all features
        for i, feature in enumerate(self.features):
            try:
                feature.validate()
            except ValueError as e:
                # Use feature name if accessible, otherwise use index
                feature_name = getattr(feature, "name", f"at index {i}")
                raise ValueError(f"Invalid feature '{feature_name}': {e}") from e
