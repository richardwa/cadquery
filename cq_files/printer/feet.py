import cadquery as cq
from cqextension.monkey_patch import seamSelector
from slicer.slice import setSlicerSettings

p = cq.Workplane().box(24, 24, 6).edges("|Z").fillet(2)
s = p.faces(">Z").rect(20, 20).extrude(-2, combine=False)
p = p.cut(s)
cboreDepth = 4
p = p.faces("<Z").workplane().cboreHole(5.5, 12, cboreDepth)

# add bridge layer
p = p.faces("<Z").workplane(offset=-cboreDepth).box(13, 13, .2)
show_object(p)
setSlicerSettings(p, duplicate=4)
