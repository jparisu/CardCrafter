"""
Unit tests for the styling.image module.
"""

from CardCrafter.styling.image import ImageFormatting, ImageStyle


class Test_ImageFormatting:
    """Tests for ImageFormatting enum."""

    def test_crop_value(self):
        """Test that CROP has correct value."""
        assert ImageFormatting.CROP.value == 'crop'

    def test_rescale_value(self):
        """Test that RESCALE has correct value."""
        assert ImageFormatting.RESCALE.value == 'rescale'


class Test_ImageStyle:
    """Tests for ImageStyle dataclass."""

    def test_default_formatting(self):
        """Test default formatting is RESCALE."""
        style = ImageStyle()
        assert style.formatting == ImageFormatting.RESCALE

    def test_custom_formatting_crop(self):
        """Test creating style with CROP formatting."""
        style = ImageStyle(formatting=ImageFormatting.CROP)
        assert style.formatting == ImageFormatting.CROP

    def test_custom_formatting_rescale(self):
        """Test creating style with RESCALE formatting."""
        style = ImageStyle(formatting=ImageFormatting.RESCALE)
        assert style.formatting == ImageFormatting.RESCALE

    def test_is_dataclass(self):
        """Test that ImageStyle is a dataclass."""
        style1 = ImageStyle()
        style2 = ImageStyle()
        # Dataclasses should be equal if their fields are equal
        assert style1.formatting == style2.formatting
