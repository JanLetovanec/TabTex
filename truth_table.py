def execute_term(inputs, literals):
    for literal in literals:
        if literal < 0:
            literal *= -1
            literal -= 1
            if inputs[literal]:
                return False
        else:
            literal -= 1
            if not inputs[literal]:
                return False
    return True


def execute(inputs, terms):
    """ Resolves a function for given inputs """
    for term in terms:
        if execute_term(inputs, term):
            return "1"
    return "0"


def get_row(state, fs):
    """ Generates next row string """
    input_row = []
    for bool_val in state:
        value = (False, True)[bool_val]
        input_row.append(value)

    output_row = []
    for terms in fs:
        output_row.append(execute(state, terms))

    row = input_row + output_row
    return row


def generate_input(input_var):
    """ Generates next input """
    pointer = len(input_var) - 1
    while pointer >= 0:
        input_var[pointer] = not input_var[pointer]
        if input_var[pointer]:  # was 0 before, then you are done
            pointer = -1
        pointer -= 1
    return


def truth_table(variable_num, fs):
    """
    Generates truth table for custom functions
    :param variable_num: number of variables appearing in functions
    :param fs: a list of boolean functions of those variables,
    function is a list of terms in SOP form (considered || together)
    term is a list of literals (considered && together)
    literal is an integer, negative values are considered as negated,
    magnitude of the integer is order of the variable (i.e. -1 is not first variable)
    :return: resulting table, first variable_num columns are inputs,
    then every column corresponds to one provided function
    """
    inputs = [False]*variable_num
    zero = [False]*variable_num
    result = []

    while True:
        row = get_row(inputs, fs)
        result.append(row)
        generate_input(inputs)
        if inputs == zero:
            break

    return result

# TODO: add some more user-friendly way of inputting functions

