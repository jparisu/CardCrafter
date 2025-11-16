"""
Module for defining decks of cards.

This module provides the Deck class that manages a collection of card features
and can generate individual cards from feature values.
"""

from __future__ import annotations

from typing import Any

from CardCrafter.carding.card import Card
from CardCrafter.carding.feature import Feature
from CardCrafter.positioning.size import AbsoluteSize


class Deck:
    """
    Represents a deck (collection) of cards with shared features.

    A deck defines the common structure (features) that all its cards share,
    and can generate individual cards by providing values for those features.
    """

    def __init__(
            self,
            card_size: AbsoluteSize,
            features: dict[str, Feature],
    ) -> None:
        """
        Initialize a deck.

        Args:
            card_size: The absolute size of cards in this deck.
            features: A dictionary mapping feature names to Feature instances.
        """
        self._card_size = card_size
        self._features = features
        self._cards = []
        self._cards_quantity = []


    def feature_names(self) -> list[str]:
        """
        Gets the names of all features in this deck.

        Returns:
            A list of feature names.
        """
        return list(self._features.keys())


    def create_card(self, feature_values: dict[str, Any]) -> Card:
        """
        Creates a card by providing values for features.

        Args:
            feature_values: A dictionary mapping feature names to their values.
                           Features not in this dict will use their default values if set.

        Returns:
            A Card instance with elements generated from the feature values.
        """
        elements = []
        for name, feature in self._features.items():

            if name in feature_values:
                value = feature_values[name]
                element = feature.generate_element(
                    size=self._card_size,
                    value=value,
                )
                elements.append(element)

            else:
                element = feature.default(
                    size=self._card_size,
                )
                if element is not None:
                    elements.append(element)

        return Card(
            size=self._card_size,
            elements=elements,
        )


    def add_card(self, card: Card, quantity: int = 1) -> None:
        """
        Adds a card to the deck.

        Args:
            card: The card to add.
            quantity: How many copies of this card to add (default: 1).
        """
        self._cards.append(card)
        self._cards_quantity.append(quantity)
