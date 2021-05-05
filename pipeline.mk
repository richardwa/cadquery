$(info file: $(file))
target = $(subst project,target,$(file))
base_file = $(patsubst %.py,%,$(target))
$(info $(base_file))
