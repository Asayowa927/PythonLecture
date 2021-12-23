# input(): ユーザの丹生勅した値(文字列)を取得する

# age = input("何歳ですか？")
# print("あなたは{}歳です".format(age))

# challenge1
age = int(input("何歳ですか?"))
casino_age = 18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""
if age >= casino_age:
    print("どうぞお入りください")
    game = int(input(game_text))
    if game == 1:
        print("ではルーレットを開始します!")
    elif game == 2:
        print("ではブラックジャックを開始します!")
    elif game == 3:
        print("ではポーカーを開始します!")
    else:
        print("1~3を選んでください!")

else:
    print("{}歳以上になってから出直しな!!".format(casino_age))