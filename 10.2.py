step = int(input())
phrase = input()
new_phrase = ''
for i in range(len(phrase)):
    if phrase[i] != ' ':
        new_phrase +=chr(ord(phrase[i])+step)
    else:
        new_phrase += phrase[i]
print(new_phrase)