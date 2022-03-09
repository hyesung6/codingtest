'''

from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3)
four = bisect_right(v, 4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)

print(f'number of 3: {three}')  #2
print(f'number of 4: {four}')  #0
print(f'number of 6: {six}')  #3


'''



# boj 2512
# 국가 예산 배정


# 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때,
# 조건을 만족하도록 예산을 배정하는 프로그램 작성

# 첫째 줄에는 지방의 수 = N ( 3 =< N =< 10000 )
# 다음 줄에 지방의 수만큼 예산요청이 들어옴 ( 빈칸을 사이에 두고 )
# 그 다음 줄에는 총 예산 = M

# 모든 요청이 가능한 경우 요청 금액대로 배정
# 불가능한 경우 특정 정수 상한액만큼 배정

# 배정된 예산 중 최댓값인 정수를 출력


'''
# Answer

N = int(input())

req = list(map(int, input().split()))

M = int(input())

lo = 0
hi = max(req)
mid = (lo + hi) // 2
ans = 0

def is_possible(mid):
    return sum(min(r, mid) for r in req) <= M




while lo <= hi:
    if is_possible(mid):
        lo = mid + 1
        ans = mid

    else:
        hi = mid - 1

    mid = (lo + hi) // 2

print(ans)
'''
