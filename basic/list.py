# リスト(lists): 複数のオブジェクトを順序付けて保存するデータ型
# []で括って,(カンマ)で各オブジェクトを区切る
fruits = ['apple', 'peach', 'melon', 'grapes']
hetro_list = ['string', 1, 3.4, True, fruits]

print(hetro_list)
print(fruits[0])
print(fruits[-1])
print(hetro_list[-1][-1])
print("hello world"[6])
# .append: 新しいオブジェクトを追加する
print(fruits)
fruits.append('banana')
print(fruits)
# .insert: 指定したindexにオブジェクトを追加する
print(fruits)
fruits.insert(3, 'lemon')
print(fruits)
# .remove: マッチした最初のオブジェクトを除く
print(fruits)
fruits.remove('peach')
print(fruits)
# .sort: 昇順に並び替える
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# .len(): リストの要素数を取得する(length)
print(len(fruits))
print(len("hello world"))