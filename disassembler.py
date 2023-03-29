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

