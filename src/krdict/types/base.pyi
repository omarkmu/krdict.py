from collections.abc import Mapping
from enum import Enum
from typing import Optional, TypeVar, Union, overload

T = TypeVar('T')
EnumType = TypeVar('EnumType', bound=EnumBase)

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

class EnumProxyBase:
    __populated__: bool
    def __init__(self, populate: bool): ...
