def is_isogram(string):
    last = ''
    for i in string.lower():
        if i in last:
            return False
        last += i
    return True
