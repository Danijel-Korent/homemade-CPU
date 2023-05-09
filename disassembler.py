#!/usr/bin/env python3

# NOTE: This code requires Python 3.7 because of the "namedtuple" usage
# TODO: Replace namedtuple with "real" struct

from enum import Enum
from collections import namedtuple

class OperandType(Enum):
    REG_A = "a"
    REG_OUT_1 = "out1"
    REG_OUT_2 = "out2"
    REG_IN_1 = "in1"
    REG_IN_2 = "in2"
    RAM_ADDRESS = "RAM_ADDRESS"
    ROM_ADDRESS = "ROM_ADDRESS"
    IMMEDIATE_VAL = "IMMEDIATE_VAL"
    NONE = "NONE"

InstructionRow = namedtuple("InstructionRow", ["instruction_opcode", "instruction_name", "operand1_type", "operand2_type"])


# A table of all valid instructions of the CPU's ISA
instruction_table = [
    InstructionRow(0x00, "mov", OperandType.REG_OUT_1, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x01, "mov", OperandType.REG_OUT_2, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x02, "mov", OperandType.REG_A, OperandType.REG_IN_1),
    InstructionRow(0x03, "mov", OperandType.REG_A, OperandType.REG_IN_2),
    InstructionRow(0x04, "mov", OperandType.REG_A, OperandType.RAM_ADDRESS),
    InstructionRow(0x05, "mov", OperandType.RAM_ADDRESS, OperandType.REG_A),
    InstructionRow(0x06, "mov", OperandType.REG_OUT_1, OperandType.REG_A),
    InstructionRow(0x07, "mov", OperandType.REG_A, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x08, "nand", OperandType.REG_A, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x09, "cmp", OperandType.REG_A, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x0A, "jmp", OperandType.ROM_ADDRESS, OperandType.NONE),
    InstructionRow(0x0B, "je",  OperandType.ROM_ADDRESS, OperandType.NONE),
    InstructionRow(0x0C, "jne", OperandType.ROM_ADDRESS, OperandType.NONE)
]


def find_instruction_by_opcode(opcode):
    for instruction in instruction_table:
        if instruction.instruction_opcode == opcode:
            return instruction
    return None


def operand_to_string(operand_type, operand_val):
    string = ""

    operand_hex_val = hex(operand_val)

    if operand_type == OperandType.REG_A:
        string = OperandType.REG_A.value
    elif operand_type == OperandType.REG_OUT_1:
        string = OperandType.REG_OUT_1.value
    elif operand_type == OperandType.REG_OUT_2:
        string = OperandType.REG_OUT_2.value
    elif operand_type == OperandType.REG_IN_1:
        string = OperandType.REG_IN_1.value
    elif operand_type == OperandType.REG_IN_2:
        string = OperandType.REG_IN_2.value
    elif operand_type == OperandType.RAM_ADDRESS:
        string = "[" + operand_hex_val + "]"
    elif operand_type == OperandType.ROM_ADDRESS:
        string = operand_hex_val
    elif operand_type == OperandType.IMMEDIATE_VAL:
        string = operand_hex_val
        # TODO: This really shouldn't be done in this function but in some later stage
        if operand_val > 31:
            string += f"    ; '{chr(operand_val)}'"
        elif operand_val == 0xa:
            string += f"    ; '\\n'"
    elif operand_type == OperandType.NONE:
        pass
    else:
        print("ERROR: Variable is not a valid OperandType enum value")

    return string


# TODO: Add type hints
def instruction_to_asm_string(instruction):

    asm = ""

    operand = instruction & 0xFF
    opcode = (instruction & 0xF00) >> 8


    #print(f"PARSING: {hex(instruction)}")
    #print(f"OPERAND: {hex(operand)}")
    #print(f"OPCODE:  {hex(opcode)}")

    instruction = find_instruction_by_opcode(opcode)

    operand_1_str = operand_to_string(instruction.operand1_type, operand)
    operand_2_str = operand_to_string(instruction.operand2_type, operand)

    #print(f"Instruction: {instruction.instruction_opcode} {instruction.instruction_name}")
    asm = f"{instruction.instruction_name} {operand_1_str}"

    if operand_2_str != "":
        asm += f", {operand_2_str}"

    print(asm)
    return asm


# TODO: Not a good name anymore as this is now parsing data from input file,
#       processing the data and writing the result into the output file
#
# TODO: By separating this code into reading stage (parsing into array of integer values),
#       processing stage (turning array of integer values into array of instruction structs)
#       and outputing stage (turning array of instruction strucs into a file) the code will
#       be easier to read, easier to understand and probably even simpler
def parse_file(input_file_name):

    # TODO: Temp hardcoded, just for testing
    #       remove this after development ends
    input_file_name  = "useless_OS.hex"
    output_file_name = "useless_OS.asm"

    with open(input_file_name, "r") as input_file:
        first_line = input_file.readline().strip()

        if first_line != "v2.0 raw":
            print("Wrong format!!")
            return

        with open(output_file_name, "w") as output_file:

            address = 0

            for line in input_file:
                hex_numbers = line.strip().split(" ")

                for hex_number in hex_numbers:
                    try:
                        decimal_number = int(hex_number, 16)
                        asm = instruction_to_asm_string(decimal_number)
                        output_file.write(f"{hex(address)}: {asm} \n")
                        address += 1
                    except ValueError:
                        print(f"Invalid hexadecimal number: {hex_number}")
                        return


if __name__ == '__main__':

    # Print the table in a formatted way
    print("instruction_opcode | instruction_name | operand1_type | operand2_type")
    print("-" * 55)
    for entry in instruction_table:
        print(f"{entry.instruction_opcode:>17x} | {entry.instruction_name:<15} | {entry.operand1_type.value:<13} | {entry.operand2_type.value}")

    # TODO: Get the file name from the command line
    parse_file(None)
