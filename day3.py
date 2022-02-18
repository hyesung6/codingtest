import heapq as hq

N = int(input())
heapArr = []

for _ in range(N):
    for x in eval(input("튜플 형식으로 입력해주세요 :")):
        if x != 0:
            hq.heappush(heapArr, x)
        elif x == 0:
            hq.heappop(heapArr)

print(heapArr)


# 배열에 정수를 넣는다
# 0은 제외
#
# 배열에서 절댓값이 가장 작은 값을 출력하고
# 그 값을 배열에서 제거한다
# 가장 작은 값이 여러개일때에는
# 가장 작은 수를 출력하고 배열에서 제거한다.
# 프로그램은 비어있는 배열에서 시작한다.


"""
# Answer

import heapq as hq
import sys

input = sys.stdin.readilne
min_heap = [] # 양수
max_heap = [] # 음수
for _ in range(int(input())):
    x = int(input())
    if x:
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(hq.heappop(max_heap))
            else:
                print(0)

"""