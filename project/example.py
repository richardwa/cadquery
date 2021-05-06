from cqextension.monkey_patch import *
from cqextension.selectors import *
import cadquery as cq

p = cq.Workplane().box(20, 20, 20)
s = p.faces(">Z").box(10, 10, 10, combine=False)
p = p+s
p = p.edges(SeamSelector()).fillet(1)
show_object(p)
