from typing import Any
from typing import Optional

from .. import util
from ..engine import Result

class _SessionClassMethods:
    @classmethod
    def close_all(cls) -> None: ...
    @classmethod
    def identity_key(cls, *args: Any, **kwargs: Any): ...
    @classmethod
    def object_session(cls, instance: Any): ...

class ORMExecuteState(util.MemoizedSlots):
    session: Any = ...
    statement: Any = ...
    parameters: Any = ...
    local_execution_options: Any = ...
    execution_options: Any = ...
    bind_arguments: Any = ...
    def __init__(
        self,
        session: Any,
        statement: Any,
        parameters: Any,
        execution_options: Any,
        bind_arguments: Any,
        compile_state_cls: Any,
        events_todo: Any,
    ) -> None: ...
    def invoke_statement(
        self,
        statement: Optional[Any] = ...,
        params: Optional[Any] = ...,
        execution_options: Optional[Any] = ...,
        bind_arguments: Optional[Any] = ...,
    ): ...
    @property
    def bind_mapper(self): ...
    @property
    def all_mappers(self): ...
    @property
    def is_orm_statement(self): ...
    @property
    def is_select(self): ...
    @property
    def is_insert(self): ...
    @property
    def is_update(self): ...
    @property
    def is_delete(self): ...
    def update_execution_options(self, **opts: Any) -> None: ...
    @property
    def lazy_loaded_from(self): ...
    @property
    def loader_strategy_path(self): ...
    @property
    def is_column_load(self): ...
    @property
    def is_relationship_load(self): ...
    @property
    def load_options(self): ...
    @property
    def update_delete_options(self): ...
    @property
    def user_defined_options(self): ...

class SessionTransaction:
    session: Any = ...
    nested: Any = ...
    def __init__(
        self,
        session: Any,
        parent: Optional[Any] = ...,
        nested: bool = ...,
        autobegin: bool = ...,
    ) -> None: ...
    @property
    def parent(self): ...
    @property
    def is_active(self): ...
    def connection(
        self,
        bindkey: Any,
        execution_options: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def prepare(self) -> None: ...
    def commit(self, _to_root: bool = ...): ...
    def rollback(
        self, _capture_exception: bool = ..., _to_root: bool = ...
    ): ...
    def close(self, invalidate: bool = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

class Session(_SessionClassMethods):
    identity_map: Any = ...
    bind: Any = ...
    future: Any = ...
    hash_key: Any = ...
    autoflush: Any = ...
    expire_on_commit: Any = ...
    enable_baked_queries: Any = ...
    autocommit: bool = ...
    twophase: Any = ...
    def __init__(
        self,
        bind: Optional[Any] = ...,
        autoflush: bool = ...,
        future: bool = ...,
        expire_on_commit: bool = ...,
        autocommit: bool = ...,
        twophase: bool = ...,
        binds: Optional[Any] = ...,
        enable_baked_queries: bool = ...,
        info: Optional[Any] = ...,
        query_cls: Optional[Any] = ...,
    ) -> None: ...
    connection_callable: Any = ...
    def __enter__(self): ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    @property
    def transaction(self): ...
    def in_transaction(self): ...
    def in_nested_transaction(self): ...
    def get_transaction(self): ...
    def get_nested_transaction(self): ...
    def info(self): ...
    def begin(
        self,
        subtransactions: bool = ...,
        nested: bool = ...,
        _subtrans: bool = ...,
    ): ...
    def begin_nested(self): ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def prepare(self) -> None: ...
    def connection(
        self,
        bind_arguments: Optional[Any] = ...,
        close_with_result: bool = ...,
        execution_options: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def execute(
        self,
        statement: Any,
        params: Optional[Any] = ...,
        execution_options: Any = ...,
        bind_arguments: Optional[Any] = ...,
        _parent_execute_state: Optional[Any] = ...,
        _add_event: Optional[Any] = ...,
        **kw: Any,
    ) -> Result: ...
    def scalar(
        self,
        statement: Any,
        params: Optional[Any] = ...,
        execution_options: Any = ...,
        bind_arguments: Optional[Any] = ...,
        **kw: Any,
    ) -> Any: ...
    def close(self) -> None: ...
    def invalidate(self) -> None: ...
    def expunge_all(self) -> None: ...
    def bind_mapper(self, mapper: Any, bind: Any) -> None: ...
    def bind_table(self, table: Any, bind: Any) -> None: ...
    def get_bind(
        self,
        mapper: Optional[Any] = ...,
        clause: Optional[Any] = ...,
        bind: Optional[Any] = ...,
        _sa_skip_events: Optional[Any] = ...,
        _sa_skip_for_implicit_returning: bool = ...,
    ): ...
    def query(self, *entities: Any, **kwargs: Any): ...
    @property
    def no_autoflush(self) -> None: ...
    def refresh(
        self,
        instance: Any,
        attribute_names: Optional[Any] = ...,
        with_for_update: Optional[Any] = ...,
    ) -> None: ...
    def expire_all(self) -> None: ...
    def expire(
        self, instance: Any, attribute_names: Optional[Any] = ...
    ) -> None: ...
    def expunge(self, instance: Any) -> None: ...
    def add(self, instance: Any, _warn: bool = ...) -> None: ...
    def add_all(self, instances: Any) -> None: ...
    def delete(self, instance: Any) -> None: ...
    def get(
        self,
        entity: Any,
        ident: Any,
        options: Optional[Any] = ...,
        populate_existing: bool = ...,
        with_for_update: Optional[Any] = ...,
        identity_token: Optional[Any] = ...,
    ): ...
    def merge(self, instance: Any, load: bool = ...): ...
    def enable_relationship_loading(self, obj: Any) -> None: ...
    def __contains__(self, instance: Any): ...
    def __iter__(self) -> Any: ...
    def flush(self, objects: Optional[Any] = ...) -> None: ...
    def bulk_save_objects(
        self,
        objects: Any,
        return_defaults: bool = ...,
        update_changed_only: bool = ...,
        preserve_order: bool = ...,
    ): ...
    def bulk_insert_mappings(
        self,
        mapper: Any,
        mappings: Any,
        return_defaults: bool = ...,
        render_nulls: bool = ...,
    ) -> None: ...
    def bulk_update_mappings(self, mapper: Any, mappings: Any) -> None: ...
    def is_modified(self, instance: Any, include_collections: bool = ...): ...
    @property
    def is_active(self): ...
    @property
    def dirty(self): ...
    @property
    def deleted(self): ...
    @property
    def new(self): ...

class sessionmaker(_SessionClassMethods):
    kw: Any = ...
    class_: Any = ...
    def __init__(
        self,
        bind: Optional[Any] = ...,
        class_: Any = ...,
        autoflush: bool = ...,
        autocommit: bool = ...,
        expire_on_commit: bool = ...,
        info: Optional[Any] = ...,
        **kw: Any,
    ) -> None: ...
    def begin(self): ...
    def __call__(self, **local_kw: Any): ...
    def configure(self, **new_kw: Any) -> None: ...

def close_all_sessions() -> Any: ...
def make_transient(instance: object) -> Any: ...
def make_transient_to_detached(instance: object) -> Any: ...
def object_session(instance: object) -> Any: ...
