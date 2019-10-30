letter = input()
string = input()
string = string.split(' ')
for i in range(len(string)):
    if letter in string[i]:
        print(string[i])