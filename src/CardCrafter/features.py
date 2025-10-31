"""
Feature classes for CardCrafter.

This module contains feature definitions for text and image elements.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

from CardCrafter.styles import ImageStyle, TextStyle
from CardCrafter.value_objects import Anchor, BBox

if TYPE_CHECKING:
    from CardCrafter.render import RenderContext


class Feature(ABC):
    """
    Abstract base class for card features.

    A feature represents a visual element on a card (e.g., text, image).

    Attributes:
        id: Unique identifier for the feature
        name: Human-readable name for the feature
        layer: Layer order (features with lower numbers are drawn first)
        anchor: Anchor position for alignment
        bbox: Bounding box defining position and size
        enabled: Whether the feature is enabled and should be rendered
    """

    def __init__(
        self,
        id: str,
        name: str,
        layer: int = 0,
        anchor: Anchor = Anchor.TopLeft,
        bbox: Optional[BBox] = None,
        enabled: bool = True,
    ):
        """
        Initialize a Feature.

        Args:
            id: Unique identifier for the feature
            name: Human-readable name for the feature
            layer: Layer order (default: 0)
            anchor: Anchor position (default: TopLeft)
            bbox: Bounding box (default: None, will use full canvas)
            enabled: Whether the feature is enabled (default: True)
        """
        self.id = id
        self.name = name
        self.layer = layer
        self.anchor = anchor
        self.bbox = bbox if bbox is not None else BBox(0, 0, 0, 0)
        self.enabled = enabled

    def validate(self) -> None:
        """
        Validate the feature configuration.

        Raises:
            ValueError: If the feature configuration is invalid
        """
        if not self.id:
            raise ValueError("Feature id cannot be empty")
        if not self.name:
            raise ValueError("Feature name cannot be empty")
        if self.bbox.w < 0 or self.bbox.h < 0:
            raise ValueError(f"Bounding box dimensions must be non-negative: {self.bbox}")

    def layout(self, canvasW: int, canvasH: int) -> BBox:
        """
        Calculate the actual bounding box for this feature given canvas dimensions.

        This method adjusts the feature's bbox based on the anchor position
        and canvas dimensions.

        Args:
            canvasW: Canvas width in pixels
            canvasH: Canvas height in pixels

        Returns:
            The calculated bounding box
        """
        # If bbox width/height is 0, use the full canvas
        w = self.bbox.w if self.bbox.w > 0 else canvasW
        h = self.bbox.h if self.bbox.h > 0 else canvasH

        # Calculate position based on anchor
        if self.anchor == Anchor.TopLeft:
            x, y = self.bbox.x, self.bbox.y
        elif self.anchor == Anchor.Top:
            x, y = (canvasW - w) // 2 + self.bbox.x, self.bbox.y
        elif self.anchor == Anchor.TopRight:
            x, y = canvasW - w + self.bbox.x, self.bbox.y
        elif self.anchor == Anchor.Left:
            x, y = self.bbox.x, (canvasH - h) // 2 + self.bbox.y
        elif self.anchor == Anchor.Center:
            x, y = (canvasW - w) // 2 + self.bbox.x, (canvasH - h) // 2 + self.bbox.y
        elif self.anchor == Anchor.Right:
            x, y = canvasW - w + self.bbox.x, (canvasH - h) // 2 + self.bbox.y
        elif self.anchor == Anchor.BottomLeft:
            x, y = self.bbox.x, canvasH - h + self.bbox.y
        elif self.anchor == Anchor.Bottom:
            x, y = (canvasW - w) // 2 + self.bbox.x, canvasH - h + self.bbox.y
        elif self.anchor == Anchor.BottomRight:
            x, y = canvasW - w + self.bbox.x, canvasH - h + self.bbox.y
        elif self.anchor == Anchor.Bleed:
            # Bleed extends to full canvas
            x, y, w, h = 0, 0, canvasW, canvasH
        else:
            x, y = self.bbox.x, self.bbox.y

        return BBox(x, y, w, h)

    @abstractmethod
    def render(self, ctx: "RenderContext") -> None:
        """
        Render the feature to the render context.

        Args:
            ctx: The render context to draw on

        Raises:
            NotImplementedError: This method must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement render()")


