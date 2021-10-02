多重リスト（配列の中に配列を入れる）

a=[1,[2,3,'apple'],3])

print([1][2])#apple

a=[1,2,3,4,5])

a.append('a','b')#[1,2,3,4,5,'a','b']

a.in(間に入れるからin)sert(1,'c')#[1,'c',2,3,4,5,'a','b']

a.clear()#a配列を消す

a=['b','c','a','d']

a.sort()(a=sorted(a))

print(a)#辞書の昇順より['a','b','c','d']

a.reverse()#辞書の降順より['d','c','b','a']

a=[1,2,3,3,3]

print(a.remove(3))#左から3を１つ消す#[1,2,3,3]

b=a.pop()#配列はスタックよりpopで最新の3を取り出す

print(a,b)#[1,2,3,3] 3

print(a.count(1))#1の数を数えるより1表示

c=a

c[0]='A'

print(a)#['A',1,2,3,3]cとaのメモリアドレスは同じなのでc書き換えるとaも書き換わる

#～これを防ぐには～

c=a.copy()をつかうとaは[1,2,3,3]のままになる

a={'a':1,'b':2,'c':3}

print(a.values())#1,2,3

print(a.keys)#'a','b','c'

print(a.items())#{'a':1,'b';2,'c':3}

print(a['a'])#1

print(a.get('a')#1 ,エラーにはならなく、第２引数に指定したものを表示(何も指定しなかったときは「None]返す