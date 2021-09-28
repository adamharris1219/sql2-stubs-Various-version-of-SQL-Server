from typing import Any
from typing import Optional

from .pymysql import MySQLDialect_pymysql as MySQLDialect_pymysql
from ...engine import AdaptedConnection
from ... import pool as pool
from ... import util as util
from ...util.concurrency import await_fallback as await_fallback
from ...util.concurrency import await_only as await_only

class AsyncAdapt_aiomysql_cursor:
    server_side: bool = ...
    await_: Any = ...
    def __init__(self, adapt_connection: Any) -> None: ...
    @property
    def description(self): ...
    @property
    def rowcount(self): ...
    @property
    def arraysize(self): ...
    @arraysize.setter
    def arraysize(self, value: Any) -> None: ...
    @property
    def lastrowid(self): ...
    def close(self) -> None: ...
    def execute(self, operation: Any, parameters: Optional[Any] = ...): ...
    def executemany(self, operation: Any, seq_of_parameters: Any): ...
    def setinputsizes(self, *inputsizes: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def fetchone(self): ...
    def fetchmany(self, size: Optional[Any] = ...): ...
    def fetchall(self): ...

class AsyncAdapt_aiomysql_ss_cursor(AsyncAdapt_aiomysql_cursor):
    server_side: bool = ...
    await_: Any = ...
    def __init__(self, adapt_connection: Any) -> None: ...
    def close(self) -> None: ...
    def fetchone(self): ...
    def fetchmany(self, size: Optional[Any] = ...): ...
    def fetchall(self): ...

class AsyncAdapt_aiomysql_connection(AdaptedConnection):
    await_: Any = ...
    dbapi: Any = ...
    def __init__(self, dbapi: Any, connection: Any) -> None: ...
    def ping(self, reconnect: Any): ...
    def character_set_name(self): ...
    def autocommit(self, value: Any) -> None: ...
    def cursor(self, server_side: bool = ...): ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def close(self) -> None: ...

class AsyncAdaptFallback_aiomysql_connection(AsyncAdapt_aiomysql_connection):
    await_: Any = ...

class AsyncAdapt_aiomysql_dbapi:
    aiomysql: Any = ...
    pymysql: Any = ...
    paramstyle: str = ...
    def __init__(self, aiomysql: Any, pymysql: Any) -> None: ...
    def connect(self, *arg: Any, **kw: Any): ...

class MySQLDialect_aiomysql(MySQLDialect_pymysql):
    driver: str = ...
    supports_server_side_cursors: bool = ...
    is_async: bool = ...
    @classmethod
    def dbapi(cls): ...
    @classmethod
    def get_pool_class(cls, url: Any): ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def get_driver_connection(self, connection: Any) -> Any:

dialect = MySQLDialect_aiomysql
