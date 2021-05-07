$(info file: $(file))
target = $(subst cq_files,target,$(file))
base_file = $(patsubst %.py,%,$(target))
$(info base: $(base_file))

$(base_file).stl:$(file)
	python -m build $(file)

stl: $(base_file).stl

$(base_file).gcode:$(base_file).stl
	python -m slicer.slice $(base_file).stl

gcode: $(base_file).gcode

$(base_file).upload:$(base_file).gcode
	curl.exe -k \
		-H "X-Api-Key: E01B67DAC70E45FB87F33CE3CC0CF803" \
		-F "select=false" \
		-F "print=false" \
		-F "file=@$(base_file).gcode" \
		http://octopi/api/files/local
	touch $(base_file).upload

upload: $(base_file).upload

all: stl gcode upload