# if文のNoneの取り扱い
a = None
if a is None:
    print("a is None!!")
else:
    print("a has value!!")
if a:
    print("a has value")
else:
    print("a in None!!")
if not a:
    a = 10
    print(a)
