from collections.abc import Mapping
from enum import Enum, IntEnum
from typing import Any, Optional, Type, TypeVar, Union, overload

T = TypeVar('T')
EnumType = TypeVar('EnumType', bound='EnumBase')

class EnumBase(Enum):
    __aliases__: dict

    @classmethod
    @property
    def aliases(cls) -> Mapping: ...

    @overload
    @classmethod
    def get(cls: Type[EnumType], key: Any, default: T) -> Union[EnumType, T]: ...

    @overload
    @classmethod
    def get(cls: Type[EnumType], key: Any, default=None) -> Optional[EnumType]: ...

    @overload
    @classmethod
    def get_value(cls: Type[EnumType], key: Any, default: Any) -> Any: ...

    @overload
    @classmethod
    def get_value(cls: Type[EnumType], key: Any, default=None) -> Optional[Any]: ...

class IntEnumBase(EnumBase, IntEnum):
    @classmethod
    @property
    def aliases(cls) -> Mapping[str, int]: ...

    @overload
    @classmethod
    def get_value(cls: Type[EnumType], key: Any, default: T) -> Union[int, T]: ...

    @overload
    @classmethod
    def get_value(cls: Type[EnumType], key: Any, default: None=None) -> Optional[int]: ...

class StrEnumBase(str, EnumBase):
    @classmethod
    @property
    def aliases(cls) -> Mapping[str, str]: ...

    @overload
    @classmethod
    def get_value(cls: Type[EnumType], key: Any, default: T) -> Union[str, T]: ...

    @overload
    @classmethod
    def get_value(cls: Type[EnumType], key: Any, default: None=None) -> Optional[str]: ...

class EnumProxyBase:
    __populated__: bool
    def __init__(self, populate: bool): ...
