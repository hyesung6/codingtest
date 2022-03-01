# BFS
# Breadth First Search
# 너비 우선 탐색

# 큐를 사용하여 구현

# 상위 노드를 큐에서 팝 하면서
# 하위 노드를 푸쉬하는 식으로

#            0              # 1번째에 여기까지 탐색
#        1        2         # 2번째에 여기까지 탐색
#     3    4   5    6       # 3번째에 여기까지 탐색
#   7   8  9     10 11 12   # 4번째에 여기까지 탐색

# 깊이 우선 탐색과 다르게 루트로부터 간선 갯수가 같은 노드끼리 먼저 탐색함



from collections import deque

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1

def dfs():
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)




# DFS & BFS

# 둘 다 모두 완전탐색이다
# 느리다.


# 서로 탐색 순서가 다르다

# DFS는 항상 모든 경우를 찾아야 함

# BFS가 최장 거리 탐색에 있어서는
# 찾는 자료를 발견 즉시 종료하게 되므로
# 좀 더 빠를 여지가 있음
