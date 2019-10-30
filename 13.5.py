n = int(input())
commands = dict([input('Введите название команды и баллы через пробел:').split() for _ in range(n)])
list_d = list(commands.items())
list_d.sort(key=lambda i : i[1]);
list_d.reverse()
for i in list_d:
    print(i[0], ':', i[1])