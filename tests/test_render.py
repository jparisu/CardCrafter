"""
Tests for rendering classes.
"""

import pytest

from CardCrafter.features import TextFeature
from CardCrafter.render import CardConfig, CardData, CardRenderer, RenderContext, RenderedImage, ResourceCache
from CardCrafter.styles import TextStyle
from CardCrafter.template import Template
from CardCrafter.value_objects import BBox, Resolution


class TestResourceCache:
    """Tests for ResourceCache class."""

    def test_cache_creation(self):
        """Test creating a ResourceCache."""
        cache = ResourceCache()
        assert isinstance(cache._fonts, dict)
        assert isinstance(cache._images, dict)

    def test_cache_get_font(self):
        """Test getting a font from cache."""
        cache = ResourceCache()
        font1 = cache.getFont("/path/to/font.ttf", 12)
        font2 = cache.getFont("/path/to/font.ttf", 12)
        # Should return the same cached object
        assert font1 is font2

    def test_cache_get_font_different_sizes(self):
        """Test that different font sizes are cached separately."""
        cache = ResourceCache()
        font1 = cache.getFont("/path/to/font.ttf", 12)
        font2 = cache.getFont("/path/to/font.ttf", 24)
        # Should return different objects
        assert font1 is not font2

    def test_cache_get_image(self):
        """Test getting an image from cache."""
        cache = ResourceCache()
        img1 = cache.getImage("/path/to/image.png")
        img2 = cache.getImage("/path/to/image.png")
        # Should return the same cached object
        assert img1 is img2


class TestCardData:
    """Tests for CardData class."""

    def test_carddata_creation_empty(self):
        """Test creating an empty CardData."""
        data = CardData()
        assert data.values == {}

    def test_carddata_creation_with_values(self):
        """Test creating CardData with initial values."""
        values = {"title": "Card Title", "description": "Card Description"}
        data = CardData(values=values)
        assert data.values == values

    def test_carddata_get_existing_key(self):
        """Test getting an existing key."""
        data = CardData(values={"name": "John"})
        assert data.get("name") == "John"

    def test_carddata_get_missing_key_default(self):
        """Test getting a missing key returns default."""
        data = CardData()
        assert data.get("missing") == ""
        assert data.get("missing", "default") == "default"


class TestCardConfig:
    """Tests for CardConfig class."""

    def test_cardconfig_creation_empty(self):
        """Test creating an empty CardConfig."""
        config = CardConfig()
        assert config.globalStyles == {}
        assert config.tokens == {}

    def test_cardconfig_creation_with_values(self):
        """Test creating CardConfig with initial values."""
        styles = {"title": TextStyle(fontSize=24)}
        tokens = {"primary_color": "#FF0000"}
        config = CardConfig(globalStyles=styles, tokens=tokens)
        assert config.globalStyles == styles
        assert config.tokens == tokens


class TestRenderContext:
    """Tests for RenderContext class."""

    def test_rendercontext_creation_default(self):
        """Test creating a RenderContext with default values."""
        ctx = RenderContext(canvasW=800, canvasH=600)
        assert ctx.canvasW == 800
        assert ctx.canvasH == 600
        assert ctx.dpi == 300
        assert ctx.backend == "Pillow"
        assert isinstance(ctx.resources, ResourceCache)
        assert isinstance(ctx.data, CardData)

    def test_rendercontext_creation_custom(self):
        """Test creating a RenderContext with custom values."""
        cache = ResourceCache()
        data = CardData(values={"key": "value"})
        ctx = RenderContext(canvasW=1920, canvasH=1080, dpi=600, backend="Cairo", resources=cache, data=data)
        assert ctx.canvasW == 1920
        assert ctx.canvasH == 1080
        assert ctx.dpi == 600
        assert ctx.backend == "Cairo"
        assert ctx.resources is cache
        assert ctx.data is data

    def test_rendercontext_invalid_canvas_dimensions(self):
        """Test that invalid canvas dimensions raise ValueError."""
        with pytest.raises(ValueError, match="Canvas dimensions must be positive"):
            RenderContext(canvasW=0, canvasH=600)

        with pytest.raises(ValueError, match="Canvas dimensions must be positive"):
            RenderContext(canvasW=800, canvasH=-600)

    def test_rendercontext_invalid_dpi(self):
        """Test that invalid dpi raises ValueError."""
        with pytest.raises(ValueError, match="dpi must be positive"):
            RenderContext(canvasW=800, canvasH=600, dpi=0)

    def test_rendercontext_get_text_value(self):
        """Test getting text value from context data."""
        data = CardData(values={"title": "My Title"})
        ctx = RenderContext(canvasW=800, canvasH=600, data=data)
        assert ctx.get_text_value("title", "fallback") == "My Title"
        assert ctx.get_text_value("missing", "fallback") == "fallback"

    def test_rendercontext_get_image_value(self):
        """Test getting image value from context data."""
        data = CardData(values={"image": "/path/to/image.png"})
        ctx = RenderContext(canvasW=800, canvasH=600, data=data)
        assert ctx.get_image_value("image", "/fallback.png") == "/path/to/image.png"
        assert ctx.get_image_value("missing", "/fallback.png") == "/fallback.png"

    def test_rendercontext_draw_image(self):
        """Test drawing an image (placeholder implementation)."""
        ctx = RenderContext(canvasW=800, canvasH=600)
        img = {"path": "/test.png"}
        # Should not raise an error
        ctx.drawImage(img, 10, 20, 100, 100, radius=5)

    def test_rendercontext_draw_text(self):
        """Test drawing text (placeholder implementation)."""
        ctx = RenderContext(canvasW=800, canvasH=600)
        style = TextStyle()
        bbox = BBox(10, 20, 200, 50)
        # Should not raise an error
        ctx.drawText("Test Text", bbox, style)


