get = input()
key = input()
get_list = get.split('?')
get = get_list[1]
get = get.split('&')
for i in range(len(get)):
    if key in get[i]:
        get[i] = get[i].split('=')
        print(get[i][1])
        break