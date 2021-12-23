# is演算子 : 同じオブジェクトかどうか判定する
a = 1
b = 1
c = 3
d = a
e = 2 - 1
print(id(a))
print(id(b))
print(id(c))
print(id(1))
print(a is b)  #idの一致
print(a is not c)

print(d is a)
print(d is b)

print(a is e)

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"
print(hello, hello2)
print(hello is hello2)

hello = "konnichiwa"

print(id(hello))
print(id(hello2))

print(hello is hello2)

# Noneかどうかの判定によく使う

nothing = None
print(nothing)

print(id(None))
print(id(nothing))

print(nothing is None)