T = int(input())
for i in range(T):
    VPS = []
    for j in input():


# 이전 요소와 다른 요소가 들어오면 YES, 같은 요소가 반복되면 NO








"""
# Answer
T = int(input())
for i in range(T):
    stk = []
    isVPS = True
    for j in input():
        if j == '(':
            stk.append(j)
        else:
            if len(stk) > 0:
                stk.pop()
            else:
                isVPS = False
                break

    if len(stk) > 0:
        isVPS = False
"""
