# Load CQGI
import cadquery.cqgi as cqgi
import cadquery as cq
import sys
import os
from slicer.slice import getSliceCmd

cadfile = sys.argv[1]
cadfile_base = os.path.splitext(cadfile)[0].replace("cq_files", "target")
# load the cadquery script
model = cqgi.parse(open(cadfile).read())


# run the script and store the result (from the show_object call in the script)
build_result = model.build()

# test to ensure the process worked.
if build_result.success:
    last = len(build_result.results) - 1
    stl = f"{cadfile_base}.stl"
    shape = build_result.results[last].shape
    cq.exporters.export(shape, stl)
    bat = open(f"{cadfile_base}.slice.bat", "w")
    bat.write(getSliceCmd(shape, stl))

else:
    print(f"BUILD FAILED: {build_result.exception}")
