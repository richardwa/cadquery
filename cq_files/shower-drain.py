from cqextension.monkey_patch import seamSelector
from cq_files.utils import hexGrid
import cadquery as cq
import math

rimDiameter = 68
drainDiameter = 37
meshSize = 8
t = 1.2

holes = math.ceil(rimDiameter/meshSize)
grate = cq.Workplane().circle(rimDiameter/2-.1).extrude(t).cut(
    hexGrid(meshSize, t, t,  holes, holes))

ring = cq.Workplane().circle(rimDiameter/2).circle(
    rimDiameter/2-t).extrude(t*2)
comb = ring.union(grate)

crossbrace = grate.faces(">Z").workplane().center(-t/2, drainDiameter/2-t)\
    .rect(t, (rimDiameter-drainDiameter)/2 - .1, centered=False).extrude(t, combine=False)
crossbrace = crossbrace.faces("<Y").workplane().polyline(
  ((0,0),(t,0),(2*t, t),(-t,t),(0,0))).close().extrude(-t)

num_braces = 12
for i in range(num_braces):
    comb.add(crossbrace.rotate((0, 0, 0), (0, 0, 1), 15+360/num_braces*i))


drain = ring.faces(">Z").workplane().circle(
    drainDiameter/2).circle(drainDiameter/2-t).extrude(t*3)

comb = comb.union(drain)
show_object(comb)
