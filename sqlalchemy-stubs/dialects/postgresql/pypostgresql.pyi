from typing import Any

from .base import PGDialect as PGDialect
from .base import PGExecutionContext as PGExecutionContext
from ... import processors as processors
from ... import types as sqltypes
from ... import util as util

class PGNumeric(sqltypes.Numeric):
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class PGExecutionContext_pypostgresql(PGExecutionContext): ...

class PGDialect_pypostgresql(PGDialect):
    driver: str = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    description_encoding: Any = ...
    default_paramstyle: str = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    execution_ctx_cls: Any = ...
    colspecs: Any = ...
    @classmethod
    def dbapi(cls): ...
    def dbapi_exception_translation_map(self): ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...

dialect = PGDialect_pypostgresql
