#import re;
count = int(input())
code = [input() for i in range(count)]
for i in range(count):
    for j in range(len(code[i])):
        code[i] = ' '.join(code[i].split())
#print(code)