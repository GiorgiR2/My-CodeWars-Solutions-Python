# https://www.codewars.com/kata/56606694ec01347ce800001b
def is_triangle(a, b, c):
    l = [a, b, c]
    rows = [[0, 1, 2],
            [2, 0, 1],
            [1, 2, 0]]
    for i in rows:
        if l[i[0]] + l[i[1]] <= l[i[2]]:
            return False
    return True
