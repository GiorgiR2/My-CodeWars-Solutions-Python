# https://www.codewars.com/kata/54e6533c92449cc251001667
def unique_in_order(iterable):
    ans = ["something"]
    for i in iterable:
        if i != ans[-1]:
            ans.append(i)
    return ans[1:]
