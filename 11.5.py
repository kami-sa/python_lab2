word = input()
while len(word) != 1:
    word = word.strip(word[0]);
    word = word.strip(word[-1]);
    print(word)
