"""
Contains base class for KRDict enumeration helpers.
"""

# pylint: disable=too-few-public-methods

from collections.abc import Mapping
from enum import Enum

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

class EnumBase(Enum):
    """Base class for enumerations."""

    __ALIASES__ = {}

    @classmethod
    @property
    def aliases(cls):
        """The alias dictionary of the enumeration."""
        return _ReadOnlyDict(cls.__ALIASES__)

    @classmethod
    def get(cls, key, default_value=None):
        """
        Returns the enumeration associated with a literal, or the default value
        if the literal is not associated with any enumeration value.
        """

        if isinstance(key, cls):
            return cls(key.value)

        if isinstance(key, str):
            literal_value = cls.__ALIASES__.get(key)

            if literal_value is None:
                try:
                    return cls[key]
                except KeyError:
                    return default_value

            key = literal_value

        try:
            return cls(key)
        except ValueError:
            return default_value

class EnumProxyBase:
    """Base class for enumeration proxies."""

    def __init__(self, populate):
        self.__populated__ = populate
