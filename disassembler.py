#!/usr/bin/env python3

# NOTE: This code requires Python 3.7 because of the "namedtuple" usage

from enum import Enum
from collections import namedtuple

class OperandType(Enum):
    REG_A = "REG_A"
    REG_OUT_1 = "REG_OUT_1"
    REG_OUT_2 = "REG_OUT_2"
    REG_IN_1 = "REG_IN_1"
    REG_IN_2 = "REG_IN_2"
    RAM_ADDRESS = "RAM_ADDRESS"
    ROM_ADDRESS = "ROM_ADDRESS"
    IMMEDIATE_VAL = "IMMEDIATE_VAL"
    NONE = "NONE"

InstructionRow = namedtuple("InstructionRow", ["instruction_opcode", "instruction_name", "operand1_type", "operand2_type"])

instruction_table = [
    InstructionRow(0x00, "MOV", OperandType.REG_OUT_1, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x01, "MOV", OperandType.REG_OUT_2, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x02, "MOV", OperandType.REG_A, OperandType.REG_IN_1),
    InstructionRow(0x03, "MOV", OperandType.REG_A, OperandType.REG_IN_2),
    InstructionRow(0x04, "MOV", OperandType.REG_A, OperandType.RAM_ADDRESS),
    InstructionRow(0x05, "MOV", OperandType.RAM_ADDRESS, OperandType.REG_A),
    InstructionRow(0x06, "MOV", OperandType.REG_OUT_1, OperandType.REG_A),
    InstructionRow(0x07, "MOV", OperandType.REG_A, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x08, "AND", OperandType.REG_A, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x09, "CMP", OperandType.REG_A, OperandType.IMMEDIATE_VAL),
    InstructionRow(0x0A, "JMP", OperandType.ROM_ADDRESS, OperandType.NONE),
    InstructionRow(0x0B, "JE",  OperandType.ROM_ADDRESS, OperandType.NONE),
    InstructionRow(0x0C, "JNE", OperandType.ROM_ADDRESS, OperandType.NONE)
]


def find_instruction_by_opcode(opcode):
    for instruction in instruction_table:
        if instruction.instruction_opcode == opcode:
            return instruction
    return None


# TODO: Implement
def opcode_to_asm(opcode):
    print(f"PARSING: {hex(opcode)}")
    pass


def parse_file(file_name):
    file_name = "useless_OS.hex"

    with open(file_name, "r") as file:
        first_line = file.readline().strip()

        if first_line != "v2.0 raw":
            print("Wrong format!!")
            return

        for line in file:
            hex_numbers = line.strip().split(" ")

            for hex_number in hex_numbers:
                try:
                    decimal_number = int(hex_number, 16)
                    opcode_to_asm(decimal_number)
                except ValueError:
                    print(f"Invalid hexadecimal number: {hex_number}")
                    return


if __name__ == '__main__':

    # Print the table in a formatted way
    print("instruction_opcode | instruction_name | operand1_type | operand2_type")
    print("-" * 55)
    for entry in instruction_table:
        print(f"{entry.instruction_opcode:>17x} | {entry.instruction_name:<15} | {entry.operand1_type.value:<13} | {entry.operand2_type.value}")

    # Test find_instruction_by_opcode
    opcode_to_find = 0x02
    found_instruction = find_instruction_by_opcode(opcode_to_find)
    if found_instruction:
        print(f"\nFound instruction: {found_instruction}")
    else:
        print(f"\nNo instruction found for opcode: {opcode_to_find:x}")

    parse_file(None)
