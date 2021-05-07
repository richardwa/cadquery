from cqextension.monkey_patch import seamSelector
from cq_files.utils import hexGrid
import cadquery as cq
import math

rimDiameter= 68
drainDiameter= 37
meshSize = 8
thickness= 1.2


p = hexGrid(6,1,2, 5,5)
show_object(p)

options = {

}
def showerDrain ( rimDiameter, drainDiameter, meshSize, thickness):
   ringOuter = ring(
    od=rimDiameter,
    id=rimDiameter - t * 2,
    h=t * 2,
    radii= [0, 0, 0, t / 2]
  ).align([0, 0, 1])

   hexMesh = cylinder({ d: rimDiameter - t * 1.8, h: t, $fn: 100 })
    .difference(
      hexTile({
        hexSize: meshSize,
        spacing: t,
        size: [rimDiameter, rimDiameter],
        thickness: t + 1
      }))
    .translate([0, 0, t / 2]);

   drainInnerDiameter = drainDiameter - t * 2;
   braceLen = (rimDiameter - drainDiameter) / 2 + t / 2;
   braceWidth = t * 1.2;
   chamferWidth = t - 0.2;

   crossbrace = cube([braceLen, braceWidth, t])
    .align([1, 1, 1])
    .union(square([chamferWidth, braceWidth])
      .linear_extrude({ height: t, scale: [1, 2.5], center: false })
      .translate([chamferWidth / 2, braceWidth / 2, 0]))
    .translate([drainInnerDiameter / 2, - t / 2, t])
    .rotate([0, 0, 15]); // offset a bit so that the bars don't end on center of hex

   ringInner = ring({
    od: drainDiameter,
    id: drainInnerDiameter,
    h: t * 3,
    $fn: 50,
  }).align([0, 0, 1])
    .translate([0, 0, t * 1.8]);

  return ringOuter.union(
    hexMesh,
    crossbrace.tile_circular({ times: 12 }),
    ringInner
  );


show_object(showerDrain(...options))
