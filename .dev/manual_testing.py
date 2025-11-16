import logging
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Silence traces from other modules except my library
logging.getLogger(__name__).addHandler(logging.NullHandler())
# Activate debugging
logging.basicConfig(
    level=logging.DEBUG,
)

################################################################################################
# Try printing a card

# Printing a card

from CardCrafter.carding.card import Card
from CardCrafter.positioning.position import AbsolutePosition, Position
from CardCrafter.positioning.point import Point
from CardCrafter.positioning.measure import AbsoluteMeasure, RelativeMeasure
from CardCrafter.positioning.size import Size, AbsoluteSize
from CardCrafter.rendering.pil import Canvas_PIL
from CardCrafter.rendering.element import TextElement, ImageElement
from CardCrafter.styling.text import TextStyle, TextAlignment
from CardCrafter.styling.image import ImageStyle, ImageFormatting
from CardCrafter.styling.color import Color

size = AbsoluteSize(width=AbsoluteMeasure.from_px(400), height=AbsoluteMeasure.from_px(600))

position = Position(layer=1, point=Point(x=RelativeMeasure(0.1), y=RelativeMeasure(0.1)), size=Size(width=RelativeMeasure(0.8), height=RelativeMeasure(0.1)))
title = TextElement(
    position=position.absolute(size),
    text="Test Card",
    style=TextStyle(
        font_name="arial.ttf",
        font_size=24,
        font_color=Color.from_name("black"),
        alignment=TextAlignment.CENTER,
    )
)

position = Position(layer=1, point=Point(x=RelativeMeasure(0.1), y=RelativeMeasure(0.3)), size=Size(width=RelativeMeasure(0.8), height=RelativeMeasure(0.1)))
subtitle = TextElement(
    position=position.absolute(size),
    text="This is a subtitle",
    style=TextStyle(
        font_name="arial.ttf",
        font_size=18,
        font_color=Color.from_hex("#DDDDDD"),
        alignment=TextAlignment.LEFT,
    )
)

position = Position(layer=2, point=Point(x=RelativeMeasure(0.2), y=RelativeMeasure(0.1)), size=Size(width=RelativeMeasure(0.9), height=RelativeMeasure(0.9)))
image = ImageElement(
    position=position.absolute(size),
    image_path=f"{src_path}/../resources/images/flags/eu.png",
    style=ImageStyle(formatting=ImageFormatting.RESCALE),
)

card = Card(
    size=size,
    elements=[title, subtitle, image],
)

canvas = Canvas_PIL(size=size)
card.render(canvas)
canvas
