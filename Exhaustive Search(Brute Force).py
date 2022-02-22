# day5
# Exhaustive Search - Brute Force
# 무차별 대입

# 장점 : 반드시 답을 찾을 수 있다.
#       답이 없으면 없는 대로 답이 없다는 성과를 얻을 수 있음

# 단점 : 자원을 많이 잡아먹고 오래 걸림



# 순열(Permutation)
# 모든 경우의 수를 순서대로 살펴볼 때 용이하다

# 0 1 2 3
# 0 1 3 2
# 0 2 1 3 ...

"""
from itertools import permutations
v = [0, 1, 2, 3]
for i in permutations(v, 4):
    print(i)
"""




# 조합 ( Combination )
# 인자로 들어온 갯수로 이루어진 쌍이 나올 수 있는 모든 경우의 수를 추출
# v / 2 + (v-1) / 1

"""
from itertools import combinations
v = [0, 1, 2, 3]
for i in combinations(v, 2):
    print(i)
"""

# boj 2309

# 아홉 난쟁이가 있다
# 일곱 난쟁이의 키의 합은 100이다
# 아홉 난쟁이의 키가 주어졌을 때
# 합이 100인 경우를 찾는다
# 100이 아닌 경우는 없다

from itertools import combinations

heights = [int(input()) for _ in range(9)]

for i in combinations(heights, 7):
    if sum(i) == 100:
        for realDwarfs in sorted(i):
            print(realDwarfs)

        break




# 정리
# 시간초과 나지 않을지 확인
# 될 거 같으면 완전탐색으로 문제를 푼다.
