age = int(input("何歳ですか?"))
casino_age = 18
game_dict = {1: 'ルーレット', 2: 'ブラックジャック', 3: 'ポーカー'}

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        print("プレイするゲームを選択してください.")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = int(input(":"))
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました")
            break
        else:
            print("正しい選択肢を選んでください!")
            continue
else:
    print("{}歳以上になってから出直しな!!".format(casino_age))

# if age >= casino_age:
#     print("どうぞお入りください")
#     while True:
#         game = int(input(game_text))
#         if game == 1:
#             print("ではルーレットを開始します!")
#             break
#         elif game == 2:
#             print("ではブラックジャックを開始します!")
#             break
#         elif game == 3:
#             print("ではポーカーを開始します!")
#             break
#         else:
#             print("1~3を選んでください!")
#             continue
# else:
#     print("{}歳以上になってから出直しな!!".format(casino_age))