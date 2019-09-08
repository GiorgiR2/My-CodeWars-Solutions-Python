# https://www.codewars.com/kata/are-the-numbers-in-order/train/python
def in_asc_order(arr):
    last_num = 0
    for i in arr:
        if i <= last_num:
            return False
        last_num = i
    return True
