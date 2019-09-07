def unique_in_order(iterable):
    ans = ["something"]
    for i in iterable:
        if i != ans[-1]:
            ans.append(i)
    return ans[1:]
