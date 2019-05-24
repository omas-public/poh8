
[恋するハッカソン〜君色に染まるアイドル〜](https://paiza.jp/poh/hatsukoi)
=========================================================================

![poh8](poh8.png)

Hair
----

###  [ショートヘア](hatsukoi_hair2/test.py "ショートヘアセット")

``` python
N, S = int(input()), input()

# 確認用
print(N, S)
```

### [ロングヘア](hatsukoi_hair3/test.py "ロングヘアセット")

``` python
N = int(input())

# 確認用
print(N)
```

### [ポニーテイル](hatsukoi_hair4/test.py,"ポニーテールセット")

``` python
for [d, e] in [input().split() for _ in range(5)]:
  # 確認用
  print(d, e)

```

### [ツインテール](hatsukoi_hair5/test.py "ツインテールセット")

``` python
[s, t] = [int(input()) for _ in range(2)]

# 確認用
print(s, t)
```

### [おさげ](hatsukoi_hair6/test.py "おさげ")

``` python
[n, m] = [int(input()) for _ in range(2)]
ts = [int(input()) for _ in range(m)]

# 確認用
print(n)
for t in ts:
  print(t)
```

EYE
---

### [たれ目](hatsukoi_eye2/test.py "たれ目")

``` python
[s, n] = [int(_) for _ in input().split()]

# 確認用
print(s, t)
```

### [つり目](hatsukoi_eye3/test.py "つり目")

``` python
p = int(input())

# 確認用
print(p)

```

### [めがね](hatsukoi_eye4/test.py "めがね")

``` python
N = int(input())
alist = map(int,input().split()[:N])

# 確認用
for a in alist: 
  print(a)
```

CLOTHES
-------
### [cute衣装](hatsukoi_clothes2/test.py "Cute衣装")

``` python
[n, m] = [int(_) for _ in input().split()]

# 確認
print(n, m)
```

### [sexy衣装](hatsukoi_clothes3/test.py "Sexy衣装")

``` python
[N, M] = [int(_) for _ in input().split()]

# 確認
print(N, M)
```

### [制服](hatsukoi_clothes5/test.py "制服")

``` python
cs = input().split()

# 確認
for c in cs:
  print(c)

```

### [浴衣](hatsukoi_clothes6/test.py "浴衣")

``` python
N = int(input())
ts = [input().split() for _ in range(N)]

for [t, s] in ts:
  # 確認
  print(int(t), s)

```

SPECIAL
-------

### [水着](hatsukoi_special2/test.py "水着")

``` python
[n, m] = map(int, input().split())
[s, t] = [input() for _ in range(2)]

# 確認
print(n, m, s, t)
```

### [マイク](hatsukoi_special5/test.py "マイク")

``` python
[n, m] = [int(input()) for _ in range(2)]

# 確認
print(n, m)
```

### [カチューシャ](hatsukoi_special6/test.py "カチューシャ")

```
[[n, p], [m, q]] = [map(int, input().split()) for _ in range(2)]

# 確認
print(n, p, m, q)

```