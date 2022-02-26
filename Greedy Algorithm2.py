# boj 1449

# 물이 새는 곳 개수 N
# 테이프 길이 L

# 물은 파이프의 가장 왼쪽에서 정수만큼 떨어진 거리만 샘
# 테이프를 이용해 물을 막을 때 그 위치의 좌우 0.5만큼 간격을 줘야함
# 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오

# 첫째 줄에 N, L이 주어짐
# 둘째 줄에는 물이 새는 곳의 위치가 주어진다.


# 구멍이 4개
# 테이프의 길이 2cm
#
# 1 2 100 101

# N, L = input().split()
# N = int(N)
# L = int(L)
#
#
# waterLeakSpot = input()
# waterLeakSpot = list(map(int, waterLeakSpot.split()))
# # print(waterLeakSpot)
# # print(N // L)
#
#
# fixedSpot = 0
# usedTape = 9999
# tapeOnSpotCount = L
#
# for i in waterLeakSpot:
#     if i == usedTape + 1:
#         fixedSpot += 1
#         tapeOnSpotCount -= 1
#     elif i < usedTape:
#         usedTape = i
#         fixedSpot += 1


# ========================================================


# Answer

N, L = map(int, input().split())
coord = [False] * 1001
for i in map(int, input().split()):
    coord[i] = True

ans = 0
x = 0
while x < 1001:
    if coord[x]:
        ans += 1
        x += L
    else:
        x += 1
print(ans)


# 테이프 길이 L은 한 번 붙이면 그만큼의 간격을 덮을 수 있으므로
# 1001까지의 배열에서 True인 자리에 테이프를 붙이고 + L 한 값만큼
# 건너뛰어 계산해도 됨
# Ex) 100번째 자리에 3cm짜리 테이프를 붙이면 101, 102는 계산하지 않아도 됨

# 내가 찾고자 하는 범위의 최대값의 배열을 만들고
# 찾고자 하는 값에 True를 부여하는 방식
# ==> 좌표압축이라 함