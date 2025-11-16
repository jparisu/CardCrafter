"""
Module defining the abstract Canvas interface for rendering.

This module provides the abstract base class for canvas implementations
that handle drawing text and images onto a surface.
"""

from PIL import Image, ImageDraw, ImageFont, ImageColor
import logging
from abc import ABC, abstractmethod

from CardCrafter.rendering.element import TextElement, ImageElement

logger = logging.getLogger(__name__)

class Canvas(ABC):
    """
    Abstract base class for rendering canvases.
    
    Defines the interface for adding elements to a canvas and saving the result.
    """

    @abstractmethod
    def add_text(
        self,
        element: TextElement,
    ) -> None:
        """
        Adds a text element to the canvas.
        
        Args:
            element: The text element to add.
        """
        pass


    @abstractmethod
    def add_image(
        self,
        element: ImageElement
    ) -> None:
        """
        Adds an image element to the canvas.
        
        Args:
            element: The image element to add.
        """
        pass


    @abstractmethod
    def save(
        self,
        filepath: str,
    ) -> None:
        """
        Saves the canvas to a file.
        
        Args:
            filepath: The path where the canvas should be saved.
        """
        pass
