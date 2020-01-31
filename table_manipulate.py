import sys
from table_funcs import *


def switch_rows(tabular, index1, index2):
    """ Swaps two rows """
    tabular[index1], tabular[index2] = tabular[index2], tabular[index1]
    return tabular


def switch_cols(tabular, index1, index2):
    """ Swaps two columns"""
    for row in tabular:
        row[index1], row[index2] = row[index2], row[index1]
    return tabular


def remap_value(table, target, default):
    """
    Mutates table!
    Remaps all target values to default values
    :param table: Table to mutate
    :param target: Target value to change
    :param default: Default to change the target to
    :return: None
    """
    for row_index in range(0, len(table)):
        for cel_index in range(0, len(table[row_index])):
            if table[row_index][cel_index] == target:
                table[row_index][cel_index] = default
