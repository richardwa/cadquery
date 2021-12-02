import cadquery as cq
from cqextension.monkey_patch import seamSelector
from slicer.slice import setSlicerSettings
import math

# base shape
size = (56, 25, 13)
p = cq.Workplane().box(*size).edges("|Z").fillet(10)

# add carbon fiber rod holes
rod_offset = 3
rod_od = 12.5
p = p.faces(">Z").workplane().rect(40, rod_offset * 2, forConstruction=True)\
    .vertices(">Y").hole(rod_od)

# add screw holes and nut insert
screw_pos = p.faces(">Y").workplane().rect(20, 4).vertices("<Z")
nut_insert = screw_pos.box(3, 5, 3, combine=False).translate((0, -10, 0))
p = screw_pos.hole(3, 10).cut(nut_insert)

# create bearing bevel
bearing_od = 15
bevel_angle = 100
bevel_x = (bearing_od / 2) / math.sin(bevel_angle / 2 * math.pi / 180)
bevel_y = (bearing_od / 2) / math.cos(bevel_angle / 2 * math.pi / 180)
b = cq.Workplane("YZ") \
    .lineTo(0, bevel_y)\
    .lineTo(bevel_x, 0)\
    .lineTo(0, -bevel_y).close() \
    .extrude(size[0], both=True) \
    .edges("|X and >Y").fillet(6) \
    .translate((0, -size[1]/2, 0))
    
# for checking fit
# cyl = cq.Workplane("YZ").circle(bearing_od/2).extrude(100, both=True).translate((0, -size[1]/2, 0))

# gaps
gap_size = 1.2
g = cq.Workplane().box(40, gap_size, size[2]).translate(
    (0, rod_offset+rod_od/2 - gap_size/2, 0))
g = g.faces(">Y").workplane().rect(gap_size, size[2]).extrude(10)

show_object(p.cut(b).cut(g))  # type: ignore
