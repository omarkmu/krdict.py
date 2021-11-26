from abc import ABC, abstractmethod
from collections.abc import Mapping
from enum import IntEnum
from typing import Optional, Type, TypeVar, Union, overload

T = TypeVar('T')
EnumType = TypeVar('EnumType', bound='EnumBase')

class EnumBase(ABC):
    __aliases__: dict

    @classmethod
    @property
    def aliases(cls) -> Mapping: ...

    @overload
    @classmethod
    @abstractmethod
    def get(cls: Type[EnumType], key, default: None = None) -> Optional[EnumType]: ...

    @overload
    @classmethod
    @abstractmethod
    def get(cls: Type[EnumType], key, default: T) -> Union[EnumType, T]: ...

class IntEnumBase(EnumBase, IntEnum):
    pass

class EnumProxyBase:
    __populated__: bool
    def __init__(self, populate: bool): ...
