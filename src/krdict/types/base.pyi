from collections.abc import Mapping
from enum import Enum
from typing import Any, Generic, Optional, Type, TypeVar, Union, overload

T = TypeVar('T')
EnumType = TypeVar('EnumType', bound='EnumBase')
UnderlyingType = TypeVar('UnderlyingType')

class EnumBase(Generic[UnderlyingType]):
    __aliases__: Mapping[str, UnderlyingType]

    @classmethod
    @property
    def aliases(cls) -> Mapping[str, UnderlyingType]: ...

    @overload
    @classmethod
    def get(cls: Type[EnumType], key: Any) -> Optional[EnumType]: ...

    @overload
    @classmethod
    def get(cls: Type[EnumType], key: Any, default: T) -> Union[EnumType, T]: ...

    @overload
    @classmethod
    def get_value(cls: Type[EnumType], key: Any) -> Optional[UnderlyingType]: ...

    @overload
    @classmethod
    def get_value(cls: Type[EnumType], key: Any, default: T) -> Union[UnderlyingType, T]: ...

class IntEnumBase(int, EnumBase[int], Enum):
    pass

class StrEnumBase(str, EnumBase[str], Enum):
    pass

class EnumProxyBase:
    __populated__: bool
    def __init__(self, populate: bool): ...
