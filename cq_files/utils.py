import cadquery as cq
import math

def hexGrid(hexSize: float, spacing: float, h: float, xCount: int, yCount: int):
    hexSize_1 = hexSize * 2 / math.sqrt(3)
    total = hexSize + spacing
    total_1 = total * math.sqrt(3)
    param = dict(xSpacing=total_1, ySpacing=total,
                 xCount=math.ceil(xCount/2), yCount=yCount)
    p = cq.Workplane().rarray(**param).polygon(6, hexSize_1).extrude(h)
    q = cq.Workplane().center(total_1/2, total/2)\
        .rarray(**param).polygon(6, hexSize_1).extrude(h)
    return p+q

