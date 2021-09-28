from typing import Any
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Pattern
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from . import base
from . import interfaces
from .cursor import CursorFetchStrategy
from .url import URL
from .. import pool
from .. import util
from .._typing import _ExecuteOptions
from .._typing import _TypeToInstance
from ..sql import compiler
from ..sql.type_api import TypeEngine
from ..util import langhelpers

_T = TypeVar("_T")

AUTOCOMMIT_REGEXP: Pattern[str]
SERVER_SIDE_CURSOR_RE: Pattern[str]
CACHE_HIT: langhelpers._symbol
CACHE_MISS: langhelpers._symbol
CACHING_DISABLED: langhelpers._symbol
NO_CACHE_KEY: langhelpers._symbol

class DefaultDialect(interfaces.Dialect):
    type_compiler: _TypeToInstance[compiler.GenericTypeCompiler] = ...
    execution_ctx_cls: Type[DefaultExecutionContext] = ...
    supports_alter: bool = ...
    use_setinputsizes: bool = ...
    default_sequence_base: int = ...
    execute_sequence_format: Union[
        Type[Tuple[Any, ...]], Type[List[Any]]
    ] = ...
    supports_views: bool = ...
    supports_sequences: bool = ...
    sequences_optional: bool = ...
    preexecute_autoincrement_sequences: bool = ...
    postfetch_lastrowid: bool = ...
    implicit_returning: bool = ...
    full_returning: bool = ...
    insert_executemany_returning: bool = ...
    cte_follows_insert: bool = ...
    supports_native_enum: bool = ...
    supports_native_boolean: bool = ...
    non_native_boolean_check_constraint: bool = ...
    supports_simple_order_by_label: bool = ...
    tuple_in_values: bool = ...
    connection_characteristics: util.immutabledict[str, Any] = ...
    engine_config_types: util.immutabledict[str, Any] = ...
    supports_native_decimal: bool = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    returns_unicode_strings: langhelpers._symbol = ...
    description_encoding: Optional[str] = ...
    name: str = ...
    max_identifier_length: int = ...
    isolation_level: Optional[Any] = ...
    max_index_name_length: Optional[int] = ...
    max_constraint_name_length: Optional[int] = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    colspecs: Dict[Type[TypeEngine[Any]], Type[TypeEngine[Any]]] = ...
    default_paramstyle: str = ...
    supports_default_values: bool = ...
    supports_empty_insert: bool = ...
    supports_multivalues_insert: bool = ...
    supports_is_distinct_from: bool = ...
    supports_server_side_cursors: bool = ...
    server_side_cursors: bool = ...
    supports_for_update_of: bool = ...
    server_version_info: Optional[Tuple[Any, ...]] = ...
    default_schema_name: Optional[str] = ...
    construct_arguments: Any = ...
    requires_name_normalize: bool = ...
    reflection_options: Tuple[Any, ...] = ...
    dbapi_exception_translation_map: util.immutabledict[str, str] = ...
    is_async: bool = ...
    CACHE_HIT: langhelpers._symbol = ...
    CACHE_MISS: langhelpers._symbol = ...
    CACHING_DISABLED: langhelpers._symbol = ...
    NO_CACHE_KEY: langhelpers._symbol = ...
    convert_unicode: bool = ...
    encoding: str = ...
    positional: bool = ...
    dbapi: Any = ...
    paramstyle: str = ...
    case_sensitive: bool = ...
    label_length: Optional[int] = ...
    compiler_linting: int = ...
    def __init__(
        self,
        convert_unicode: bool = ...,
        encoding: str = ...,
        paramstyle: Optional[str] = ...,
        dbapi: Optional[Any] = ...,
        implicit_returning: Optional[Any] = ...,
        case_sensitive: bool = ...,
        supports_native_boolean: Optional[Any] = ...,
        max_identifier_length: Optional[Any] = ...,
        label_length: Optional[Any] = ...,
        compiler_linting: langhelpers._symbol = ...,
        server_side_cursors: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    @property
    def dialect_description(self) -> str: ...
    @property
    def supports_sane_rowcount_returning(self) -> bool: ...
    @classmethod
    def get_pool_class(cls, url: URL) -> Type[pool.Pool]: ...
    def get_dialect_pool_class(self, url: URL) -> Type[pool.Pool]: ...
    @classmethod
    def load_provisioning(cls) -> None: ...
    def initialize(self, connection: base.Connection) -> None: ...
    def on_connect(self) -> Optional[interfaces._OnConnect]: ...
    def get_default_isolation_level(
        self, dbapi_conn: interfaces._DBAPIConnection
    ) -> Any: ...
    def type_descriptor(self, typeobj: Type[TypeEngine[Any]]) -> Any: ...  # type: ignore[override]
    def has_index(
        self,
        connection: base.Connection,
        table_name: str,
        index_name: str,
        schema: Optional[str] = ...,
    ) -> bool: ...
    def validate_identifier(self, ident: Any) -> None: ...
    def connect(
        self, *cargs: Any, **cparams: Any
    ) -> interfaces._DBAPIConnection: ...
    def create_connect_args(
        self, url: Any
    ) -> Tuple[Sequence[Any], Mapping[str, Any]]: ...
    def set_engine_execution_options(self, engine: Any, opts: Any) -> None: ...
    def set_connection_execution_options(
        self, connection: Any, opts: Any
    ) -> None: ...
    def do_begin(
        self, dbapi_connection: interfaces._DBAPIConnection
    ) -> None: ...
    def do_rollback(
        self, dbapi_connection: interfaces._DBAPIConnection
    ) -> None: ...
    def do_commit(
        self, dbapi_connection: interfaces._DBAPIConnection
    ) -> None: ...
    def do_close(
        self, dbapi_connection: interfaces._DBAPIConnection
    ) -> None: ...
    def do_ping(
        self, dbapi_connection: interfaces._DBAPIConnection
    ) -> bool: ...
    def create_xid(self) -> str: ...
    def do_savepoint(self, connection: base.Connection, name: str) -> None: ...
    def do_rollback_to_savepoint(
        self, connection: base.Connection, name: str
    ) -> None: ...
    def do_release_savepoint(
        self, connection: base.Connection, name: str
    ) -> None: ...
    def do_executemany(
        self,
        cursor: interfaces._DBAPICursor,
        statement: Any,
        parameters: Any,
        context: Optional[interfaces.ExecutionContext] = ...,
    ) -> None: ...
    def do_execute(
        self,
        cursor: interfaces._DBAPICursor,
        statement: Any,
        parameters: Any,
        context: Optional[interfaces.ExecutionContext] = ...,
    ) -> None: ...
    def do_execute_no_params(  # type: ignore[override]
        self,
        cursor: interfaces._DBAPICursor,
        statement: Any,
        context: Optional[interfaces.ExecutionContext] = ...,
    ) -> None: ...
    def is_disconnect(
        self,
        e: Any,
        connection: base.Connection,
        cursor: interfaces._DBAPICursor,
    ) -> bool: ...
    def reset_isolation_level(
        self, dbapi_conn: interfaces._DBAPIConnection
    ) -> None: ...
    def normalize_name(self, name: Optional[str]) -> Optional[str]: ...
    def denormalize_name(self, name: Optional[str]) -> Optional[str]: ...
    def get_driver_connection(
        self, connection: interfaces._DBAPIConnection
    ) -> Any: ...

class StrCompileDialect(DefaultDialect):
    statement_compiler: Type[compiler.StrSQLCompiler] = ...
    ddl_compiler: Type[compiler.DDLCompiler] = ...
    type_compiler: Type[compiler.StrSQLTypeCompiler] = ...
    preparer: Type[compiler.IdentifierPreparer] = ...
    supports_sequences: bool = ...
    sequences_optional: bool = ...
    preexecute_autoincrement_sequences: bool = ...
    implicit_returning: bool = ...
    supports_native_boolean: bool = ...
    supports_simple_order_by_label: bool = ...
    colspecs: Dict[Type[TypeEngine[Any]], Type[TypeEngine[Any]]] = ...

class DefaultExecutionContext(interfaces.ExecutionContext):
    isinsert: bool = ...
    isupdate: bool = ...
    isdelete: bool = ...
    is_crud: bool = ...
    is_text: bool = ...
    isddl: bool = ...
    executemany: bool = ...
    compiled: Optional[compiler.Compiled] = ...
    statement: Optional[str] = ...
    result_column_struct: Any = ...
    returned_default_rows: Any = ...
    execution_options: _ExecuteOptions = ...
    include_set_input_sizes: Any = ...
    exclude_set_input_sizes: Any = ...
    cursor_fetch_strategy: Any = ...
    cache_stats: Any = ...
    invoked_statement: Any = ...
    cache_hit: Any = ...
    @util.memoized_property
    def identifier_preparer(self) -> compiler.IdentifierPreparer: ...
    @util.memoized_property
    def engine(self) -> base.Engine: ...
    @util.memoized_property
    def postfetch_cols(self) -> List[Any]: ...  # type: ignore[override]
    @util.memoized_property
    def prefetch_cols(self) -> List[Any]: ...  # type: ignore[override]
    @util.memoized_property
    def returning_cols(self) -> None: ...
    @util.memoized_property
    def no_parameters(self) -> bool: ...
    @util.memoized_property
    def should_autocommit(self) -> bool: ...  # type: ignore[override]
    @property
    def connection(self) -> base.Connection: ...  # type: ignore[override]
    def should_autocommit_text(self, statement: str) -> bool: ...
    def create_cursor(self) -> interfaces._DBAPICursor: ...
    def create_default_cursor(self) -> interfaces._DBAPICursor: ...
    def create_server_side_cursor(self) -> interfaces._DBAPICursor: ...
    def pre_exec(self) -> None: ...
    def get_out_parameter_values(
        self, names: Sequence[str]
    ) -> Sequence[Any]: ...
    def post_exec(self) -> None: ...
    def get_result_processor(
        self, type_: Any, colname: Any, coltype: Any
    ) -> CursorFetchStrategy: ...
    def get_lastrowid(self) -> Any: ...
    def handle_dbapi_exception(self, e: BaseException) -> None: ...
    @property
    def rowcount(self) -> int: ...
    def supports_sane_rowcount(self) -> bool: ...
    def supports_sane_multi_rowcount(self) -> bool: ...
    @util.memoized_property
    def inserted_primary_key_rows(self) -> Any: ...
    def lastrow_has_defaults(self) -> bool: ...
    current_parameters: Optional[Dict[Any, Any]] = ...
    def get_current_parameters(
        self, isolate_multiinsert_groups: bool = ...
    ) -> Optional[Dict[Any, Any]]: ...
    def get_insert_default(self, column: Any) -> Optional[Any]: ...
    def get_update_default(self, column: Any) -> Optional[Any]: ...
