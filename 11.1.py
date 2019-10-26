combination = input()
#print(combination.split('p'))
comb_list = combination.split('p'); #английская раскладка
length = 0;
for i in range(len(comb_list)):
    if len(comb_list[i])>length:
        length = len(comb_list[i])
print(length)
