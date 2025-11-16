"""
TODO
"""

from PIL import Image, ImageDraw, ImageFont, ImageColor
import logging
from abc import ABC, abstractmethod

from CardCrafter.positioning.size import AbsoluteSize
from CardCrafter.rendering.element import TextElement, ImageElement
from CardCrafter.styling.text import TextAlignment
from CardCrafter.styling.image import ImageFormatting
from CardCrafter.styling.color import Color
from CardCrafter.rendering.canvas import Canvas

logger = logging.getLogger(__name__)


def _alignment_to_anchor(alignment: TextAlignment) -> str:
    if alignment == TextAlignment.LEFT:
        return "lt"
    elif alignment == TextAlignment.CENTER:
        return "mt"
    elif alignment == TextAlignment.RIGHT:
        return "rt"


def _color_to_pil(color: Color) -> str:
    return color.to_hex()



class Canvas_PIL(Canvas):

    def __init__(
            self,
            size: AbsoluteSize,
    ):
        self._size = size
        self._image = Image.new("RGBA", size.to_tuple())
        self._draw = ImageDraw.Draw(self._image)


    def save(
        self,
        filepath: str,
    ) -> None:
        self._image.save(filepath)

    def show(
        self,
    ) -> None:
        self._image.show()


    def add_text(
        self,
        element: TextElement,
    ) -> None:

        font = element.style.font_name

        # Draw the text on the image
        try:
            font = ImageFont.truetype(element.style.font_name, element.style.font_size)
        except OSError:
            logger.warning(f"{element.style.font_name} not found. Falling back to default font.")
            font = ImageFont.load_default()

        position = element.position.start_corner().to_tuple()
        anchor = _alignment_to_anchor(element.style.alignment)
        color = _color_to_pil(element.style.font_color)

        self._draw.text(
            position,
            element.text,
            font=font,
            fill=color,
            anchor=anchor,
        )


    def add_image(
        self,
        element: ImageElement
    ) -> None:

        # Open the image
        img = Image.open(element.image_path).convert("RGBA")

        # Resize or crop
        if element.style.formatting == ImageFormatting.RESCALE:
            img = img.resize(element.position.size.to_tuple())
        else:
            img = img.crop((0, 0, element.position.width, element.position.height))

        self._image.paste(img, element.position.to_box())
