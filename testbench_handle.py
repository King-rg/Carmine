import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge,Timer
import random

from tb import BRecode_tb

@cocotb.test()
async def BRecode(dut):
    """Testbench for the B-Encode module."""
    # Start a clock on the clk port
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    cocotb.start_soon(BRecode_tb.applyTests(dut))
    await Timer(100, units="ns")  # Run for 100 ns