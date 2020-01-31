from table_manipulate import (switch_rows, switch_cols, remap_value)
from table_funcs import (generate_function_table, lookup_by_row)
from truth_table import (truth_table)

def to_table(table_string):
    """ Parses string data into something more manageable """
    table = table_string.split("\\\\\n")
    table.pop()
    for index in range(0, len(table)):
        table[index] = table[index].split("\t&\t")
        table[index] = list(map(int, table[index]))
    return table


def to_string(tabular):
    """ Prints the table in TeX format """
    result = ""
    for row in tabular:
        row = list(map(str, row))
        result += "\t&\t".join(row) + "\t\\\\" + "\n"
    return result
