from cqextension.monkey_patch import seamSelector
import cadquery as cq

p = cq.Workplane().box(30, 30, 30)
s = p.faces("#Z").box(10, 10, 10, combine=False)
p = (p + s).edges(seamSelector).fillet(1)
show_object(p)
