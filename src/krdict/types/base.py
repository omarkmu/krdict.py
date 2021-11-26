"""
Contains base class for KRDict enumeration helpers.
"""

# pylint: disable=too-few-public-methods

from collections.abc import Mapping
from enum import IntEnum

class _ReadOnlyDict(Mapping):
    def __init__(self, data):
        self._dict = data

    def __getitem__(self, key):
        return self._dict[key]

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict)

    def __str__(self):
        return self._dict.__str__()

    def __repr__(self):
        return self._dict.__repr__()

class EnumBase:
    """Base class for enumerations."""

    __aliases__ = {}

    @classmethod
    @property
    def aliases(cls):
        """The alias dictionary of the enumeration."""
        return _ReadOnlyDict(cls.__aliases__)

class IntEnumBase(EnumBase, IntEnum):
    """Base class for integer-based enumerations."""

    @classmethod
    def get(cls, key, default=None):
        """
        Returns the enumeration associated with a literal, or the default value
        if the literal is not associated with any enumeration value.
        """

        if isinstance(key, cls):
            return cls(key.value)

        if isinstance(key, str):
            literal_value = cls.__aliases__.get(key)

            if literal_value is None:
                try:
                    return cls[key]
                except KeyError:
                    return default

            key = literal_value

        try:
            return cls(key)
        except ValueError:
            return default

class EnumProxyBase:
    """Base class for enumeration proxies."""

    def __init__(self, populate):
        self.__populated__ = populate
