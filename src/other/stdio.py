# 整数入力1
n = int(input())

# 連続int
a, b = map(int, input().split())

# 連続入力list (int)
a = list(map(int, input().split()))

# 改行int
a = [int(input()) for i in range(n)]

# 改行文字列
a = [input() for i in range(n)]

# 複数行2列int
xy = [map(int, input().split()) for i in range(n)]
x, y = [list(i) for i in zip(*xy)]


# 複数列2行int
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# nm行列(int)
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
