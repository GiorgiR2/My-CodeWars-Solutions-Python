# https://www.codewars.com/kata/grill-it/train/python
def grille(message, code):
    code = "{0:0{1}b}".format(code, len(message))[int("-" + str(len(message))):]
    return "".join([i for i, j in zip(list(message), list(code)) if j == "1"])


print(grille("ab", 256) == "")
print(grille("abcde", 32) == "")
