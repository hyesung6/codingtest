# boj 10844

# N 이 주어질 때 , 길이가 N인 계단 수가 총 몇 개 있는지 구하시오

# 입력 첫째 줄에 N이 주어진다. 1 =< N < 100

# 출력 첫째 줄에 정답을 1_000_000_000으로 나눈 나머지를 출력



MOD = 1_000_000_000

cache = [[0] * 10 for _ in range(101)]
for j in range(1, 10):
    cache[1][j] = 1

for i in range(2, 101):
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i - 1][j - 1]
            cache[i][j] %= MOD
        if j < 9:
            cache[i][j] += cache[i - 1][j + 1]
            cache[i][j] %= MOD

ans = 0
N = int(input())
for j in range(10):
    ans += cache[N][j]
    ans %= MOD

print(ans)
