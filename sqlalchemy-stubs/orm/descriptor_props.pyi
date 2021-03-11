from typing import Any
from typing import Optional
from typing import TypeVar

from . import attributes as attributes
from . import util as orm_util
from .interfaces import MapperProperty as MapperProperty
from .interfaces import PropComparator as PropComparator
from .. import event as event
from .. import schema as schema
from .. import sql as sql
from .. import util as util
from ..sql import expression as expression

_T = TypeVar("_T")

class DescriptorProperty(MapperProperty[_T]):
    doc: Any = ...
    uses_objects: bool = ...
    key: Any = ...
    descriptor: Any = ...
    def instrument_class(self, mapper: Any): ...

class CompositeProperty(DescriptorProperty[_T]):
    attrs: Any = ...
    composite_class: Any = ...
    active_history: Any = ...
    deferred: Any = ...
    group: Any = ...
    comparator_factory: Any = ...
    info: Any = ...
    def __init__(self, class_: Any, *attrs: Any, **kwargs: Any) -> None: ...
    def instrument_class(self, mapper: Any) -> None: ...
    def do_init(self) -> None: ...
    def props(self): ...
    @property
    def columns(self): ...
    def get_history(self, state: Any, dict_: Any, passive: Any = ...): ...
    class CompositeBundle(orm_util.Bundle):
        property: Any = ...
        def __init__(self, property_: Any, expr: Any) -> None: ...
        def create_row_processor(
            self, query: Any, procs: Any, labels: Any
        ): ...
    class Comparator(PropComparator):
        __hash__: Any = ...
        def clauses(self): ...
        def __clause_element__(self): ...
        def expression(self): ...
        def __eq__(self, other: Any) -> Any: ...
        def __ne__(self, other: Any) -> Any: ...

class ConcreteInheritedProperty(DescriptorProperty[_T]):
    descriptor: Any = ...
    def __init__(self): ...

class SynonymProperty(DescriptorProperty[_T]):
    name: Any = ...
    map_column: Any = ...
    descriptor: Any = ...
    comparator_factory: Any = ...
    doc: Any = ...
    info: Any = ...
    def __init__(
        self,
        name: Any,
        map_column: Optional[Any] = ...,
        descriptor: Optional[Any] = ...,
        comparator_factory: Optional[Any] = ...,
        doc: Optional[Any] = ...,
        info: Optional[Any] = ...,
    ) -> None: ...
    @property
    def uses_objects(self): ...
    def get_history(self, *arg: Any, **kw: Any): ...
    parent: Any = ...
    def set_parent(self, parent: Any, init: Any) -> None: ...
