#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/parsing-a-boolean-expression/
# Unfinished


def parse_bool_expr(expression):
    logical_operators = []
    sub_expression = []
    boolean_mapper = {'t': True, 'f': False}
    i = 0
    size = len(expression)
    while i < size:
        e = expression[i]
        if e == '!':
            sub_expression.append(not boolean_mapper[expression[i + 2]])
            i += 3
        elif e == '&' or e == '|':
            logical_operators.append(e)
        else:
            i += 1
    return sub_expression[0]


if __name__ == '__main__':
    print(parse_bool_expr("!(f)"))
    # print(parse_bool_expr("|(f,t)"))
    # print(parse_bool_expr("&(t,f)"))
    # print(parse_bool_expr("|(&(t,f,t),!(t))"))

