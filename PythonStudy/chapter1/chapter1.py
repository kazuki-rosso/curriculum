1-1
>>> data = [1, 3, 5, 7]
>>> for i in data:
...     print(i ** 2)
...
1
9
25
49



1-2
>>> for j in range(1, 9, 2):
...     print(j ** 2)
...
1
9
25
49
>>>

2-1
>>> all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
>>> wait_place = ["札幌","大阪"]
>>> get_place = ["横浜"]
>>> for place in all_place:
...     if place == "横浜":
...         print(place + "のチケットが当選しました!")
...     elif place == "札幌" or place == "大阪":
...         print(place + "のチケットは結果待ち")
...     else:
...         print(place + "のチケットは落選しました")
...
札幌のチケットは結果待ち
東京のチケットは落選しました
横浜のチケットが当選しました!
大阪のチケットは結果待ち
名古屋のチケットは落選しました
福岡のチケットは落選しました

2-2
>>> get_place.extend(wait_place)
>>> s = "{}と{}と{}のチケットが当選しました!"
>>> print(s.format(*get_place))
横浜と札幌と大阪のチケットが当選しました!
