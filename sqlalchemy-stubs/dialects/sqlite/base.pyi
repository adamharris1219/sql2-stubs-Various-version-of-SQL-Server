from typing import Any
from typing import Optional

from .json import JSON as JSON
from .json import JSONIndexType as JSONIndexType
from .json import JSONPathType as JSONPathType
from ... import exc as exc
from ... import processors as processors
from ... import sql as sql
from ... import types as sqltypes
from ... import util as util
from ...engine import default as default
from ...engine import reflection as reflection
from ...sql import coercions as coercions
from ...sql import ColumnElement as ColumnElement
from ...sql import compiler as compiler
from ...sql import elements as elements
from ...sql import roles as roles
from ...sql import schema as schema
from ...types import BLOB as BLOB
from ...types import BOOLEAN as BOOLEAN
from ...types import CHAR as CHAR
from ...types import DECIMAL as DECIMAL
from ...types import FLOAT as FLOAT
from ...types import INTEGER as INTEGER
from ...types import NUMERIC as NUMERIC
from ...types import REAL as REAL
from ...types import SMALLINT as SMALLINT
from ...types import TEXT as TEXT
from ...types import TIMESTAMP as TIMESTAMP
from ...types import VARCHAR as VARCHAR

class _SQliteJson(JSON):
    def result_processor(self, dialect: Any, coltype: Any): ...

class _DateTimeMixin:
    def __init__(
        self,
        storage_format: Optional[Any] = ...,
        regexp: Optional[Any] = ...,
        **kw: Any,
    ) -> None: ...
    @property
    def format_is_text_affinity(self): ...
    def adapt(self, cls: Any, **kw: Any): ...
    def literal_processor(self, dialect: Any): ...

class DATETIME(_DateTimeMixin, sqltypes.DateTime):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class DATE(_DateTimeMixin, sqltypes.Date):
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class TIME(_DateTimeMixin, sqltypes.Time):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

colspecs: Any
ischema_names: Any

class SQLiteCompiler(compiler.SQLCompiler):
    extract_map: Any = ...
    def visit_now_func(self, fn: Any, **kw: Any): ...
    def visit_localtimestamp_func(self, func: Any, **kw: Any): ...
    def visit_true(self, expr: Any, **kw: Any): ...
    def visit_false(self, expr: Any, **kw: Any): ...
    def visit_char_length_func(self, fn: Any, **kw: Any): ...
    def visit_cast(self, cast: Any, **kwargs: Any): ...
    def visit_extract(self, extract: Any, **kw: Any): ...
    def limit_clause(self, select: Any, **kw: Any): ...
    def for_update_clause(self, select: Any, **kw: Any): ...
    def visit_is_distinct_from_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_is_not_distinct_from_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_json_getitem_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_json_path_getitem_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_empty_set_expr(self, element_types: Any): ...
    def visit_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_not_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_on_conflict_do_nothing(self, on_conflict: Any, **kw: Any): ...
    def visit_on_conflict_do_update(self, on_conflict: Any, **kw: Any): ...

class SQLiteDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column: Any, **kwargs: Any): ...
    def visit_primary_key_constraint(self, constraint: Any): ...
    def visit_unique_constraint(self, constraint: Any): ...
    def visit_check_constraint(self, constraint: Any): ...
    def visit_column_check_constraint(self, constraint: Any): ...
    def visit_foreign_key_constraint(self, constraint: Any): ...
    def define_constraint_remote_table(
        self, constraint: Any, table: Any, preparer: Any
    ): ...
    def visit_create_index(
        self,
        create: Any,
        include_schema: bool = ...,
        include_table_schema: bool = ...,
    ): ...
    def post_create_table(self, table: Any): ...

class SQLiteTypeCompiler(compiler.GenericTypeCompiler):
    def visit_large_binary(self, type_: Any, **kw: Any): ...
    def visit_DATETIME(self, type_: Any, **kw: Any): ...
    def visit_DATE(self, type_: Any, **kw: Any): ...
    def visit_TIME(self, type_: Any, **kw: Any): ...
    def visit_JSON(self, type_: Any, **kw: Any): ...

class SQLiteIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any = ...

class SQLiteExecutionContext(default.DefaultExecutionContext): ...

class SQLiteDialect(default.DefaultDialect):
    name: str = ...
    supports_alter: bool = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    supports_default_values: bool = ...
    supports_empty_insert: bool = ...
    supports_cast: bool = ...
    supports_multivalues_insert: bool = ...
    tuple_in_values: bool = ...
    default_paramstyle: str = ...
    execution_ctx_cls: Any = ...
    statement_compiler: Any = ...
    ddl_compiler: Any = ...
    type_compiler: Any = ...
    preparer: Any = ...
    ischema_names: Any = ...
    colspecs: Any = ...
    isolation_level: Any = ...
    construct_arguments: Any = ...
    native_datetime: Any = ...
    def __init__(
        self,
        isolation_level: Optional[Any] = ...,
        native_datetime: bool = ...,
        json_serializer: Optional[Any] = ...,
        json_deserializer: Optional[Any] = ...,
        _json_serializer: Optional[Any] = ...,
        _json_deserializer: Optional[Any] = ...,
        **kwargs: Any,
    ) -> None: ...
    def set_isolation_level(self, connection: Any, level: Any) -> None: ...
    def get_isolation_level(self, connection: Any): ...
    def on_connect(self): ...
    def get_schema_names(self, connection: Any, **kw: Any): ...
    def get_table_names(
        self, connection: Any, schema: Optional[Any] = ..., **kw: Any
    ): ...
    def get_temp_table_names(self, connection: Any, **kw: Any): ...
    def get_temp_view_names(self, connection: Any, **kw: Any): ...
    def has_table(
        self, connection: Any, table_name: Any, schema: Optional[Any] = ...
    ): ...
    def get_view_names(
        self, connection: Any, schema: Optional[Any] = ..., **kw: Any
    ): ...
    def get_view_definition(
        self,
        connection: Any,
        view_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_columns(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_pk_constraint(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_foreign_keys(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_unique_constraints(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_check_constraints(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_indexes(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
