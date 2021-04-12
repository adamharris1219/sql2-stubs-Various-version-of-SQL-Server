from typing import Any
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import TypeVar

from ...engine.result import FilterResult
from ...engine.result import FrozenResult
from ...engine.result import MergedResult
from ...engine.result import Result
from ...engine.result import RMKeyView
from ...engine.result import Row

_TAsyncResult = TypeVar("_TAsyncResult", bound=AsyncResult)
_TAsyncScalarResult = TypeVar("_TAsyncScalarResult", bound=AsyncScalarResult)
_TAsyncMappingResult = TypeVar(
    "_TAsyncMappingResult", bound=AsyncMappingResult
)

class AsyncCommon(FilterResult):
    async def close(self) -> None: ...

class AsyncResult(AsyncCommon):
    def __init__(self, real_result: Result) -> None: ...
    def keys(self) -> RMKeyView: ...
    def unique(
        self: _TAsyncResult, strategy: Optional[Any] = ...
    ) -> _TAsyncResult: ...
    def columns(
        self: _TAsyncResult, *col_expressions: Any
    ) -> _TAsyncResult: ...
    async def partitions(
        self, size: Optional[int] = ...
    ) -> Iterator[List[Any]]: ...
    async def fetchone(self) -> Optional[Row]: ...
    async def fetchmany(self, size: Optional[int] = ...) -> List[Row]: ...
    async def all(self) -> List[Row]: ...
    def __aiter__(self: _TAsyncResult) -> _TAsyncResult: ...
    async def __anext__(self) -> Row: ...
    async def first(self) -> Optional[Row]: ...
    async def one_or_none(self) -> Optional[Row]: ...
    async def scalar_one(self) -> Any: ...
    async def scalar_one_or_none(self) -> Optional[Any]: ...
    async def one(self) -> Row: ...
    async def scalar(self) -> Optional[Any]: ...
    async def freeze(self) -> FrozenResult: ...
    def merge(self, *others: Any) -> MergedResult: ...
    def scalars(self, index: int = ...) -> AsyncScalarResult: ...
    def mappings(self) -> AsyncMappingResult: ...

class AsyncScalarResult(AsyncCommon):
    def __init__(self, real_result: AsyncResult, index: Any) -> None: ...
    def unique(
        self: _TAsyncScalarResult, strategy: Optional[Any] = ...
    ) -> _TAsyncScalarResult: ...
    async def partitions(
        self, size: Optional[int] = ...
    ) -> Iterator[List[Any]]: ...
    async def fetchall(self) -> List[Any]: ...
    async def fetchmany(self, size: Optional[int] = ...) -> List[Any]: ...
    async def all(self) -> List[Any]: ...
    def __aiter__(self: _TAsyncScalarResult) -> _TAsyncScalarResult: ...
    async def __anext__(self) -> Any: ...
    async def first(self) -> Optional[Any]: ...
    async def one_or_none(self) -> Optional[Any]: ...
    async def one(self) -> Any: ...

class AsyncMappingResult(AsyncCommon):
    def __init__(self, result: AsyncResult) -> None: ...
    def keys(self) -> RMKeyView: ...
    def unique(
        self: _TAsyncMappingResult, strategy: Optional[Any] = ...
    ) -> _TAsyncMappingResult: ...
    def columns(
        self: _TAsyncMappingResult, *col_expressions: Any
    ) -> _TAsyncMappingResult: ...
    async def partitions(
        self, size: Optional[int] = ...
    ) -> Iterator[List[Mapping[Any, Any]]]: ...
    async def fetchall(self) -> List[Mapping[Any, Any]]: ...
    async def fetchone(self) -> Optional[Mapping[Any, Any]]: ...
    async def fetchmany(
        self, size: Optional[int] = ...
    ) -> List[Mapping[Any, Any]]: ...
    async def all(self) -> List[Mapping[Any, Any]]: ...
    def __aiter__(self: _TAsyncMappingResult) -> _TAsyncMappingResult: ...
    async def __anext__(self) -> Mapping[Any, Any]: ...
    async def first(self) -> Optional[Mapping[Any, Any]]: ...
    async def one_or_none(self) -> Optional[Mapping[Any, Any]]: ...
    async def one(self) -> Mapping[Any, Any]: ...
