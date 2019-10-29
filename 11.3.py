word = input()
place = int(input())
letter = input()
if len(letter) > 1:
    print('ОШИБКА')
elif word[place-1] == letter:
    print('ДА')
else:
    print('НЕТ')