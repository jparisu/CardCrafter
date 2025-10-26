"""
Tests for template class.
"""

import pytest

from CardCrafter.features import TextFeature
from CardCrafter.template import Template
from CardCrafter.value_objects import BBox, Resolution


class TestTemplate:
    """Tests for Template class."""

    def test_template_creation_default(self):
        """Test creating a Template with default values."""
        res = Resolution(1920, 1080)
        template = Template(name="Card Template", resolution=res)
        assert template.name == "Card Template"
        assert template.resolution == res
        assert template.dpi == 300
        assert template.safeMargin == 0
        assert template.bleed == 0
        assert template.features == []

    def test_template_creation_custom(self):
        """Test creating a Template with custom values."""
        res = Resolution(2100, 2970)
        features = [
            TextFeature(id="title", name="Title", textKey="title"),
            TextFeature(id="desc", name="Description", textKey="desc"),
        ]
        template = Template(
            name="Custom Card",
            resolution=res,
            dpi=600,
            safeMargin=50,
            bleed=25,
            features=features,
        )
        assert template.name == "Custom Card"
        assert template.resolution == res
        assert template.dpi == 600
        assert template.safeMargin == 50
        assert template.bleed == 25
        assert len(template.features) == 2

    def test_template_invalid_dpi(self):
        """Test that invalid dpi raises ValueError."""
        res = Resolution(1920, 1080)
        with pytest.raises(ValueError, match="dpi must be positive"):
            Template(name="Test", resolution=res, dpi=0)

        with pytest.raises(ValueError, match="dpi must be positive"):
            Template(name="Test", resolution=res, dpi=-100)

    def test_template_invalid_safemargin(self):
        """Test that invalid safeMargin raises ValueError."""
        res = Resolution(1920, 1080)
        with pytest.raises(ValueError, match="safeMargin must be non-negative"):
            Template(name="Test", resolution=res, safeMargin=-10)

    def test_template_invalid_bleed(self):
        """Test that invalid bleed raises ValueError."""
        res = Resolution(1920, 1080)
        with pytest.raises(ValueError, match="bleed must be non-negative"):
            Template(name="Test", resolution=res, bleed=-5)

    def test_template_get_features_by_layer(self):
        """Test getting features sorted by layer."""
        res = Resolution(1920, 1080)
        features = [
            TextFeature(id="f3", name="F3", textKey="k3", layer=3),
            TextFeature(id="f1", name="F1", textKey="k1", layer=1),
            TextFeature(id="f2", name="F2", textKey="k2", layer=2),
        ]
        template = Template(name="Test", resolution=res, features=features)
        sorted_features = template.getFeaturesByLayer()
        assert len(sorted_features) == 3
        assert sorted_features[0].id == "f1"
        assert sorted_features[1].id == "f2"
        assert sorted_features[2].id == "f3"

    def test_template_validate_success(self):
        """Test validating a valid template."""
        res = Resolution(1920, 1080)
        features = [
            TextFeature(id="title", name="Title", textKey="title", bbox=BBox(0, 0, 100, 50)),
        ]
        template = Template(name="Valid Template", resolution=res, features=features)
        template.validate()  # Should not raise

    def test_template_validate_empty_name(self):
        """Test that empty name raises ValueError during validation."""
        res = Resolution(1920, 1080)
        template = Template(name="", resolution=res)
        with pytest.raises(ValueError, match="Template name cannot be empty"):
            template.validate()

    def test_template_validate_invalid_resolution(self):
        """Test that invalid resolution raises ValueError during validation."""
        res = Resolution(0, 1080)
        template = Template(name="Test", resolution=res)
        with pytest.raises(ValueError, match="Template resolution must be positive"):
            template.validate()

        res2 = Resolution(1920, -100)
        template2 = Template(name="Test", resolution=res2)
        with pytest.raises(ValueError, match="Template resolution must be positive"):
            template2.validate()

    def test_template_validate_invalid_feature(self):
        """Test that invalid feature raises ValueError during validation."""
        res = Resolution(1920, 1080)
        # Create a feature with empty id
        features = [
            TextFeature(id="", name="Test", textKey="key"),
        ]
        template = Template(name="Test", resolution=res, features=features)
        with pytest.raises(ValueError, match="Invalid feature"):
            template.validate()
