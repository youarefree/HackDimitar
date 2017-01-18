import sys

matrix = ['f :: String -> Int\n', 'g :: Int -> String\n', '\n', 'f . g\n']
splitting_symbols = ['::', '->']


def splitting(for_split):
    first_list = []
    second_list = []
    third_list = []
    help_list = []
    for k in for_split:
        first_list.append(k.split(" :: "))
    for j in first_list:
        help_list.append(j.split(" -> "))
    for i in help_list:
        if i not in splitting_symbols:
            second_list.append
    third_list.append(second_list)
    return third_list


def return_function(input_value, in_type, out_type):
    if in_type == "String" and out_type == "Int":
        return len(in_type)
    if in_type == "Int" and out_type == "String":
        return str(in_type)
    if in_type == out_type:
        return type(out_type)


def main():
    inpt = list(sys.stdin)
    print(inpt)
    list_of_equations = splitting(inpt)
    print(list_of_equations)
    # for i in list_of_equations:








if __name__ == '__main__':
    main()

