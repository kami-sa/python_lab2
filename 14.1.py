count = int(input())
recipe = []
new_recipe = []
for i in range(count):
    recipe.append(input())
    if 'лук' not in recipe[i]:
        new_recipe.append(recipe[i])
for i in range(len(new_recipe)):
    if i != len(new_recipe) - 1:
        print(new_recipe[i], end=', ')
    else:
        print(new_recipe[i])

