from collections import deque


# 深さ優先探索（グラフ）
def dfs(e, v, seen: list[bool]) -> list[bool]:  # e: エッジの集合，v: ノード，seen: 既に訪れたノードの集合
    seen[v] = True
    m = len(e[0])
    for n in range(m):
        if e[v][n] & (not seen[n]) & (n != v):
            dfs(e, n, seen)
    return seen


# 幅優先探索
def bfs(G, d, queue: deque):
    while queue:
        next = queue.popleft()
        for node in G[next]:
            if d[node] == -1:
                d[node] = d[next] + 1
                queue.append(node)
    return d


# ダイクストラ法
def dijkstra(adj, n, s=0):  # adj: 隣接行列，n: ノード数，s: 始点ノード
    import heapq

    INF = 10**9
    dist = [INF] * n  # 始点からの最短距離
    dist[s] = 0  # 始点ノードの距離は0
    seen = [False] * n  # 既に訪れたかどうか
    tmp = [(0, s)]
    while tmp:
        tmp_v = heapq.heappop(tmp)[1]
        seen[tmp_v] = True
        for t, c in adj[tmp_v]:
            if (dist[t] > dist[tmp_v] + c) & (not seen[t]):
                dist[t] = dist[tmp_v] + c
                heapq.heappush(tmp, (dist[t], t))
    return dist


# ワーシャルフロイド法
def warshall_floyd(d):  # d[i][j]: ノードiからノードjへの距離
    d_min = d.copy()
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d_min[i][j] = min(d_min[i][j], d_min[i][k] + d_min[k][j])
    return d_min


# 二部グラフ判定
def is_bipartite(G: list[list[int]]) -> bool:
    # G: 連結なグラフ
    N = len(G)  # ノード数
    seen = [-1] * N  # 既に訪れたかどうか
    seen[0] = 1
    stack = [0]
    while stack:  # 深さ優先探索
        tmp_node = stack.pop()
        tmp_color = seen[tmp_node]
        for node in G[tmp_node]:
            if seen[node] == -1:
                seen[node] = 1 - tmp_color
                stack.append(node)
            elif seen[node] == tmp_color:
                return False
    return True


# 最小全域木
def prim(adj):
    import heapq

    # adj: 隣接行列
    # adj[i]: i番目のノードに接続するノードのリスト（cost, node）の順
    N = len(adj)  # ノード数
    res_set = set()  # 最小全域木のノード集合
    seen = [False] * N  # 既に訪れたかどうか
    res = 0  # 最小全域木の重みの合計
    heap = [(0, 0)]  # (cost, node)の順でソートするためのheap
    heapq.heapify(heap)
    while heap:
        cost, node = heapq.heappop(heap)
        if seen[node]:
            continue

        seen[node] = True
        res_set.add(node)
        res += cost

        for c, t in adj[node]:
            if not seen[t]:
                heapq.heappush(heap, (c, t))

        if len(res_set) == N:
            break
    return res


# 強連結成分分解
def scc(N, G, RG):
    # RG: G の各辺を反転したグラフ
    post_order = []
    seen = [0] * N
    group = [None] * N

    def dfs(v):
        seen[v] = 1
        for t in G[v]:
            if not seen[t]:
                dfs(t)
        post_order.append(v)

    def dfs_reverse(s, cnt):
        group[s] = cnt
        seen[s] = 1
        for t in RG[s]:
            if not seen[t]:
                dfs_reverse(t, cnt)

    for i in range(N):
        if not seen[i]:
            dfs(i)

    seen = [0] * N
    label = 0
    for s in reversed(post_order):
        if not seen[s]:
            dfs_reverse(s, label)
            label += 1

    return label, group
