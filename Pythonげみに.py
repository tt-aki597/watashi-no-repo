#printで文字を出す方法と四則演算
print("hello world")
print("LOL XD (^-^)")
print("こんにちは")
print("蚕")
print(0+1+2+3+10000)
print(2+3)
print("t123212321")


#置き換えと代入
x=2132123
a = 0.121
print (type(x+1))
print(type(x+a))

#属性
s = "wwww"
print (type(s))
print(s)

#真偽
w = 10 > 1
print(w)

#xに一つではなく複数　データを持たせ,何個目に何があるか取り出す
b =[1,2,3,4,5,6,7,]
print(type(b))
print(b[1])

#仮定した文字.appendで仮定した文字に付け足して入れられる
b.append(8)

print (b)

#remove で削除
b.remove(2)
print(b)

#やってることは上と同じ 順番指定なし
c = {"サクランボ" : 10,"オレンジ" : 20, "イチゴ" : 30}


print (c["サクランボ"])
print (c["オレンジ"])
print (c["イチゴ"])

c["サクランボ"] = 333

print (c)


c["gawawa"] = 60

print(c)

c.pop ("gawawa")

print (c)

print (type(c))