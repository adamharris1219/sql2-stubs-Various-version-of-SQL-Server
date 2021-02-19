from typing import Any
from typing import Optional

from .. import util as util
from ..orm import attributes as attributes
from ..orm import interfaces as interfaces
from ..sql import elements as elements

HYBRID_METHOD: Any
HYBRID_PROPERTY: Any

class hybrid_method(interfaces.InspectionAttrInfo):
    is_attribute: bool = ...
    extension_type: Any = ...
    func: Any = ...
    def __init__(self, func: Any, expr: Optional[Any] = ...) -> None: ...
    def __get__(self, instance: Any, owner: Any): ...
    expr: Any = ...
    def expression(self, expr: Any): ...

class hybrid_property(interfaces.InspectionAttrInfo):
    is_attribute: bool = ...
    extension_type: Any = ...
    fget: Any = ...
    fset: Any = ...
    fdel: Any = ...
    expr: Any = ...
    custom_comparator: Any = ...
    update_expr: Any = ...
    def __init__(
        self,
        fget: Any,
        fset: Optional[Any] = ...,
        fdel: Optional[Any] = ...,
        expr: Optional[Any] = ...,
        custom_comparator: Optional[Any] = ...,
        update_expr: Optional[Any] = ...,
    ) -> None: ...
    def __get__(self, instance: Any, owner: Any): ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def __delete__(self, instance: Any) -> None: ...
    @property
    def overrides(self): ...
    def getter(self, fget: Any): ...
    def setter(self, fset: Any): ...
    def deleter(self, fdel: Any): ...
    def expression(self, expr: Any): ...
    def comparator(self, comparator: Any): ...
    def update_expression(self, meth: Any): ...

class Comparator(interfaces.PropComparator):
    property: Any = ...
    expression: Any = ...
    def __init__(self, expression: Any) -> None: ...
    def __clause_element__(self): ...
    def adapt_to_entity(self, adapt_to_entity: Any): ...

class ExprComparator(Comparator):
    cls: Any = ...
    expression: Any = ...
    hybrid: Any = ...
    def __init__(self, cls: Any, expression: Any, hybrid: Any) -> None: ...
    def __getattr__(self, key: Any): ...
    @property
    def info(self): ...
    @property
    def property(self): ...
    def operate(self, op: Any, *other: Any, **kwargs: Any): ...
    def reverse_operate(self, op: Any, other: Any, **kwargs: Any): ...
