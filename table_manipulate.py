import sys


def print_back(tabular):
    """ Prints the table in TeX format """
    for row in tabular:
        row = list(map(str, row))
        print("\t&\t".join(row) + "\t\\\\")


def parse_table(table_string):
    """ Parses string data into something more manageable """
    table = table_string.split("\t\\\\\n")
    table.pop()
    for index in range(0, len(table)):
        table[index] = table[index].split("\t&\t")
        table[index] = list(map(int, table[index]))
    return table


def switch_rows(tabular, index1, index2):
    """ Swaps two rows """
    tabular[index1], tabular[index2] = tabular[index2], tabular[index1]
    return tabular


if __name__ == '__main__':
    print("Please copy paste your table here (including the last new-line)")
    input_str = sys.stdin.read()
    table = parse_table(input_str)
    switch_rows(table, 0, 3)
    print_back(table)

# 0	&	0	&	1	\\
# 0	&	1	&	1	\\
# 1	&	0	&	0	\\
# 1	&	1	&	0	\\
