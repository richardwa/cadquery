from cqextension.monkey_patch import seamSelector
from cq_files.utils import *
from slicer.slice import setSlicerSettings
import cadquery as cq
import math


p = hexGrid(6, .1, 1, 5, 5)

ring = cq.Workplane().circle(10).circle(8).extrude(2)
r = ring+p
show_object(r)
setSlicerSettings(r, fan_always_on=True)
