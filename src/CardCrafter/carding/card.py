"""
TODO
"""

import logging

from CardCrafter.rendering.element import Element
from CardCrafter.positioning.size import AbsoluteSize
from CardCrafter.rendering.canvas import Canvas

logger = logging.getLogger(__name__)

class Card:

    def __init__(
            self,
            size: AbsoluteSize,
            elements: list[Element],
    ):
        self._size = size
        self._elements = elements


    def render(
            self,
            canvas: Canvas,
    ) -> None:
        """TODO"""
        logger.debug(f"Rendering card {self}")

        # For each element in order of their layer, render them onto the canvas
        for element in sorted(self._elements, key=lambda e: e.layer):
            element.render(canvas)
