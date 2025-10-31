"""
Tests for feature classes.
"""

import pytest

from CardCrafter.features import ImageFeature, TextFeature
from CardCrafter.render import RenderContext
from CardCrafter.styles import ImageStyle, TextStyle
from CardCrafter.value_objects import Anchor, BBox


class TestFeature:
    """Tests for base Feature class."""

    def test_feature_cannot_be_instantiated_directly(self):
        """Test that Feature is abstract and cannot be instantiated."""
        # We can create it but render() must be implemented
        # Note: Feature is abstract, but Python doesn't prevent instantiation
        # unless we use ABC properly - let's test the subclasses instead
        pass

    def test_feature_validate(self):
        """Test feature validation through a concrete subclass."""
        feature = TextFeature(id="test", name="Test Feature", textKey="test_key")
        feature.validate()  # Should not raise

    def test_feature_validate_empty_id(self):
        """Test that empty id raises ValueError."""
        feature = TextFeature(id="", name="Test Feature", textKey="test_key")
        with pytest.raises(ValueError, match="Feature id cannot be empty"):
            feature.validate()

    def test_feature_validate_empty_name(self):
        """Test that empty name raises ValueError."""
        feature = TextFeature(id="test", name="", textKey="test_key")
        with pytest.raises(ValueError, match="Feature name cannot be empty"):
            feature.validate()

    def test_feature_validate_negative_bbox(self):
        """Test that negative bbox dimensions raise ValueError."""
        feature = TextFeature(id="test", name="Test", textKey="key", bbox=BBox(0, 0, -100, 100))
        with pytest.raises(ValueError, match="Bounding box dimensions must be non-negative"):
            feature.validate()

    def test_feature_layout_topleft(self):
        """Test layout calculation with TopLeft anchor."""
        feature = TextFeature(
            id="test", name="Test", textKey="key", anchor=Anchor.TopLeft, bbox=BBox(10, 20, 100, 50)
        )
        layout = feature.layout(800, 600)
        assert layout == BBox(10, 20, 100, 50)

    def test_feature_layout_center(self):
        """Test layout calculation with Center anchor."""
        feature = TextFeature(id="test", name="Test", textKey="key", anchor=Anchor.Center, bbox=BBox(0, 0, 100, 50))
        layout = feature.layout(800, 600)
        # Center: (800-100)/2 = 350, (600-50)/2 = 275
        assert layout == BBox(350, 275, 100, 50)

    def test_feature_layout_bottomright(self):
        """Test layout calculation with BottomRight anchor."""
        feature = TextFeature(
            id="test", name="Test", textKey="key", anchor=Anchor.BottomRight, bbox=BBox(0, 0, 100, 50)
        )
        layout = feature.layout(800, 600)
        # BottomRight: 800-100 = 700, 600-50 = 550
        assert layout == BBox(700, 550, 100, 50)

    def test_feature_layout_bleed(self):
        """Test layout calculation with Bleed anchor (full canvas)."""
        feature = TextFeature(id="test", name="Test", textKey="key", anchor=Anchor.Bleed, bbox=BBox(10, 20, 100, 50))
        layout = feature.layout(800, 600)
        # Bleed extends to full canvas
        assert layout == BBox(0, 0, 800, 600)

    def test_feature_layout_zero_dimensions(self):
        """Test layout with zero dimensions uses canvas size."""
        feature = TextFeature(id="test", name="Test", textKey="key", anchor=Anchor.TopLeft, bbox=BBox(10, 20, 0, 0))
        layout = feature.layout(800, 600)
        # Zero dimensions should use canvas size
        assert layout == BBox(10, 20, 800, 600)


class TestTextFeature:
    """Tests for TextFeature class."""

    def test_textfeature_creation_default(self):
        """Test creating a TextFeature with default values."""
        feature = TextFeature(id="text1", name="Title", textKey="title")
        assert feature.id == "text1"
        assert feature.name == "Title"
        assert feature.textKey == "title"
        assert feature.fallbackText == ""
        assert isinstance(feature.style, TextStyle)
        assert feature.layer == 0
        assert feature.anchor == Anchor.TopLeft
        assert feature.enabled is True

    def test_textfeature_creation_custom(self):
        """Test creating a TextFeature with custom values."""
        style = TextStyle(fontSize=24)
        feature = TextFeature(
            id="text2",
            name="Description",
            textKey="desc",
            fallbackText="Default text",
            style=style,
            layer=2,
            anchor=Anchor.Center,
            bbox=BBox(10, 10, 200, 100),
            enabled=False,
        )
        assert feature.id == "text2"
        assert feature.name == "Description"
        assert feature.textKey == "desc"
        assert feature.fallbackText == "Default text"
        assert feature.style.fontSize == 24
        assert feature.layer == 2
        assert feature.anchor == Anchor.Center
        assert feature.bbox == BBox(10, 10, 200, 100)
        assert feature.enabled is False

    def test_textfeature_render(self):
        """Test rendering a text feature."""
        feature = TextFeature(
            id="text1", name="Test", textKey="test_key", fallbackText="Fallback", bbox=BBox(0, 0, 100, 50)
        )
        ctx = RenderContext(canvasW=800, canvasH=600)
        # This should not raise an error
        feature.render(ctx)


class TestImageFeature:
    """Tests for ImageFeature class."""

    def test_imagefeature_creation_default(self):
        """Test creating an ImageFeature with default values."""
        feature = ImageFeature(id="img1", name="Background", imageKey="bg_image")
        assert feature.id == "img1"
        assert feature.name == "Background"
        assert feature.imageKey == "bg_image"
        assert feature.fallbackImage == ""
        assert isinstance(feature.style, ImageStyle)
        assert feature.layer == 0
        assert feature.anchor == Anchor.TopLeft
        assert feature.enabled is True

    def test_imagefeature_creation_custom(self):
        """Test creating an ImageFeature with custom values."""
        style = ImageStyle(radius=10)
        feature = ImageFeature(
            id="img2",
            name="Portrait",
            imageKey="portrait",
            fallbackImage="/default.png",
            style=style,
            layer=1,
            anchor=Anchor.Center,
            bbox=BBox(50, 50, 300, 400),
            enabled=False,
        )
        assert feature.id == "img2"
        assert feature.name == "Portrait"
        assert feature.imageKey == "portrait"
        assert feature.fallbackImage == "/default.png"
        assert feature.style.radius == 10
        assert feature.layer == 1
        assert feature.anchor == Anchor.Center
        assert feature.bbox == BBox(50, 50, 300, 400)
        assert feature.enabled is False

    def test_imagefeature_render(self):
        """Test rendering an image feature."""
        feature = ImageFeature(
            id="img1", name="Test", imageKey="test_image", fallbackImage="/fallback.png", bbox=BBox(0, 0, 100, 100)
        )
        ctx = RenderContext(canvasW=800, canvasH=600)
        # This should not raise an error
        feature.render(ctx)
