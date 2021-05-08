# Load CQGI
import cadquery.cqgi as cqgi
import cadquery as cq
import sys, os
from slicer.slice import getSlicerSettings

cadfile = sys.argv[1]
cadfile_base = os.path.splitext(cadfile)[0].replace("cq_files","target")
# load the cadquery script
model = cqgi.parse(open(cadfile).read())


# run the script and store the result (from the show_object call in the script)
build_result = model.build()

# get slicer settings
print("settings", getSlicerSettings())

# test to ensure the process worked.
if build_result.success:
    if (len(build_result.results) == 1):
      cq.exporters.export(build_result.results[0].shape, f"{cadfile_base}.stl")
    else:
        # loop through all the shapes returned and export to STL
        for i, result in enumerate(build_result.results):
            cq.exporters.export(result.shape, f"{cadfile_base}_{i}.stl")
else:
    print(f"BUILD FAILED: {build_result.exception}")