class TextFeature(Feature):
    """
    Text feature for displaying text on a card.

    Attributes:
        textKey: Key to fetch text from CardData
        fallbackText: Fallback text if key is not found
        style: TextStyle configuration
    """

    def __init__(
        self,
        id: str,
        name: str,
        textKey: str,
        fallbackText: str = "",
        style: Optional[TextStyle] = None,
        layer: int = 0,
        anchor: Anchor = Anchor.TopLeft,
        bbox: Optional[BBox] = None,
        enabled: bool = True,
    ):
        """
        Initialize a TextFeature.

        Args:
            id: Unique identifier for the feature
            name: Human-readable name for the feature
            textKey: Key to fetch text from CardData
            fallbackText: Fallback text if key is not found (default: empty string)
            style: TextStyle configuration (default: None, will use default TextStyle)
            layer: Layer order (default: 0)
            anchor: Anchor position (default: TopLeft)
            bbox: Bounding box (default: None)
            enabled: Whether the feature is enabled (default: True)
        """
        super().__init__(id, name, layer, anchor, bbox, enabled)
        self.textKey = textKey
        self.fallbackText = fallbackText
        self.style = style if style is not None else TextStyle()

    def render(self, ctx: "RenderContext") -> None:
        """
        Render the text feature to the render context.

        Args:
            ctx: The render context to draw on
        """
        # Get the actual bbox for this canvas
        actual_bbox = self.layout(ctx.canvasW, ctx.canvasH)

        # Get the text from the context's data
        text = ctx.get_text_value(self.textKey, self.fallbackText)

        # Draw the text using the render context
        ctx.drawText(text, actual_bbox, self.style)


class ImageFeature(Feature):
    """
    Image feature for displaying images on a card.

    Attributes:
        imageKey: Key to fetch image path/URL from CardData
        fallbackImage: Fallback image path if key is not found
        style: ImageStyle configuration
    """

    def __init__(
        self,
        id: str,
        name: str,
        imageKey: str,
        fallbackImage: str = "",
        style: Optional[ImageStyle] = None,
        layer: int = 0,
        anchor: Anchor = Anchor.TopLeft,
        bbox: Optional[BBox] = None,
        enabled: bool = True,
    ):
        """
        Initialize an ImageFeature.

        Args:
            id: Unique identifier for the feature
            name: Human-readable name for the feature
            imageKey: Key to fetch image path/URL from CardData
            fallbackImage: Fallback image path if key is not found (default: empty string)
            style: ImageStyle configuration (default: None, will use default ImageStyle)
            layer: Layer order (default: 0)
            anchor: Anchor position (default: TopLeft)
            bbox: Bounding box (default: None)
            enabled: Whether the feature is enabled (default: True)
        """
        super().__init__(id, name, layer, anchor, bbox, enabled)
        self.imageKey = imageKey
        self.fallbackImage = fallbackImage
        self.style = style if style is not None else ImageStyle()

    def render(self, ctx: "RenderContext") -> None:
        """
        Render the image feature to the render context.

        Args:
            ctx: The render context to draw on
        """
        # Get the actual bbox for this canvas
        actual_bbox = self.layout(ctx.canvasW, ctx.canvasH)

        # Get the image path from the context's data
        image_path = ctx.get_image_value(self.imageKey, self.fallbackImage)

        # Load the image from the resource cache
        img = ctx.resources.getImage(image_path)

        # Draw the image using the render context
        ctx.drawImage(img, actual_bbox.x, actual_bbox.y, actual_bbox.w, actual_bbox.h, self.style.radius)
