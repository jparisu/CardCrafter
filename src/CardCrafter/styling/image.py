"""
TODO
"""

from enum import Enum
from dataclasses import dataclass

class ImageFormatting(Enum):
    CROP = 'crop'
    RESCALE = 'rescale'


@dataclass
class ImageStyle:

    formatting: ImageFormatting = ImageFormatting.RESCALE
