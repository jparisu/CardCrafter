"""
TODO
"""

from abc import ABC, abstractmethod
import logging

from CardCrafter.positioning.position import AbsolutePosition
from CardCrafter.styling.text import TextStyle
from CardCrafter.styling.image import ImageStyle

logger = logging.getLogger(__name__)

class Element(ABC):

    def __init__(
            self,
            position: AbsolutePosition,
            ):
        self._position = position

    @property
    def position(self) -> AbsolutePosition:
        return self._position

    @property
    def layer(self) -> int:
        return self._position.layer

    @abstractmethod
    def render(
            self,
            canvas: 'Canvas',
    ) -> None:
        pass


class TextElement(Element):

    def __init__(
            self,
            position: AbsolutePosition,
            text: str,
            style: TextStyle,
    ):
        super().__init__(position)
        self._text = text
        self._style = style

    @property
    def style(self) -> TextStyle:
        return self._style

    @property
    def text(self) -> str:
        return self._text


    def render(
            self,
            canvas: 'Canvas',
    ) -> None:
        """TODO"""
        logger.debug(f"Rendering TextElement at position {self.position} with text '{self._text}'")
        canvas.add_text(self)


class ImageElement(Element):

    def __init__(
            self,
            position: AbsolutePosition,
            image_path: str,
            style: ImageStyle,
    ):
        super().__init__(position)
        self._image_path = image_path
        self._style = style

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def style(self) -> ImageStyle:
        return self._style

    def render(
            self,
            canvas: 'Canvas',
    ) -> None:
        """TODO"""
        logger.debug(f"Rendering ImageElement at position {self.position} with image '{self._image_path}'")
        canvas.add_image(self)
