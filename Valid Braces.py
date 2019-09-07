def validBraces(string):  # []{}()
    last = " "
    op, cl = "[{(", "]})"
    for i_n, i in enumerate(string):
        if i in cl and last[-1] == op[cl.index(i)]:
            last = last[0:-1]
        elif i in op:
            last += i
        elif i not in op:
            return False
    if last == ' ':
        return True
    return False
