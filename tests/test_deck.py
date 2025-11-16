"""
Unit tests for the carding.deck module.
"""

from CardCrafter.carding.card import Card
from CardCrafter.carding.deck import Deck
from CardCrafter.carding.feature import TextFeature
from CardCrafter.positioning.measure import AbsoluteMeasure, MeasureUnit
from CardCrafter.positioning.point import Point
from CardCrafter.positioning.position import Position
from CardCrafter.positioning.size import AbsoluteSize, Size


class Test_Deck:
    """Tests for Deck class."""

    def test_init(self):
        """Test Deck initialization."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        features = {}
        deck = Deck(card_size, features)
        assert deck._card_size == card_size
        assert deck._features == features
        assert deck._cards == []
        assert deck._cards_quantity == []

    def test_init_with_features(self):
        """Test Deck initialization with features."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        feat_width = AbsoluteMeasure(50, MeasureUnit.MM)
        feat_height = AbsoluteMeasure(30, MeasureUnit.MM)
        feat_size = Size(feat_width, feat_height)
        position = Position(point, feat_size)

        feature = TextFeature("title", position)
        features = {"title": feature}

        deck = Deck(card_size, features)
        assert "title" in deck._features

    def test_feature_names_empty(self):
        """Test feature_names with no features."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        deck = Deck(card_size, {})
        assert deck.feature_names() == []

    def test_feature_names(self):
        """Test feature_names method."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        feat_width = AbsoluteMeasure(50, MeasureUnit.MM)
        feat_height = AbsoluteMeasure(30, MeasureUnit.MM)
        feat_size = Size(feat_width, feat_height)
        position = Position(point, feat_size)

        feature1 = TextFeature("title", position)
        feature2 = TextFeature("description", position)
        features = {"title": feature1, "description": feature2}

        deck = Deck(card_size, features)
        names = deck.feature_names()
        assert "title" in names
        assert "description" in names
        assert len(names) == 2

    def test_create_card_empty_features(self):
        """Test creating card with no features."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        deck = Deck(card_size, {})
        card = deck.create_card({})

        assert isinstance(card, Card)
        assert len(card._elements) == 0

    def test_create_card_with_values(self):
        """Test creating card with feature values."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        feat_width = AbsoluteMeasure(50, MeasureUnit.MM)
        feat_height = AbsoluteMeasure(30, MeasureUnit.MM)
        feat_size = Size(feat_width, feat_height)
        position = Position(point, feat_size)

        feature = TextFeature("title", position)
        features = {"title": feature}

        deck = Deck(card_size, features)
        card = deck.create_card({"title": "Test Title"})

        assert isinstance(card, Card)
        assert len(card._elements) == 1

    def test_create_card_missing_value_no_default(self):
        """Test creating card without value and no default."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        x = AbsoluteMeasure(10, MeasureUnit.MM)
        y = AbsoluteMeasure(20, MeasureUnit.MM)
        point = Point(x, y)
        feat_width = AbsoluteMeasure(50, MeasureUnit.MM)
        feat_height = AbsoluteMeasure(30, MeasureUnit.MM)
        feat_size = Size(feat_width, feat_height)
        position = Position(point, feat_size)

        feature = TextFeature("title", position)
        features = {"title": feature}

        deck = Deck(card_size, features)
        card = deck.create_card({})  # No value provided

        assert isinstance(card, Card)
        assert len(card._elements) == 0  # No default, so no element

    def test_add_card(self):
        """Test adding a card to the deck."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        deck = Deck(card_size, {})
        card = Card(card_size, [])

        deck.add_card(card)
        assert len(deck._cards) == 1
        assert deck._cards[0] == card
        assert deck._cards_quantity[0] == 1

    def test_add_card_with_quantity(self):
        """Test adding a card with quantity."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        deck = Deck(card_size, {})
        card = Card(card_size, [])

        deck.add_card(card, quantity=5)
        assert len(deck._cards) == 1
        assert deck._cards_quantity[0] == 5

    def test_add_multiple_cards(self):
        """Test adding multiple cards."""
        width = AbsoluteMeasure(100, MeasureUnit.MM)
        height = AbsoluteMeasure(150, MeasureUnit.MM)
        card_size = AbsoluteSize(width, height)

        deck = Deck(card_size, {})
        card1 = Card(card_size, [])
        card2 = Card(card_size, [])

        deck.add_card(card1, quantity=2)
        deck.add_card(card2, quantity=3)

        assert len(deck._cards) == 2
        assert deck._cards_quantity == [2, 3]
