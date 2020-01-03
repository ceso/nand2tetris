#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from help_funcs import *
from default_tables import *

def translate(code, a_table, c_table):
    asm = []

    for line in code:
        if is_a_inst(line):
            asm.append(a_table[line])
        elif is_c_inst(line):
            asm.append(c_table[line])

    return asm

def make_c_table(code, first_bits):
    c_table = {}

    for line in code:
        if is_c_inst(line):
            semi_c = line.find(';')
            equal = line.find('=')

            # if inst_c is dest=comp;jmp
            if equal != -1 and semi_c != -1:
                dest = line[:equal]
                goto = line[semi_c+1:]
                comp = line[equal+1:semi_c]
                a_bit = get_abit(comp)
                c_table[line] = first_bits + a_bit + comp_table[comp] + dest_table[dest] + goto_table[goto]
            # if inst_c is dest=comp
            elif equal != -1 and semi_c == -1:
                dest = line[:equal]
                comp = line[equal+1:]
                a_bit = get_abit(comp)
                c_table[line] = first_bits + a_bit + comp_table[comp] + dest_table[dest] + goto_table['null']
            # if comp;jmp
            elif equal == -1 and semi_c != -1:
                comp = line[:semi_c]
                a_bit = get_abit(comp)
                goto = line[semi_c+1:]
                c_table[line] = first_bits + a_bit + comp_table[comp] + dest_table['null'] + goto_table[goto]

    return c_table

def make_a_table(code, label_table):
    a_table = {}
    start = 16
    for line in code:
        if is_a_inst(line):
            key = line[1:]
            # is a instruction
            if parse_int(key) is not None:
                a_table[line] = format(int(key), '016b')
            # already in a_table
            elif line in a_table.keys():
                continue
            # is in a predefined symbol
            elif key in predef_table.keys():
                a_table[line] = format(predef_table[key], '016b')
            # if is a label
            elif key in label_table.keys():
                a_table[line] = label_table[key]
            else:
                a_table[line] = format(start, '016b')
                start += 1

    return a_table

def make_label_table(code_asm):
    i = 0
    label_table = {}

    for line in code_asm:
        i += 1
        if is_label(line):
            i -= 1
            label_table[line[1:-1]] = format(i, '016b')
    
    return label_table

def main():
    file_asm = sys.argv[1]
    # for bits 14, 15 and 16
    first_bits = '111'
    code = prepare_code(file_asm)
    label_table = make_label_table(code)
    a_table = make_a_table(code, label_table)
    c_table = make_c_table(code, first_bits)
    asm_code = translate(code, a_table, c_table)    
    write_asm_f(asm_code, file_asm)

main()
