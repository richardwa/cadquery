import cadquery as cq
from cqextension.cq_print import *
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
from OCP.TopTools import TopTools_IndexedDataMapOfShapeListOfShape, TopTools_ListOfShape
from OCP.BRepAlgoAPI import (
    BRepAlgoAPI_Common,
    BRepAlgoAPI_Fuse,
    BRepAlgoAPI_Cut,
    BRepAlgoAPI_BooleanOperation,
    BRepAlgoAPI_Splitter,
    BRepAlgoAPI_BuilderAlgo,
)

bool_op_section_edges = []
original_bool_op = cq.Shape._bool_op


def _bool_op(
    self,
    args: Iterable["Shape"],
    tools: Iterable["Shape"],
    op: Union[BRepAlgoAPI_BooleanOperation, BRepAlgoAPI_Splitter],
) -> "Shape":
    ret = original_bool_op(self, args, tools, op)

    print('injected')
    bool_op_section_edges.clear()
    for a in op.SectionEdges():
        bool_op_section_edges.append(a)
    # print(bool_op_section_edges)

    return ret


cq.Shape._bool_op = _bool_op


class SeamSelector(cq.Selector):
    def str_edge(self, obj):
        s = []
        s.append(obj.geomType())
        s.append(str(obj.startPoint().toTuple()))
        s.append(str(obj.endPoint().toTuple()))
        if obj_type.upper() == "CIRCLE":
            circle = obj._geomAdaptor().Circle()
            radius = circle.Radius()
            centre = circle.Location()
            s.append(str(cq.Vector(centre).toTuple()))
            s.append(str(radius))
        return "".join(s)

    def filter(self, objectList):
        edges = set()
        for e in bool_op_section_edges:
            edge = cq.Shape.cast(e)
            # print("edge1", self.str_edge(edge))
            edges.add(self.str_edge(edge))
        r = []

        for o in objectList:
            # print("edge2", self.str_edge(o))
            if self.str_edge(o) in edges:
                r.append(o)
        return r
