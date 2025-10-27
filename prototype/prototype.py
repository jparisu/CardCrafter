
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
from typing import Any
import logging

class Feature(ABC):

    def __init__(
            self,
            layer: int,
            top_left: tuple[float, float],
            bottom_right: tuple[float, float]
    ):
        self.layer = layer
        self.top_left = top_left
        self.bottom_right = bottom_right

    @abstractmethod
    def render(
            self,
            value: Any,
            canvas: Image.Image,
            draw: ImageDraw.ImageDraw,
    ):
        pass

    def _calculate_own_shape(self, canvas_shape: tuple[int, int]):
        canvas_width, canvas_height = canvas_shape
        own_top_left_x = int(self.top_left[0] * canvas_width)
        own_top_left_y = int(self.top_left[1] * canvas_height)
        own_bottom_right_x = int(self.bottom_right[0] * canvas_width)
        own_bottom_right_y = int(self.bottom_right[1] * canvas_height)
        return ((own_top_left_x, own_top_left_y), (own_bottom_right_x, own_bottom_right_y))



class ColorFeature(Feature):

    def __init__(
            self,
            layer: int,
            top_left: tuple[int, int],
            bottom_right: tuple[int, int],
    ):
        super().__init__(layer, top_left, bottom_right)


    def render(
            self,
            value: Any,
            canvas: Image.Image,
            draw: ImageDraw.ImageDraw,
    ):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Value must be a string representing a color for ColorFeature.")
        # Check if the value is a valid color
        try:
            ImageColor.getrgb(value)
        except ValueError:
            raise ValueError(f"Value '{value}' is not a valid color string for ColorFeature.")

        # Calculate shape
        shape = self._calculate_own_shape(canvas.size)

        logging.debug(f"Drawing ColorFeature with color {value} at {shape}")

        # Draw the rectangle on the image
        draw.rectangle(shape, fill=value)



@dataclass
class TextStyle:
    font_size: int
    font_color: str
    alignment: str


class TextFeature(Feature):

    def __init__(
            self,
            layer: int,
            top_left: tuple[int, int],
            bottom_right: tuple[int, int],
            style: TextStyle
    ):
        super().__init__(layer, top_left, bottom_right)
        self.style = style


    def render(
            self,
            value: Any,
            canvas: Image.Image,
            draw: ImageDraw.ImageDraw,
    ):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Value must be a string for TextFeature.")

        # Calculate shape
        shape = self._calculate_own_shape(canvas.size)

        logging.debug(f"Drawing TextFeature with text '{value}' at {shape}")

        # Draw the text on the image
        font = ImageFont.truetype("DejaVuSans.ttf", self.style.font_size)
        draw.text(
            shape[0],
            value,
            font=font,
            fill=self.style.font_color,
            anchor=self.style.alignment
        )


@dataclass
class ImageStyle:
    crop: bool
    resize: bool


class ImageFeature(Feature):
    def __init__(
            self,
            layer: int,
            top_left: tuple[int, int],
            bottom_right: tuple[int, int],
            style: ImageStyle,
    ):
        super().__init__(layer, top_left, bottom_right)
        self.style = style


    def render(
            self,
            value: Any,
            canvas: Image.Image,
            draw: ImageDraw.ImageDraw,
    ):
        # Check if the value is a string
        if not isinstance(value, str):
            raise ValueError("Value must be a string for ImageFeature.")
        # Check if the value is a correct path
        if not os.path.isfile(value):
            raise ValueError(f"Value '{value}' is not a valid file path for ImageFeature.")

        # Calculate shape
        shape = self._calculate_own_shape(canvas.size)

        logging.debug(f"Drawing ImageFeature with image '{value}' at {shape}")

        # Resize the image
        img = Image.open(value)
        if self.style.resize:
            img = img.resize((shape[1][0] - shape[0][0], shape[1][1] - shape[0][1]))
        elif self.style.crop:
            img = img.crop((0, 0, shape[1][0] - shape[0][0], shape[1][1] - shape[0][1]))

        # Include the image on the canvas
        canvas.paste(img, shape[0])



class Card:

    def __init__(
            self,
            width: int,
            height: int,
            features: dict[str, Feature]
    ):
        self.width = width
        self.height = height
        self.features = features

    def render(
            self,
            configuration: dict[str, any],
            result_path: str
    ):
        # Create a blank canvas
        canvas = Image.new('RGBA', (self.width, self.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(canvas)

        # Sort features by layer
        sorted_features = sorted(
            self.features.items(),
            key=lambda item: item[1].layer
        )

        # Render each feature
        for feature_name, feature in sorted_features:
            if feature_name in configuration:
                feature.render(configuration[feature_name], canvas, draw)

        # Save the final image
        canvas.save(result_path)


logging.getLogger(__name__).addHandler(logging.NullHandler())


if __name__ == "__main__":

    # Set debug logging level
    logging.basicConfig(level=logging.DEBUG)

    # Example usage
    card = Card(
        width=400,
        height=600,
        features={
            "background": ColorFeature(
                layer=0,
                top_left=(0.0, 0.0),
                bottom_right=(1.0, 1.0)
            ),
            "title": TextFeature(
                layer=2,
                top_left=(0, 0),
                bottom_right=(0.1, 1),
                style=TextStyle(
                    font_size=40,
                    font_color="black",
                    alignment="lt"
                )
            ),
            "subtitle": TextFeature(
                layer=2,
                top_left=(0.0, 0.1),
                bottom_right=(0.2, 1),
                style=TextStyle(
                    font_size=20,
                    font_color="black",
                    alignment="lt"
                )
            ),
            "image": ImageFeature(
                layer=1,
                top_left=(0.1, 0.25),
                bottom_right=(0.9, 0.9),
                style=ImageStyle(
                    crop=False,
                    resize=True,
                )
            )
        }
    )

    configuration = {
        "background": "#FFDDCC",
        "title": "Sample Card 1",
        "subtitle": "This is the first sample card.",
        "image": "resources/images/flags/eu.png",
    }

    card.render(configuration, "prototype/example_card.png")
