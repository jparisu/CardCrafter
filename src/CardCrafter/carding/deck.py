"""
TODO
"""

from __future__ import annotations
from typing import Any

from CardCrafter.carding.feature import Feature
from CardCrafter.carding.card import Card
from CardCrafter.positioning.size import AbsoluteSize


class Deck:
    """
    TODO
    """

    def __init__(
            self,
            card_size: AbsoluteSize,
            features: dict[str, Feature],
    ) -> None:
        self._card_size = card_size
        self._features = features
        self._cards = []
        self._cards_quantity = []


    def feature_names(self) -> list[str]:
        """
        TODO
        """
        return list(self._features.keys())


    def create_card(self, feature_values: dict[str, Any]) -> Card:
        """
        TODO
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
        TODO
        """
        self._cards.append(card)
        self._cards_quantity.append(quantity)
