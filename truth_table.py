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
    input_strings = []
    for bool_val in state:
        value = ("0", "1")[bool_val]
        input_strings.append(value)

    output_string = []
    for terms in fs:
        output_string.append(execute(state, terms))

    input_row = "\t&\t".join(input_strings)
    output_row = "\t&\t".join(output_string)
    row = input_row + "\t&\t" + output_row + "\t\\\\"
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
    """ Generates truth table """
    inputs = [False]*variable_num
    zero = [False]*variable_num

    while True:
        row = get_row(inputs, fs)
        print(row)
        generate_input(inputs)
        if inputs == zero:
            break


if __name__ == '__main__':
    my_var_num = 2
    my_f1 = [
        [-1,-2,-3],
        [1,-3,-4],
        [-1,3,4],
        [2,3,-4],
        [-2,3,4]
    ]
    my_f2 = [
        [-1]
    ]
    truth_table(my_var_num, [my_f2])
    # truth_table(my_var_num, [my_f2, my_f1])
