"""
Contains base class for KRDict enumeration helpers.
"""

# pylint: disable=too-few-public-methods

from collections.abc import Mapping
from enum import Enum, IntEnum

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
        return str(self._dict)

    def __repr__(self):
        return repr(self._dict)

class EnumBase(Enum):
    """Base class for enumerations."""

    __aliases__ = {}

    @classmethod
    @property
    def aliases(cls):
        """The alias dictionary of the enumeration."""
        return _ReadOnlyDict(cls.__aliases__)

    @classmethod
    def get(cls, key, default=None):
        """
        Returns the enumeration instance associated with a literal,
        or the provided default value if the literal is not associated with any enumeration.
        """

        if isinstance(key, cls):
            return cls(key.value)

        if isinstance(key, str):
            literal_value = cls.__aliases__.get(key)

            if literal_value is not None:
                key = literal_value
            else:
                try:
                    return cls[key]
                except KeyError:
                    pass

        try:
            return cls(key)
        except ValueError:
            return default

    @classmethod
    def get_value(cls, key, default=None):
        """
        Returns the enumeration value associated with a literal,
        or the provided default value if the literal is not associated with any enumeration.
        """

        enum_instance = cls.get(key)
        return enum_instance.value if enum_instance is not None else default

class IntEnumBase(EnumBase, IntEnum):
    """Base class for integer-based enumerations."""

class StrEnumBase(str, EnumBase):
    """Base class for string-based enumerations."""

    def __str__(self):
        return Enum.__str__(self)

class EnumProxyBase:
    """Base class for enumeration proxies."""

    def __init__(self, populate):
        self.__populated__ = populate
