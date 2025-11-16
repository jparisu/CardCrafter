"""
Module for handling image styling.

This module provides enumerations and classes for configuring how images
are displayed within their designated space.
"""

from enum import Enum
from dataclasses import dataclass

class ImageFormatting(Enum):
    """
    Enumeration of image formatting options.
    
    Attributes:
        CROP: Crop the image to fit the space.
        RESCALE: Rescale/resize the image to fit the space.
    """
    CROP = 'crop'
    RESCALE = 'rescale'


@dataclass
class ImageStyle:
    """
    Represents the styling options for an image element.
    
    Attributes:
        formatting: How the image should be adjusted to fit its space (default: RESCALE).
    """

    formatting: ImageFormatting = ImageFormatting.RESCALE
