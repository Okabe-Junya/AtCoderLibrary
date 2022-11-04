# 数学用ライブラリ

## 各位の和

【概要】

引数で与えられた数字の各位の和を返す．例えば，引数として$123$を与えると，$1 + 2 + 3 = 6$ が返される．

【コード】

```python
def n_sum(n):
    return sum([int(i) for i in list(str(n))])
```

## n進数変換

【概要】

第一引数に与えられた数値を，第二引数に与えられた基数に変換して返す．例えば10進数の$5$を2進数変換すると$101_{(2)}$となるため，101が返される．

【コード】

```python
```

【サンプル】

```python
>>> base_n(5, 2)
101

>>> base_n(7, 4)
13
```

## 10進数変換

【概要】  
第一引数に与えられた数値を，10進数に変換して返す．基数は第二引数で与える．例えば，2進数の$101_{(2)}$を10進数変換すると$5$となるため，5が返される．

【コード】

```python
```

【サンプル】

```python
>>> base_10(101, 2)
5

>>> base_10(13, 4)
7
```

## 最大公約数

### 2数の最大公約数

【概要】  
`gcd` では引数で与えられた2つの数値の最大公約数を返す．例えば，12と18の最大公約数は6であるため，6が返される．ユークリッドの互除法を用いて実装されているため，2つの引数 $a,\, b$ に対して $O(\log\min(a,\,b))$ の計算量で動作する．

【コード】

```python
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)
```

【サンプル】

```python
>>> gcd(12, 18)
6

>>> gcd(33, 22)
11
```

### 複数の数の最大公約数

【概要】  
`gcd_list` では，引数で与えられたリストの最大公約数を返す．

【コード】

```python
def gcd_list(l):
    res = l[0]
    for num in l:
        res = gcd(res, num)
    return res
```

【サンプル】

```python
>>> gcd_list([12, 18, 6])
6
```

## 最小公倍数

【概要】  
`lcm` では引数で与えられた2つの数値の最小公倍数を返す． `lcm_list` では，引数で与えられたリストの最小公倍数を返す．

【コード】

```python
def lcm(a, b):
    return a * b // gcd(a, b)
```

```python
def lcm_list(l):
    res = l[0]
    for i in l:
        res = lcm(res, i)
    return 
```

【サンプル】

```python
>>> lcm(12, 18)
36

>>> lcm(33, 22)
66
```

```python
>>> lcm_list([12, 18, 6])
36
```

## 階乗

【概要】  
引数で与えられた数値の階乗を返す．再帰を用いて実装されており，引数 $n$ に対して $O(n)$ で動作する．

【コード】

```python
def factorial(n):  # n > 0
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

【サンプル】

```python
>>> factorial(5)
120

>>> factorial(7)
5040
```

## 順列

【概要】  
第一引数を $n$，第二引数を $r$ としたとき，$_nP_r$を返す．

【コード】

```python
def permutation(n, r):  # n > 0, r <= n
    return factorial(n) // factorial(n - r)
```

【サンプル】

```python
>>> permutation(5, 3)
60

>>> permutation(10, 2)
90
```

## 組合せ

【概要】  
第一引数を $n$，第二引数を $r$ としたとき，$_nC_r$を返す．

【コード】

```python
def cmb(n, r):  # n > 0, r <= n
    return factorial(n) // (factorial(n - r) * factorial(r))
```

【サンプル】

```python
>>> cmb(5, 3)
10

>>> cmb(10, 2)
45
```

## エラトステネスの篩

【概要】  
引数で与えられた数値以下の素数をリストとして返す．

【コード】

```python
```

【サンプル】

```python
>>> sieve(10)
[False, True, True, False, True, False, True, False, False, False, True], [2, 3, 5, 7]

>>> sieve(5)
([False, True, True, False, True, True], [2, 3, 5])
```

## 素因数分解

【概要】  
引数で与えられた数値の約数をリストで返す．ただし，$n = \Pi_{i=1}^k a_i^{b_i}$ であるとき，$[[a_1,\, b_1],\cdots [a_k,\, b_k]]$ の形式で返される．

【コード】

```python
```

【サンプル】

```python
>>> factorization(9)
[[3, 2]]

>>> factorization(10)
[[2, 1], [5, 1]]

>>> factorization(48)
[[2, 4], [3, 1]]
```

## 約数列挙

【概要】  
引数で与えられた数値の約数をリストで返す．

【コード】

```python
```

【サンプル】

```python
>>> make_divistors(9)
[1, 3, 9]

>>> make_divistors(48)
[1, 2, 3, 4, 6, 8, 12, 16, 24, 48]
```

## 冪乗の剰余

【概要】  
第一引数を $n$，第二引数を $m$，第三引数を $p$ としたとき，$n^m \mod\, p$ を返す．

【コード】

```python
```

【サンプル】

```python
>>> pos(2, 5, 3)
2

>>> pos(10, 4, 100)
0
```

## 逆元計算

【概要】  
第一引数を $a$，第二引数を $p$ としたとき，$a^{-1} \mod\, p$ を返す．

【コード】

```python
def inv(a, m):  # a < m, mが素数
    def pos(x, n, m):
        if n == 0:
            return 1
        res = pos((x ** 2) % m, n // 2, m)
        if n % 2 == 1:
            res = res * x % m
        return res
    return pos(a, m - 2, m)
```

【サンプル】

```python
```

## 拡張ユークリッドの互除法

【概要】  
引数 $(a,b)$ の組に対して $ax + by = \gcd(a, b)$ の解を求める（ただし $a, b$ は互いに素であるとする）．

【コード】

```python
def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = ext_gcd(b, a % b)
        return y, x - (a // b) * y, g
```

【サンプル】

```python
```

## 二項係数の剰余

【概要】  
引数の組 $(n,k,p)$ に対して，$n^k \mod\, p$ を返す．

【コード】

```python
def cmb_mod(n, k, p):
    def permutation(n, r):
        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n - 1)
        return factorial(n) // factorial(n - r)

    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    def inv(a, m):  
        def pos(x, n, m):
            if n == 0:
                return 1
            res = pos((x ** 2) % m, n // 2, m)
            if n % 2 == 1:
                res = res * x % m
            return res
        return pos(a, m - 2, m)

    fact_k = factorial(k)
    invk = inv(fact_k, p)
    return (permutation(n, k) % p) * invk % p
```

【サンプル】

```python
```
