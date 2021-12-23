# in演算子
fruits = ['apple', 'peach', 'grapes', 'banana']
# print('lemon' in fruits)
favorite = input("What is your favorite fruit?")

# challenge1
if favorite not in fruits:
    print("{}ですね, 仕入れました".format(favorite))
    fruits.append(favorite)
else:
    print("{}ですね, 差し上げますよ".format(favorite))
    fruits.remove(favorite)

print(fruits)