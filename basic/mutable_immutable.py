# # mutable (list,dict,set)
# fruits = ['apple', 'peach', 'banana']
# print(f"fruitsのIDは{id(fruits)}")
# fruits.append('lemon')
# print(f"fruitsのIDは{id(fruits)}")
#
#
# # immutable (int, float, str, bool, tuple)
# fruit = 'apple'
# print(f"fruitsのIDは{id(fruit)}")
# fruit += ', lemon'
# print(f"fruitsのIDは{id(fruit)}")
#

text = ""
for i in range(1, 11):
    text += "-" + str(i)
print(text)

text_list = []

for i in range(1, 11):
    text_list.append(str(i))
text = "-".join(text_list)
print(text)
