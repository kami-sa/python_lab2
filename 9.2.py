num_of_list = int(input())
flag = num_of_list
pupil_list = set()
while num_of_list != 0:
    if num_of_list == flag:
        num_of_pup = int(input())
        for i in range(num_of_pup):
            pupil_list.add(input())
    else:
        pupils = set()
        [pupils.add(input()) for i in range(int(input()))]
        pupil_list = pupil_list.intersection(pupils)
    num_of_list -= 1
print(pupil_list)


