"""
TODO
"""

from abc import ABC, abstractmethod
from typing import TypeVar

from CardCrafter.positioning.position import Position
from CardCrafter.positioning.size import AbsoluteSize
from CardCrafter.styling.text import TextStyle
from CardCrafter.rendering.element import Element, TextElement, ImageElement

E = TypeVar('ElementType')
S = TypeVar('StyleType')

class Feature(ABC):

    def __init__(
            self,
            name: str,
            position: Position,
            description: str = "",
            ):
        self._name = name
        self._position = position
        self._description = description

        self._is_default_set: bool = False
        self._default_args: list | None = None
        self._default_kwargs: dict | None = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def position(self) -> Position:
        return self._position

    @property
    def description(self) -> str:
        return self._description

    @abstractmethod
    def generate_element(
            self,
            size: AbsoluteSize,
            value: S,
    ) -> E:
        pass


    def default(
            self,
            size: AbsoluteSize,
    ) -> E:
        """TODO"""
        if self._is_default_set:
            return self.generate_element(
                size=size,
                *self._default_args,
                **self._default_kwargs,
            )
        return None

    def set_default(self, *args, **kwargs) -> None:
        """TODO"""
        self._is_default_set = True
        self._default_args = args
        self._default_kwargs = kwargs



class TextFeature(Feature):
    def __init__(
            self,
            name: str,
            position: Position,
            description: str = "",
            style: TextStyle = TextStyle(),
            ):
        super().__init__(name, position, description)
        self._style = style

    @property
    def style(self) -> TextStyle:
        return self._style

    def generate_element(
            self,
            size: AbsoluteSize,
            value: str,
    ) -> TextElement:

        # Check value type
        if not isinstance(value, str):
            raise TypeError(f"Expected value of type str, got {type(value)}")

        return TextElement(
            position=self.position.to_absolute(size),
            text=value,
            style=self.style,
        )


class ImageFeature(Feature):
    def __init__(
            self,
            name: str,
            position: Position,
            description: str = "",
            ):
        super().__init__(name, position, description)

    def generate_element(
            self,
            size: AbsoluteSize,
            value: str,
    ) -> ImageElement:

        # Check value type
        if not isinstance(value, str):
            raise TypeError(f"Expected value of type str, got {type(value)}")

        return ImageElement(
            position=self.position.to_absolute(size),
            image_path=value,
        )
