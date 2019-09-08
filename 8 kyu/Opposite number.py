# https://www.codewars.com/kata/56dec885c54a926dcd001095
def opposite(number):
    if str(number)[0] == "-":
        return float(str(number)[1:])
    return float("-"+str(number))

