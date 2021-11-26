from collections.abc import Mapping
from enum import Enum
from typing import Generic, Optional, Type, TypeVar, Union, overload

class EnumBase(Enum):
    @classmethod
    @property
    def aliases(cls) -> Mapping: ...

    @overload
    @classmethod
    def get(cls: EnumType, key, default_value: None = None) -> Optional[EnumType]: ...

    @overload
    @classmethod
    def get(cls: EnumType, key, default_value: T = None) -> Union[EnumType, T]: ...

T = TypeVar('T')
EnumType = TypeVar('EnumType', bound=EnumBase)

class EnumProxyMeta(type, Generic[EnumType]):
    def __getitem__(cls, key) -> EnumType: ...

class EnumProxyBase(Generic[EnumType]):
    _ENUM: Type[EnumType]
    _LITERALS: dict

    def __new__(cls, value) -> EnumType: ...

    @classmethod
    @property
    def aliases(cls) -> Mapping: ...

    @classmethod
    @property
    def enum(cls) -> Type[EnumType]: ...

    @overload
    @classmethod
    def get(cls, key, default_value: None = None) -> Optional[EnumType]: ...

    @overload
    @classmethod
    def get(cls, key, default_value: T = None) -> Union[EnumType, T]: ...

