# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def rem_word(i):
    if 'абв' in i: i = None
    if i!= None: new_text.append(i)

text = str(input('Введите текст \n'))
text = text.split()
new_text = []
for i in text:
    rem_word(i)
for i in new_text: print(i, end=' ')
