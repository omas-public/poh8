
# [恋するハッカソン〜君色に染まるアイドル〜](https://paiza.jp/poh/hatsukoi)

![poh8](poh8.png)

## Hair

### [ショートヘア](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair2)

python3
[解答例](./hatsukoi_hair2/test.py "ショートヘアセット")

```python
N, S = int(input()), input()

# 確認用
print(N, S)
```

javascript
[解答例](./hatsukoi_hair2/test.js "ショートヘアセット")

```js

// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// declare variable
const [N, S] = [parseInt(lines[0], 10), lines[1]]

// Main 
// console.log(`N:${N}, S:${S}`)

```

### [ロングヘア](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair3)

python3
[解答例](hatsukoi_hair3/test.py "ロングヘアセット")

```python
N = int(input())

# 確認用
print(N)
```

javascript
[解答例](hatsukoi_hair3/test.js "ロングヘアセット")

```js
// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// declare variable
const N = parseInt(lines[0], 10)

// Main 
//console.log(`N:${N}`)

```

### [ポニーテイル](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair4)

python3
[解答例](hatsukoi_hair4/test.py　"ポニーテールセット")

``` python
for [d, e] in [input().split() for _ in range(5)]:
  # 確認用
  print(d, e)

```

javascript
[解答例](hatsukoi_hair4/test.js　"ポニーテールセット")

```js
// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// main
let count = 0 
for (const [d, e] of lines) {
  // console.log(`d:${d}, e:${e}`)
  // カウントする
}
// OKかNGを出力する

```

### [ツインテール](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair5)

python3
[解答例](hatsukoi_hair5/test.py "ツインテールセット")

``` python
[s, t] = [int(input()) for _ in range(2)]

# 確認用
print(s, t)
```

javascript
[解答例](hatsukoi_hair5/test.js "ツインテールセット")

```js
// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

const [s, t] = Array.from(lines, Number)

// main
// console.log(`s:${s}, t:${t}`)

```

### [おさげ](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair6)

python3
[解答例](hatsukoi_hair6/test.py)

```python
[n, m] = [int(input()) for _ in range(2)]
ts = [int(input()) for _ in range(m)]

# 確認用
print(n)
for t in ts:
  print(t)
```

javascript
[解答例](hatsukoi_hair6/test.js)

```js
// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')
// declare variable
const [n, m] = Array.from(lines.slice(0, 2), Number)
const tx = Array.from(lines.slice(2), Number)

// main
//console.log(`n:${n}, m:${m}, tx:[${tx}]`)

```

## EYE

### [たれ目](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_eye2)

python3
[解答例](hatsukoi_eye2/test.py "たれ目")

``` python
[s, n] = [int(_) for _ in input().split()]

# 確認用
print(s, n)
```

javascript
[解答例](hatsukoi_eye2/test.js "たれ目")

```js
// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// declare variable
const [s, n] = Array.from(lines, Number)

// Main 
// console.log(`s:${s}, n:${n}`)


```

### [つり目](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_eye3)

python3
[解答例](hatsukoi_eye3/test.py "つり目")

```python
p = int(input())

# 確認用
print(p)
```

javascript
[解答例](hatsukoi_eye3/test.js "つり目")

```js
// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// declare variable
const p = parseInt(lines[0])

// Main 
// console.log(`p:${p}`)

```

### [めがね](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_eye4)

[解答例](hatsukoi_eye4/test.py "めがね")

``` python
N = int(input())
alist = map(int,input().split()[:N])

# 確認用
for a in alist: 
  print(a)
```

javascript
[解答例](hatsukoi_eye4/test.py "めがね")

```js
// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// declare variable
const N = parseInt(lines[0])
const alist = Array.from(lines.slice(1, N), Number)

// Main 
// console.log(`N:${N}, alist:${alist}`)

```

## CLOTHES

### [cute衣装](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes2)

python3
[解答例](hatsukoi_clothes2/test.py "Cute衣装")

``` python
[n, m] = [int(_) for _ in input().split()]

# 確認
print(n, m)
```

javascript
[解答例](hatsukoi_clothes2/test.js "Cute衣装")

```js
// stream to array
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// declare variable
const [n, m] = Array.from(lines, Number)

// Main 
// console.log(`n:${n}, m:${m}`)

```

### [sexy衣装](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes3)

Python3
[解答例](hatsukoi_clothes3/test.py "Sexy衣装")

```python
N, M = [int(_) for _ in input().split()]

# 確認
print(N, M)
```

javascript
[解答例](hatsukoi_clothes3/test.js "Sexy衣装")

```js
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// declare variable
const [N, M] = Array.from(lines[0].split(' '), Number)

// Main 
// console.log(`N:${N}, M:${M}`)
```

### [制服](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes5)

python3
[解答例](hatsukoi_clothes5/test.py "制服")

``` python
cs = input().split()

# 確認
for c in cs:
  print(c)

```

javascript
[解答例](hatsukoi_clothes5/test.py "制服")

```js
const lines = require('fs').readFileSync('/dev/stdin', 'utf8')
  .toString().trim().split('\n')

// declare variable
const cs = lines

// Main 
// console.log(`cs:${cs}`)

```

### [浴衣](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes6)

python3
[解答例](hatsukoi_clothes6/test.py "浴衣")

``` python
N = int(input())
ts = [input().split() for _ in range(N)]

for [t, s] in ts:
  # 確認
  print(int(t), s)

```

## SPECIAL

### [水着](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_special2)

python3
[解答例](hatsukoi_special2/test.py "水着")

``` python
n, m = map(int, input().split())
s, t = [input() for _ in range(2)]

# 確認
print(n, m, s, t)
```

javascript
[解答例](hatsukoi_special2/test.js "水着")


### [マイク](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_special5)

python3
[解答例](hatsukoi_special5/test.py "マイク")

``` python
[n, m] = [int(input()) for _ in range(2)]

# 確認
print(n, m)
```

javascript
[解答例](hatsukoi_special5/test.js "マイク")

```js
```

### [カチューシャ](https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_special6)

python3
[解答例](hatsukoi_special6/test.py "カチューシャ")

```py
[[n, p], [m, q]] = [map(int, input().split()) for _ in range(2)]

# 確認
print(n, p, m, q)

```

javascript
[解答例](hatsukoi_special6/test.js "カチューシャ")

```js

```
