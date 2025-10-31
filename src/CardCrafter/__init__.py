"""
CardCrafter: A Python package for crafting and managing customizable cards.
"""

import logging

# Import main classes for public API
from CardCrafter.features import Feature, ImageFeature, TextFeature
from CardCrafter.render import (
    CardConfig,
    CardData,
    CardRenderer,
    RenderContext,
    RenderedImage,
    ResourceCache,
)
from CardCrafter.styles import ImageStyle, Style, TextStyle
from CardCrafter.template import Template
from CardCrafter.value_objects import Align, Anchor, BBox, FitMode, Resolution, Unit

__version__ = "0.1.0"

logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = [
    # Value Objects & Enums
    "BBox",
    "Anchor",
    "Align",
    "FitMode",
    "Unit",
    "Resolution",
    # Styles
    "Style",
    "TextStyle",
    "ImageStyle",
    # Features
    "Feature",
    "TextFeature",
    "ImageFeature",
    # Template
    "Template",
    # Rendering
    "RenderContext",
    "ResourceCache",
    "CardData",
    "CardConfig",
    "CardRenderer",
    "RenderedImage",
]
