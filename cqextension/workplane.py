import cadquery as cq

from typing import (
    overload,
    Sequence,
    TypeVar,
    Union,
    Tuple,
    Optional,
    Any,
    Iterable,
    Callable,
    List,
    cast,
    Dict,
)

class Object:
    def __init__(self, **attributes):
        self.__dict__.update(attributes)

class WP(cq.Workplane):
    def union(
        self,
        toUnion,
        clean: bool = True,
        glue: bool = False,
        tol: Optional[float] = None,
    ):
      print(self)
      return super(WP,self).union(toUnion,clean, glue, tol)

