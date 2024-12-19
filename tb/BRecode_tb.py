import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge,Timer
import random

async def readOutputs(dut):
    await RisingEdge(dut.clk)
    print(f"Block One: {dut.blockOne.value}")
    print(f"Block Two: {dut.blockTwo.value}")
    print(f"Block Three: {dut.blockThree.value}")
    print(f"Block Four: {dut.blockFour.value}")
    print(f"Block Five: {dut.blockFive.value}")
    print(f"Block Six: {dut.blockSix.value}")
    print(f"Block Seven: {dut.blockSeven.value}")
    print(f"Block Eight: {dut.blockEight.value}")
    print(f"Block Nine: {dut.blockNine.value}")
    print(f"Block Ten: {dut.blockTen.value}")
    print(f"Block Eleven: {dut.blockEleven.value}")
    print(f"Block Twelve: {dut.blockTwelve.value}")

async def applyTests(dut):
    # Generate a random mantissa
    for i in range(10):
        mantissa = random.randint(0, (1 << 24) - 1)
        
        # Apply input on RisingEdge
        await RisingEdge(dut.clk)
        dut.inp.value = mantissa
        print(f"Input: {mantissa:024b} (Hex: {mantissa:06X})")
        await readOutputs(dut)
        
    


