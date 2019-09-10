# https://www.codewars.com/kata/grill-it/train/python
def grille(message, code):
    answer, code = "", "{0:0{1}b}".format(code, len(message))
    if len(code) > len(message):
        code = code[int("-" + str(len(message))):]
    for i, j in zip(list(message), list(code)):
        if j == "1":
            answer += i
    return answer


print(grille("ab", 256) == "")
print(grille("abcde", 32) == "")
