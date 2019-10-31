n = int(input())
microbe = [[int(input()) for x in range(n)] for y in range(n)]
print(microbe)
shot = int(input())
choice = [[int(input()) for j in range(2)] for i in range(shot)]
for k in range(shot):
    microbe[choice[k][0]][choice[k][1]] -= 8
    for i in range(n):
        for j in range(n):
            if abs(choice[k][0] - i) <= 1 and abs(choice[k][1] - j) <= 1 and (
                    choice[k][0] != i or choice[k][1] != j):
                microbe[i][j] -= 4
            if microbe[i][j] < 0:
                microbe[i][j] = 0

for i in range(len(microbe)):
    for j in range(len(microbe)):
        print(microbe[i][j], end=' ')
    print()
