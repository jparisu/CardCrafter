"""
TODO
"""

from PIL import Image, ImageDraw, ImageFont, ImageColor
import logging
from abc import ABC, abstractmethod

from CardCrafter.rendering.element import TextElement, ImageElement

logger = logging.getLogger(__name__)

class Canvas(ABC):

    @abstractmethod
    def add_text(
        self,
        element: TextElement,
    ) -> None:
        pass


    @abstractmethod
    def add_image(
        self,
        element: ImageElement
    ) -> None:
        pass


    @abstractmethod
    def save(
        self,
        filepath: str,
    ) -> None:
        pass
