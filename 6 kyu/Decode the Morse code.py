# https://www.codewars.com/kata/decode-the-morse-code/train/python

def decodeMorse(morse_code):
    answer = ""
    word_list = morse_code.split("  ")
    for word in word_list:
        for i in word.split():
            answer += MORSE_CODE[i]
        answer += " "
    return answer.strip()


print(decodeMorse("...---..."))
