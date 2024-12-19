# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += src/BRecode.v

# MODULE is the basename of the Python test file
MODULE = testbench_handle

BRecode: 
	$(MAKE) sim MODULE=testbench_handle TESTCASE=BRecode TOPLEVEL=BRecode

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim