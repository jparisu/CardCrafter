"""
Tests for value objects and enums.
"""


from CardCrafter.value_objects import Align, Anchor, BBox, FitMode, Resolution, Unit


class TestBBox:
    """Tests for BBox class."""

    def test_bbox_creation(self):
        """Test creating a BBox."""
        bbox = BBox(10, 20, 100, 200)
        assert bbox.x == 10
        assert bbox.y == 20
        assert bbox.w == 100
        assert bbox.h == 200

    def test_bbox_is_named_tuple(self):
        """Test that BBox behaves like a NamedTuple."""
        bbox = BBox(10, 20, 100, 200)
        assert isinstance(bbox, tuple)
        assert len(bbox) == 4


class TestAnchor:
    """Tests for Anchor enum."""

    def test_anchor_values(self):
        """Test all anchor values exist."""
        assert Anchor.TopLeft.value == "top_left"
        assert Anchor.Top.value == "top"
        assert Anchor.TopRight.value == "top_right"
        assert Anchor.Left.value == "left"
        assert Anchor.Center.value == "center"
        assert Anchor.Right.value == "right"
        assert Anchor.BottomLeft.value == "bottom_left"
        assert Anchor.Bottom.value == "bottom"
        assert Anchor.BottomRight.value == "bottom_right"
        assert Anchor.Bleed.value == "bleed"


class TestAlign:
    """Tests for Align enum."""

    def test_align_values(self):
        """Test all align values exist."""
        assert Align.Left.value == "left"
        assert Align.Center.value == "center"
        assert Align.Right.value == "right"


class TestFitMode:
    """Tests for FitMode enum."""

    def test_fitmode_values(self):
        """Test all fit mode values exist."""
        assert FitMode.Cover.value == "cover"
        assert FitMode.Contain.value == "contain"
        assert FitMode.ScaleDown.value == "scale_down"


class TestUnit:
    """Tests for Unit enum."""

    def test_unit_values(self):
        """Test all unit values exist."""
        assert Unit.Px.value == "px"
        assert Unit.Pt.value == "pt"
        assert Unit.Mm.value == "mm"


class TestResolution:
    """Tests for Resolution class."""

    def test_resolution_creation(self):
        """Test creating a Resolution."""
        res = Resolution(1920, 1080)
        assert res.width == 1920
        assert res.height == 1080

    def test_aspect_ratio(self):
        """Test aspect ratio calculation."""
        res = Resolution(1920, 1080)
        assert res.aspect() == "16:9"

        res2 = Resolution(1000, 1000)
        assert res2.aspect() == "1:1"

        res3 = Resolution(2100, 2970)
        assert res3.aspect() == "70:99"

    def test_resolution_is_named_tuple(self):
        """Test that Resolution behaves like a NamedTuple."""
        res = Resolution(1920, 1080)
        assert isinstance(res, tuple)
        assert len(res) == 2
