import cadquery as cq
from cqextension.monkey_patch import seamSelector
from slicer.slice import setSlicerSettings

p = cq.Workplane().box(40, 60, 4).edges("|Z and >X and <Y").chamfer(20)
p = p.faces(">Z").workplane().pushPoints([
    (-10, 20), (-10, 0), (-10, -20), (10, 20)
]).hole(5)
p = p.pushPoints([(7, -10)]).hole(3)
show_object(p)
