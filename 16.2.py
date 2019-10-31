r = int(input())
csv = [input() for i in range(r)]
count = int(input())
for i in range(r):
    csv[i] = csv[i].split(',')
#print(csv)
print_list = [[]]
# for i in range(count):
#     for j in range(2):
#         print_list[i][j] = int(input())
print_list = [[int(input()) for x in range(2)] for y in range(count)]
for x in range(1):
    for y in range(count):
        print(csv[print_list[y][x]][print_list[y][x+1]])
# print(csv[print_list[0][0]][print_list[0][1]])
# print(csv[print_list[1][0]][print_list[1][1]])
# print(csv[print_list[2][0]][print_list[2][1]])
# print(csv[print_list[3][0]][print_list[3][1]])