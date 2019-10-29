count = int(input())
words = [input() for i in range(count)]
for i in range (count):
    if words[i][0:4:1] != "####":
        if words[i][0:2:1] != "%%":
            print(words[i])
        else:
            print(words[i][2:-1:1])
