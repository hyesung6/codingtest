# boj 11726

# 2xN 크기의 직사각형을 1 x 2, 2 x 1 타일로 채우는 방법의 수를 구하는 프로그램 작성
# 입력 첫째 줄에는 n이 주어진다.


# 출력 첫째 줄에 2xN 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.


MOD = 10_007

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD


print(dp[n])