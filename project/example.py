from cqextension.workplane import *
from cqkit import *

p = WP().box(20, 20, 20)
s = WP().sphere(9).rotate(
    [0, 0, 0], [1, 0, 0], 45).translate([10, 10, 10])
p = p.union(s)
pprint_obj(p.edges())
p = p.edges().fillet(1)
show_object(p)