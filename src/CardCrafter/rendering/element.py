"""
Module for defining renderable elements.

This module provides abstract and concrete element classes that can be
rendered onto a canvas, including text and image elements.
"""

from abc import ABC, abstractmethod
import logging

from CardCrafter.positioning.position import AbsolutePosition
from CardCrafter.styling.text import TextStyle
from CardCrafter.styling.image import ImageStyle

logger = logging.getLogger(__name__)

class Element(ABC):
    """
    Abstract base class for renderable elements.
    
    Elements are objects that can be rendered onto a canvas at a specific position.
    """

    def __init__(
            self,
            position: AbsolutePosition,
            ):
        """
        Initialize an element.
        
        Args:
            position: The absolute position where the element should be rendered.
        """
        self._position = position

    @property
    def position(self) -> AbsolutePosition:
        """
        Gets the position of the element.
        
        Returns:
            The absolute position of this element.
        """
        return self._position

    @property
    def layer(self) -> int:
        """
        Gets the layer (z-order) of the element.
        
        Returns:
            The layer as an integer.
        """
        return self._position.layer

    @abstractmethod
    def render(
            self,
            canvas: 'Canvas',
    ) -> None:
        """
        Renders this element onto a canvas.
        
        Args:
            canvas: The canvas to render onto.
        """
        pass


class TextElement(Element):
    """
    Represents a text element that can be rendered.
    
    Combines text content with styling and positioning information.
    """

    def __init__(
            self,
            position: AbsolutePosition,
            text: str,
            style: TextStyle,
    ):
        """
        Initialize a text element.
        
        Args:
            position: The absolute position for the text.
            text: The text content to render.
            style: The styling to apply to the text.
        """
        super().__init__(position)
        self._text = text
        self._style = style

    @property
    def style(self) -> TextStyle:
        """
        Gets the text style.
        
        Returns:
            The text styling configuration.
        """
        return self._style

    @property
    def text(self) -> str:
        """
        Gets the text content.
        
        Returns:
            The text string to render.
        """
        return self._text


    def render(
            self,
            canvas: 'Canvas',
    ) -> None:
        """
        Renders this text element onto the canvas.
        
        Args:
            canvas: The canvas to render onto.
        """
        logger.debug(f"Rendering TextElement at position {self.position} with text '{self._text}'")
        canvas.add_text(self)


class ImageElement(Element):
    """
    Represents an image element that can be rendered.
    
    Combines an image path with styling and positioning information.
    """

    def __init__(
            self,
            position: AbsolutePosition,
            image_path: str,
            style: ImageStyle,
    ):
        """
        Initialize an image element.
        
        Args:
            position: The absolute position for the image.
            image_path: The file path to the image to render.
            style: The styling to apply to the image.
        """
        super().__init__(position)
        self._image_path = image_path
        self._style = style

    @property
    def image_path(self) -> str:
        """
        Gets the image file path.
        
        Returns:
            The path to the image file.
        """
        return self._image_path

    @property
    def style(self) -> ImageStyle:
        """
        Gets the image style.
        
        Returns:
            The image styling configuration.
        """
        return self._style

    def render(
            self,
            canvas: 'Canvas',
    ) -> None:
        """
        Renders this image element onto the canvas.
        
        Args:
            canvas: The canvas to render onto.
        """
        logger.debug(f"Rendering ImageElement at position {self.position} with image '{self._image_path}'")
        canvas.add_image(self)
