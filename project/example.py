from cqextension.monkey_patch import *
import cadquery as cq

p = cq.Workplane().box(30, 30, 30)
s = p.faces("#Z").box(10, 10, 10, combine=False)
p = (p + s).edges(SeamSelector()).fillet(1)
show_object(p)
