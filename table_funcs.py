

def generate_function_table(f, start, end_excluded):
    """
    Generates a table of the binary function f, feeding in integer inputs from start to end (excluded)
    (1st argument by row, 2nd by column)
    :param f: binary function over integers
    :param start: starting input value
    :param end_excluded: ending input value (excluded)
    :return: Table, with 1st row being second argument inputs,
    1st column being first argument inputs,
    and all other cells are f(a1, a2)
    """
    table = []
    for row in range(start - 1, end_excluded):
        if row < start:
            table.append(get_table_header(start, end_excluded))
        else:
            table.append(get_row(f, row, start, end_excluded))
    return table


def get_table_header(start, end_excluded):
    """ Get the header row for table """
    row = []
    for i in range(start - 1, end_excluded):
        if i < start:
            row.append(None)
        else:
            row.append(i)
    return row


def get_row(f, first, start, end_excluded):
    row = []
    for i in range(start - 1, end_excluded):
        if i < start:
            row.append(first)
        else:
            v = f(first, i)
            row.append(v)
    return row


def lookup_by_row(table, target):
    """
    Looks up a specific value per row
    :param table: table used for lookup
    :param target: target value
    :return: table of two columns: row index, and column index if found
    """
    new_table = []
    for j in range(1, len(table)):
        row = table[j]
        new_row = [row[0]]
        for i in range(1, len(row)):
            if row[i] == target:
                new_row.append(table[0][i])
                break
        if len(new_row) < 2:
            new_row.append(None)
        new_table.append(new_row)
    return new_table
