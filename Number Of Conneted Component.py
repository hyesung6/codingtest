# boj 11724

# 무방향 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램을 작성하시오

# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# ( 1 < N < 1000,  0 < M < N * (N-1) / 2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# 같은 간선은 한 번만 주어진다.

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)