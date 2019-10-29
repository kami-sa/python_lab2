count1 = int(input())
filter_set = set()
for i in range(count1):
    filter_set.add(input())
count2 = int(input())
# search_set = set()
# for i in range(count2):
#     search_set.add(input())
# new_set = filter_set.intersection(search_set);
# print(new_set)
new_set = []
for i in range(count2):
    a = input()
    if a in filter_set:
        new_set.append(a)
print (new_set)
