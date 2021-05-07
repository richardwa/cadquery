from cqextension.monkey_patch import seamSelector
from cq_files.utils import *
import cadquery as cq
import math


p = hexGrid(6, .1, 1, 5, 5)

ring = cq.Workplane().circle(10).circle(8).extrude(2)
show_object(ring+p)
