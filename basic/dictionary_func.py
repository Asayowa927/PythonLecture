fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}
# print(fruits_colors['apple'])
if 'peach' in fruits_colors:
    print(fruits_colors['peach'])
else:
    print('the key is not found')

# .get()
fruit = input("フルーツの名前をしてください")
print(fruits_colors.get(fruit, 'nothing'))

# .update()
fruits_colors2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_colors.update(fruits_colors2)
print(fruits_colors)