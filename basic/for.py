# for loop
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print(f"I love {fruit}!!")

for char in "Hello world!!":
    print(char)

# iterable iteration
# challenge1
favorite = input("好きなフルーツは?")
favorite_list = []
for fruit in fruits:
    if fruit == favorite:
        print(f"{fruit}が好き")
        favorite_list.append("好き")
    else:
        print(f"{fruit}は好きでない")
        favorite_list.append("普通")
print(favorite_list)
# challenge2
favorite_fruits = []
normal_fruits = []
fruits = ['apple', 'peach', 'grapes', 'banana']
for fruit in fruits:
    choice = input(f"{fruit}は好き? y/n")
    if choice == 'y':
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)
print(f"favorite fruits: {favorite_fruits}")
print(f"normal fruits: {normal_fruits}")