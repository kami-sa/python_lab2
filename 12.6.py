n = int(input())
y = 1/n
a = str(y)
a = a.lstrip('0')
a = a.lstrip('.')
string = ''
symbol = ''
num_set = set(a)
count = len(num_set)
count1 = 1;
#print(num_set)
for i in range(count):
    # if a[i] in num_set:
    #     string += a[i];
    #     num_set.remove(a[i])
    for j in range(len(a)):
        for k in range(len(a)-1):
            if a[j] == a[k]:
                count1 += 1
        if count1 > 1:
            if a[i] in num_set:
                string += a[i];
                num_set.remove(a[i])
if string[0] == '0' and string[0] != a[2]:
    string = string.lstrip('0')
print(string)
# count = 0
# for i in range(len(a)-1):
#     if a[i] != a[i+1]:
#         string += a[i] #+ a[i+1]
#     else:
#         string = a[i]
#     for j in range(i, len(a), len(string)):
#         if string == a[i:len(string):1] and string != '0':
#             count += 1
#     if count > 1:
#         print(string)
#         break;
    # symbol = a[i]
    # if symbol != a[i+1]:
    #     string += symbol
    # else:
    #     string = symbol;
    # if a.count(string) > 1:
    #     break
#print(string)
# n = int(input())
# r = 1
# rr = []
# dd = []
# while r not in rr:
#     rr.append(r)
#     dd.append(10*r//n)
#     r = 10*r%n
# print(*dd[rr.index(r):])