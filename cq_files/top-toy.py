from cqextension.monkey_patch import seamSelector
from cq_files.utils import hexGrid
from slicer.slice import setSlicerSettings
import cadquery as cq
import math

r = 10
h = 10
p = cq.Workplane(inPlane="XZ").spline([(0, h), (r, 0)], [
    (-1, -1), (0, -1)]).lineTo(0, 0).close().revolve()
p = p.faces("<Z").workplane().hole(3, h/2)
show_object(p)