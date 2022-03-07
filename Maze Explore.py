# 미로 탐색
# boj 2178

# N x M의 배열로 된 미로가 있다
# 1은 이동 가능, 0은 이동 불가
# (1, 1)에서 출발하여 (N, M)으로 이동할 때
# 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오

# Answer

from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = input().split()
N = int(N)
M = int(M)
board = [input() for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        y, x, d = dq.popleft()
        if y == N - 1 and x == M - 1:
            return d
        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))


print(bfs())





# maze = []
# print(N, M)
# for i in range(N):
#     maze[i] = []
#     for j in range(M):
#         maze[i][j] = 1
# print(maze)



