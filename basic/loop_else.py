# fruits = ['apple', 'peach', 'grapes', 'banana']
#
# for fruit in fruits:
#     choice = input(f"あなたが探しているふフルーツは{fruit}ですか? y/n:")
#     if choice == "y":
#         print("見つかってよかったですね")
#         break
#     else:
#         print("そうですか...")
#     print(fruit)
# else:
#     print("お探しのフルーツはみつかりませんでした。")
#
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("countは10未満でなくなりました")

balance = 1000
game_price = 200
while balance >= game_price:
    choice = input(f"1回{game_price}円のゲームに参加しますか?(残高:{balance}円)(y/n?)")
    if choice == "y":
        balance -= game_price
        print(balance)
    elif choice == "n":
        print("また遊びましょう")
        break
    else:
        print("y/nで答えてください")
else:
    print(f"あなたの残高は{balance}円です. もうお金なくなっちゃいましたね ^_^;;")