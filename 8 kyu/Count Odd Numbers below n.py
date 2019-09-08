# https://www.codewars.com/kata/59342039eb450e39970000a6
def odd_count(n):
    input_list = [i for i in range(1, n, 2)]
    middle = int((float(len(input_list))/2) - .5)
    return input_list[middle]
