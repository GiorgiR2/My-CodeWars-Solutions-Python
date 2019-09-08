# https://www.codewars.com/kata/54ba84be607a92aa900000f1
def is_isogram(string):
    last = ''
    for i in string.lower():
        if i in last:
            return False
        last += i
    return True
