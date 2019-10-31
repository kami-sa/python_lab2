def get_key(d, value):
    a = []
    for k, v in d.items():
        if v == value:
            a.append(k)
    return a
n = int(input())
numbers = dict([input('Введите номер телефона и владельца через пробел:').split() for _ in range(n)])
#list_d = list(numbers.items())
# for i in list_d:
#     print(i[0], ':', i[1])
m = int(input())
for i in range(m):
    name = input()
    if name in numbers.values():
        print(*get_key(numbers, name), end = ' ')
    else:
        print('Нет такого имени')
    print()
