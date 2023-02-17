# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def change_into(text, i, letter_sum):
    if text[i-1] == text[i]: letter_sum += 1
    else: 
        new_text.append(str(letter_sum) + text[i-1])
        letter_sum = 1
    i += 1
    if i< len(text): change_into(text, i, letter_sum)
    else: new_text.append(str(letter_sum) + text[i-1])

def change_from(text, i):
    new_text.append(text[i+1]*int(text[i]))
    i += 2
    if i < len(text): change_from(text, i)

text = str(input('Введите ырвапол \n'))
l = text[0]
new_text = []
if l.isdigit():
    i = 0
    change_from(text, i)
else:
    i = 1
    letter_sum = 1
    change_into(text, i, letter_sum)
print(new_text)
