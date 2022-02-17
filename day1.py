

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
    
    print('YES' if isVPS else 'NO')
"""
