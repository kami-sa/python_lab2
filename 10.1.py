word = input()
letter = int(input())
if letter > len(word):
    print('ERROR')
else:
    print(word[letter-1])