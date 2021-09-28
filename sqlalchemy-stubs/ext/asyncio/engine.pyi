from typing import Any
from typing import Callable
from typing import Generator
from typing import MutableMapping
from typing import NoReturn
from typing import Optional
from typing import TypeVar

from .base import ProxyComparable
from .base import StartableContext
from .result import AsyncResult
from .result import AsyncScalarResult
from ..._typing import _ExecuteOptions
from ..._typing import _ExecuteParams
from ...engine import Dialect
from ...engine import Result
from ...engine import ScalarResult
from ...engine import Transaction
from ...engine.base import _ConnectionTypingCommon
from ...engine.base import _EngineTypingCommon
from ...future import Connection
from ...future import Engine
from ...sql import Executable

_TAsyncConnection = TypeVar("_TAsyncConnection", bound=AsyncConnection)
_TAsyncTransaction = TypeVar("_TAsyncTransaction", bound=AsyncTransaction)
_TEngine = TypeVar("_TEngine", bound=AsyncEngine)

def create_async_engine(*arg: Any, **kw: Any) -> AsyncEngine: ...

class AsyncConnectable: ...

class AsyncConnection(
    _ConnectionTypingCommon,
    ProxyComparable,
    StartableContext["AsyncConnection"],
    AsyncConnectable,
):
    # copied from future.Connection via create_proxy_methods
    @property
    def closed(self) -> bool: ...
    @property
    def invalidated(self) -> bool: ...
    dialect: Dialect
    @property
    def default_isolation_level(self) -> Any: ...
    # end copied

    engine: AsyncEngine = ...
    sync_engine: Engine = ...
    sync_connection: Optional[Connection] = ...
    def __init__(
        self,
        async_engine: AsyncEngine,
        sync_connection: Optional[Connection] = ...,
    ) -> None: ...
    async def start(self: _TAsyncConnection) -> _TAsyncConnection: ...
    @property
    def connection(self) -> NoReturn: ...
    async def get_raw_connection(self) -> Any: ...
    @property
    def info(self) -> MutableMapping[Any, Any]: ...
    def begin(self) -> AsyncTransaction: ...
    def begin_nested(self) -> AsyncTransaction: ...
    async def invalidate(self, exception: Optional[Any] = ...) -> None: ...
    async def get_isolation_level(self) -> Any: ...
    async def set_isolation_level(self) -> Any: ...
    def in_transaction(self) -> bool: ...
    def in_nested_transaction(self) -> bool: ...
    def get_transaction(self) -> Optional[AsyncTransaction]: ...
    def get_nested_transaction(self) -> Optional[AsyncTransaction]: ...
    async def execution_options(
        self: _TAsyncConnection, **opt: Any
    ) -> _TAsyncConnection: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
    async def close(self) -> None: ...
    async def exec_driver_sql(
        self,
        statement: str,
        parameters: Optional[_ExecuteParams] = ...,
        execution_options: Optional[_ExecuteOptions] = ...,
    ) -> Result: ...
    async def stream(
        self,
        statement: Executable,
        parameters: Optional[_ExecuteParams] = ...,
        execution_options: Optional[_ExecuteOptions] = ...,
    ) -> AsyncResult: ...
    async def execute(
        self,
        statement: Executable,
        parameters: Optional[_ExecuteParams] = ...,
        execution_options: Optional[_ExecuteOptions] = ...,
    ) -> Result: ...
    async def scalar(
        self,
        statement: Executable,
        parameters: Optional[_ExecuteParams] = ...,
        execution_options: Optional[_ExecuteOptions] = ...,
    ) -> Any: ...
    async def scalars(
        self,
        statement: Executable,
        parameters: Optional[_ExecuteParams] = ...,
        execution_options: Optional[_ExecuteOptions] = ...,
    ) -> ScalarResult: ...
    async def stream_scalars(
        self,
        statement: Executable,
        parameters: Optional[_ExecuteParams] = ...,
        execution_options: Optional[_ExecuteOptions] = ...,
    ) -> AsyncScalarResult: ...
    async def run_sync(
        self, fn: Callable[..., Any], *arg: Any, **kw: Any
    ) -> Any: ...
    def __await__(
        self: _TAsyncConnection,
    ) -> Generator[Any, None, _TAsyncConnection]: ...
    async def __aexit__(
        self, type_: Any, value: Any, traceback: Any
    ) -> None: ...

class AsyncEngine(_EngineTypingCommon, ProxyComparable, AsyncConnectable):
    @property
    def engine(self: _TEngine) -> _TEngine: ...
    class _trans_ctx(StartableContext[AsyncConnection]):
        conn: AsyncConnection = ...
        def __init__(self, conn: AsyncConnection) -> None: ...
        transaction: Any = ...
        async def start(self) -> AsyncConnection: ...
        def __await__(self) -> Generator[Any, None, AsyncConnection]: ...
        async def __aexit__(
            self, type_: Any, value: Any, traceback: Any
        ) -> None: ...
    sync_engine: Engine = ...
    def __init__(self, sync_engine: Engine) -> None: ...
    def begin(self) -> _trans_ctx: ...
    def connect(self) -> AsyncConnection: ...
    async def raw_connection(self) -> Any: ...
    def execution_options(self, **opt: Any) -> AsyncEngine: ...
    async def dispose(self) -> None: ...

class AsyncTransaction(ProxyComparable, StartableContext["AsyncTransaction"]):
    connection: AsyncConnection = ...
    sync_transaction: Optional[Transaction] = ...
    nested: bool = ...
    def __init__(
        self, connection: AsyncConnection, nested: bool = ...
    ) -> None: ...
    @property
    def is_valid(self) -> bool: ...
    @property
    def is_active(self) -> bool: ...
    async def close(self) -> None: ...
    async def rollback(self) -> None: ...
    async def commit(self) -> None: ...
    async def start(self: _TAsyncTransaction) -> _TAsyncTransaction: ...
    async def __aexit__(
        self, type_: Any, value: Any, traceback: Any
    ) -> None: ...
