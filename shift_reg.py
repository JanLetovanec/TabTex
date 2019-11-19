def shift(new, states):
    for i in range(0, len(states)):
        states[i], new = new, states[i]
    return new


def print_state(cycle, states):
    states = map((lambda x: ("0", "1")[x]), states)
    states = "\t&\t".join(states)
    states = str(cycle) + "\t&\t" + states + "\t\\\\"
    print(states)


def shift_reg(cycles, states, f):
    cycles += 1
    last = states[-1]
    for i in range(0, cycles):
        print_state(i, states)
        new = f(i, states, last)
        last = shift(new, states)


def my_seq(cycle, state, last):
    sequence = [1, 0, 1, 0, 1, 1, 1, 0]
    return sequence[cycle % len(sequence)]


if __name__ == '__main__':
    shift_reg(len([1, 0, 1, 0, 1, 1, 1, 0]), [0, 0, 0, 0], my_seq)
