r = int(input())
csv = [input() for i in range(r)]
count = int(input())
for i in range(r):
    csv[i] = csv[i].split(',')
print_list = [[]]
print_list = [[int(input()) for x in range(2)] for y in range(count)]
for x in range(1):
    for y in range(count):
        print(csv[print_list[y][x]][print_list[y][x+1]])
