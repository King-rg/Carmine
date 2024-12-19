import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import random
import struct

# Helper functions
def float_to_bits(f):
    """Convert a Python float to 32-bit representation."""
    return struct.unpack('>I', struct.pack('>f', f))[0]

def bits_to_float(b):
    """Convert a 32-bit representation to a Python float."""
    return struct.unpack('>f', struct.pack('>I', b))[0]

def decompose_float(b):
    """Decompose a 32-bit float into sign, exponent, and mantissa."""
    sign = (b >> 31) & 0x1
    exponent = (b >> 23) & 0xFF
    mantissa = b & 0x7FFFFF
    return sign, exponent, mantissa

def print_float_decomposition(name, b):
    """Print the decomposition of a float."""
    sign, exponent, mantissa = decompose_float(b)
    print(f"{name}:")
    print(f"  Sign: {sign}")
    print(f"  Exponent: {exponent:08b} (Decimal: {exponent})")
    print(f"  Mantissa: {mantissa:023b} (Hex: {mantissa:06X})")
    print(f"  Float Value: {bits_to_float(b)}")

@cocotb.test()
async def test_add_floats(dut):
    """Testbench for adding two single-precision floats."""

    # Start a clock on the clk port
    clock = Clock(dut.clk, 10, units="ns")  # 100 MHz
    cocotb.start_soon(clock.start())

    # Number of test cases
    NUM_TESTS = 10

    for i in range(NUM_TESTS):
        # Generate two random floats
        a_float = random.uniform(-1e3, 1e3)
        b_float = random.uniform(-1e3, 1e3)
        expected = a_float + b_float

        # Convert floats to bit-level representation
        a_bits = float_to_bits(a_float)
        b_bits = float_to_bits(b_float)
        expected_bits = float_to_bits(expected)

        # Print for debug purposes
        print_float_decomposition("A", a_bits)
        print_float_decomposition("B", b_bits)
        print_float_decomposition("Expected", expected_bits)

   