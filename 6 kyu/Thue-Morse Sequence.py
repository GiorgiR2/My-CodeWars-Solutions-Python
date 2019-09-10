# https://www.codewars.com/kata/thue-morse-sequence/train/python
def thue_morse(n):
    answer, next_step = "0", ""
    for i in range(n-1):
        for i in answer:
            if i == "1":
                next_step += "0"
            else:
                next_step += "1"
            if len(answer) >= n:
                break
        answer += next_step
        next_step = ""
    return answer[0:n]


print(thue_morse(5))
