"""
Module for defining card features.

This module provides abstract and concrete feature classes that define
what content can appear on cards (text, images, etc.).
"""

from abc import ABC, abstractmethod
from typing import TypeVar

from CardCrafter.positioning.position import Position
from CardCrafter.positioning.size import AbsoluteSize
from CardCrafter.styling.text import TextStyle
from CardCrafter.rendering.element import Element, TextElement, ImageElement
from CardCrafter.styling.image import ImageStyle

E = TypeVar('ElementType')
S = TypeVar('StyleType')

class Feature(ABC):
    """
    Abstract base class for card features.
    
    Features define placeholders for content that can appear on cards,
    such as text fields or image slots.
    """

    def __init__(
            self,
            name: str,
            position: Position,
            description: str = "",
            ):
        """
        Initialize a feature.
        
        Args:
            name: The unique name of this feature.
            position: The position where this feature should appear.
            description: An optional description of the feature.
        """
        self._name = name
        self._position = position
        self._description = description

        self._is_default_set: bool = False
        self._default_args: list | None = None
        self._default_kwargs: dict | None = None

    @property
    def name(self) -> str:
        """
        Gets the feature name.
        
        Returns:
            The feature name as a string.
        """
        return self._name

    @property
    def position(self) -> Position:
        """
        Gets the feature position.
        
        Returns:
            The position where this feature appears.
        """
        return self._position

    @property
    def description(self) -> str:
        """
        Gets the feature description.
        
        Returns:
            The feature description as a string.
        """
        return self._description

    @abstractmethod
    def generate_element(
            self,
            size: AbsoluteSize,
            value: S,
    ) -> E:
        """
        Generates a renderable element from a value.
        
        Args:
            size: The absolute size reference for positioning.
            value: The value to render (type depends on feature type).
        
        Returns:
            A renderable element.
        """
        pass


    def default(
            self,
            size: AbsoluteSize,
    ) -> E:
        """
        Generates the default element for this feature.
        
        Args:
            size: The absolute size reference for positioning.
        
        Returns:
            A renderable element if a default is set, None otherwise.
        """
        if self._is_default_set:
            return self.generate_element(
                size=size,
                *self._default_args,
                **self._default_kwargs,
            )
        return None

    def set_default(self, *args, **kwargs) -> None:
        """
        Sets the default value for this feature.
        
        Args:
            *args: Positional arguments for generate_element.
            **kwargs: Keyword arguments for generate_element.
        """
        self._is_default_set = True
        self._default_args = args
        self._default_kwargs = kwargs



class TextFeature(Feature):
    """
    A feature for displaying text on cards.
    """
    def __init__(
            self,
            name: str,
            position: Position,
            description: str = "",
            style: TextStyle = TextStyle(),
            ):
        """
        Initialize a text feature.
        
        Args:
            name: The unique name of this feature.
            position: The position where text should appear.
            description: An optional description of the feature.
            style: The text styling to apply (default: default TextStyle).
        """
        super().__init__(name, position, description)
        self._style = style

    @property
    def style(self) -> TextStyle:
        """
        Gets the text style.
        
        Returns:
            The text styling configuration.
        """
        return self._style

    def generate_element(
            self,
            size: AbsoluteSize,
            value: str,
    ) -> TextElement:
        """
        Generates a text element from a string value.
        
        Args:
            size: The absolute size reference for positioning.
            value: The text string to display.
        
        Returns:
            A TextElement ready to be rendered.
        
        Raises:
            TypeError: If value is not a string.
        """

        # Check value type
        if not isinstance(value, str):
            raise TypeError(f"Expected value of type str, got {type(value)}")

        return TextElement(
            position=self.position.absolute(size),
            text=value,
            style=self.style,
        )


class ImageFeature(Feature):
    """
    A feature for displaying images on cards.
    """
    def __init__(
            self,
            name: str,
            position: Position,
            description: str = "",
            style: ImageStyle = ImageStyle(),
            ):
        """
        Initialize an image feature.
        
        Args:
            name: The unique name of this feature.
            position: The position where the image should appear.
            description: An optional description of the feature.
            style: The image styling to apply (default: default ImageStyle).
        """
        super().__init__(name, position, description)
        self._style = style

    @property
    def style(self) -> ImageStyle:
        """
        Gets the image style.
        
        Returns:
            The image styling configuration.
        """
        return self._style

    def generate_element(
            self,
            size: AbsoluteSize,
            value: str,
    ) -> ImageElement:
        """
        Generates an image element from an image path.
        
        Args:
            size: The absolute size reference for positioning.
            value: The path to the image file.
        
        Returns:
            An ImageElement ready to be rendered.
        
        Raises:
            TypeError: If value is not a string.
        """

        # Check value type
        if not isinstance(value, str):
            raise TypeError(f"Expected value of type str, got {type(value)}")

        return ImageElement(
            position=self.position.absolute(size),
            image_path=value,
            style=self.style,
        )
