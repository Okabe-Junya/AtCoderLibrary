# 標準入力用ライブラリ

## 整数入力

【概要】  
単一の整数入力を受け取る．

【コード】

```python
n = int(input())
```

【サンプル】

## 連続整数入力

【概要】  
連続した整数入力を受け取る．受け取った整数は，独立な変数に格納される．

【コード】

```python
a, b = map(int, input().split())
```

【サンプル】

## 連続整数入力（リスト）

【概要】  
連続した整数入力を受け取る．受け取った整数は，リストに格納される．

【コード】

```python
a = list(map(int, input().split()))
```

【サンプル】

## 改行整数入力

【概要】  
改行を区切りとした整数入力を受け取る．

【コード】

```python
a = [int(input()) for i in range(n)]
```

【サンプル】

## 改行文字列入力

【概要】  
改行を区切りとした文字列入力を受け取る．

【コード】

```python
a = [input() for i in range(n)]
```

【サンプル】

## 複数行2列整数入力

【概要】  
複数行2列の入力を受け取る．各列ごとに，独立な変数に格納される．

【コード】

```python
xy = [map(int, input().split()) for i in range(n)]
x, y = [list(i) for i in zip(*xy)]
```

【サンプル】

## 行列入力

【概要】  
$n\times m$ 行列の入力を受け取る．受け取った行列は2次元配列として格納される．

【コード】

```python
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
```

【サンプル】
