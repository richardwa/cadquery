$(info file: $(file))
target = $(subst cq_files,target,$(file))
base_file = $(patsubst %.py,%,$(target))
$(info $(base_file))
