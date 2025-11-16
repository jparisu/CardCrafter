"""
Module for defining cards.

This module provides the Card class that represents a single card
with its elements to be rendered.
"""

import logging

from CardCrafter.rendering.element import Element
from CardCrafter.positioning.size import AbsoluteSize
from CardCrafter.rendering.canvas import Canvas

logger = logging.getLogger(__name__)

class Card:
    """
    Represents a single card with its renderable elements.
    
    A card is a composition of elements (text, images, etc.) positioned
    on a canvas of a specific size.
    """

    def __init__(
            self,
            size: AbsoluteSize,
            elements: list[Element],
    ):
        """
        Initialize a card.
        
        Args:
            size: The absolute size of the card.
            elements: The list of elements to render on the card.
        """
        self._size = size
        self._elements = elements


    def render(
            self,
            canvas: Canvas,
    ) -> None:
        """
        Renders all card elements onto a canvas.
        
        Elements are rendered in order of their layer (z-order),
        with lower layer values rendered first.
        
        Args:
            canvas: The canvas to render onto.
        """
        logger.debug(f"Rendering card {self}")

        # For each element in order of their layer, render them onto the canvas
        for element in sorted(self._elements, key=lambda e: e.layer):
            element.render(canvas)
