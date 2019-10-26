count = int(input())
workers = []
for i in range (count):
    workers.append(input())
set_of_workers = set (workers)
count = 0
sum = 0
while len(set_of_workers) != 0:
    w = set_of_workers.pop()
    for i in range(len(workers)):
        if workers[i] == w:
            count += 1
    if count > 1:
        sum += count;
    count = 0;

print(sum)
#print(len(set_of_workers))