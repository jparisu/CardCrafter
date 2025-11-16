"""
Unit tests for the yaml_utils.exceptions module.
"""

import pytest

from CardCrafter.yaml_utils.exceptions import (
    YamlFormatError,
    YamlKeyError,
    YamlTypeError,
)


class Test_YamlFormatError:
    """Tests for YamlFormatError exception."""

    def test_is_value_error(self):
        """Test that YamlFormatError is a ValueError."""
        assert issubclass(YamlFormatError, ValueError)

    def test_raise_with_message(self):
        """Test raising YamlFormatError with a message."""
        with pytest.raises(YamlFormatError, match="Invalid format"):
            raise YamlFormatError("Invalid format")

    def test_raise_without_message(self):
        """Test raising YamlFormatError without a message."""
        with pytest.raises(YamlFormatError):
            raise YamlFormatError()


class Test_YamlKeyError:
    """Tests for YamlKeyError exception."""

    def test_is_key_error(self):
        """Test that YamlKeyError is a KeyError."""
        assert issubclass(YamlKeyError, KeyError)

    def test_raise_with_message(self):
        """Test raising YamlKeyError with a message."""
        with pytest.raises(YamlKeyError, match="Missing key"):
            raise YamlKeyError("Missing key")

    def test_raise_without_message(self):
        """Test raising YamlKeyError without a message."""
        with pytest.raises(YamlKeyError):
            raise YamlKeyError()


class Test_YamlTypeError:
    """Tests for YamlTypeError exception."""

    def test_is_type_error(self):
        """Test that YamlTypeError is a TypeError."""
        assert issubclass(YamlTypeError, TypeError)

    def test_raise_with_message(self):
        """Test raising YamlTypeError with a message."""
        with pytest.raises(YamlTypeError, match="Wrong type"):
            raise YamlTypeError("Wrong type")

    def test_raise_without_message(self):
        """Test raising YamlTypeError without a message."""
        with pytest.raises(YamlTypeError):
            raise YamlTypeError()
