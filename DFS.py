# DFS
# Depth First Search
# 깊이 우선 탐색

# 스택 or 재귀를 사용해서 구현한다

# DFS는 완전탐색 방식이다

adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
# ...
# for row in adj:
#     print(row)

def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:    # 간선이 있으면 재귀를 도는 방식
            dfs(nxt)

