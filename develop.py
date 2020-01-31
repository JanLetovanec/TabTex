import api


def myBinF(a, b):
    return a + b


if __name__ == '__main__':
    #a = "0	&	0	&	2 \\\\" + "\n" + "0	&	1	&	1 \\\\" + "\n" + "1	&	0	&	0 \\\\" + "\n" + "1	&	1	&	0 \\\\" + "\n"
    #print(a)
    my_f1 = [
        [-1, -2, -3],
        [1, -3, -4],
        [-1, 3, 4],
        [2, 3, -4],
        [-2, 3, 4]
    ]
    table = api.truth_table(4, [my_f1])
    api.remap_value(table, True, "1")
    api.remap_value(table, False, "0")
    print(api.to_string(table))
    #print(api.to_string(table))