class TestRenderedImage:
    """Tests for RenderedImage class."""

    def test_renderedimage_creation(self):
        """Test creating a RenderedImage."""
        img = RenderedImage(width=1920, height=1080)
        assert img.width == 1920
        assert img.height == 1080

    def test_renderedimage_invalid_dimensions(self):
        """Test that invalid dimensions raise ValueError."""
        with pytest.raises(ValueError, match="Image dimensions must be positive"):
            RenderedImage(width=0, height=1080)

        with pytest.raises(ValueError, match="Image dimensions must be positive"):
            RenderedImage(width=1920, height=-100)

    def test_renderedimage_save_png(self):
        """Test saving as PNG (placeholder implementation)."""
        img = RenderedImage(width=800, height=600)
        # Should not raise an error (placeholder)
        img.savePng("/tmp/test.png")

    def test_renderedimage_save_pdf(self):
        """Test saving as PDF (placeholder implementation)."""
        img = RenderedImage(width=800, height=600)
        # Should not raise an error (placeholder)
        img.savePdf("/tmp/test.pdf")


class TestCardRenderer:
    """Tests for CardRenderer class."""

    def test_cardrenderer_creation(self):
        """Test creating a CardRenderer."""
        renderer = CardRenderer()
        assert renderer is not None

    def test_cardrenderer_render(self):
        """Test rendering a card."""
        # Create a simple template
        res = Resolution(800, 600)
        features = [
            TextFeature(id="title", name="Title", textKey="title", layer=0, bbox=BBox(10, 10, 200, 50)),
        ]
        template = Template(name="Test Card", resolution=res, features=features)

        # Create card data
        data = CardData(values={"title": "Test Title"})

        # Create config
        config = CardConfig()

        # Render the card
        renderer = CardRenderer()
        result = renderer.render(template, data, config)

        assert isinstance(result, RenderedImage)
        assert result.width == 800
        assert result.height == 600

    def test_cardrenderer_render_invalid_template(self):
        """Test that rendering with invalid template raises ValueError."""
        renderer = CardRenderer()
        # Template with empty name
        template = Template(name="", resolution=Resolution(800, 600))
        data = CardData()
        config = CardConfig()

        with pytest.raises(ValueError, match="Template name cannot be empty"):
            renderer.render(template, data, config)

    def test_cardrenderer_render_with_layers(self):
        """Test rendering with multiple features in different layers."""
        res = Resolution(800, 600)
        features = [
            TextFeature(id="f3", name="F3", textKey="k3", layer=3),
            TextFeature(id="f1", name="F1", textKey="k1", layer=1),
            TextFeature(id="f2", name="F2", textKey="k2", layer=2, enabled=False),
        ]
        template = Template(name="Multi-layer Card", resolution=res, features=features)
        data = CardData(values={"k1": "Text 1", "k2": "Text 2", "k3": "Text 3"})
        config = CardConfig()

        renderer = CardRenderer()
        result = renderer.render(template, data, config)

        assert isinstance(result, RenderedImage)

    def test_cardrenderer_resolve_value(self):
        """Test resolving values from card data."""
        renderer = CardRenderer()
        data = CardData(values={"title": "My Title"})

        # Test private method (not ideal but checking implementation)
        result = renderer._resolveValue("title", data, "fallback")
        assert result == "My Title"

        result = renderer._resolveValue("missing", data, "fallback")
        assert result == "fallback"
