# 그래프 자료구조

# 인접행렬과 인접리스트로 구현할 수 있다

# 0 1 1 1
# 1 0 1 0
# 1 1 0 1
# 1 0 1 0

# 인접행렬은 데이터 하나가 추가될 때마다 행과 열에 추가해야하므로
# 공간을 많이 쓰게 됨





# 0 | >1>2>3
# 1 | >2
# 2 |
# 3 | >2

# 인접리스트는 값이 있는지 확인하기 위해서는 직접 모든 노드를 돌아야 함






# 인접행렬은 시간적으로 유리하다
# 인접리스트는 공간적으로 유리하다

# 정점에 비해 간선이 적게 등장하면
# 시간을 크게 잡아먹지 않으므로 인접리스트를 사용하거나
# ex) N개 정점에 2N개 간선

# 정점에 비해 간선이 많이 등장하면
# 인접행렬을 써서 빠르게 자료에 접근할 수 있게 한다
# ex) N개 정점에 N 제곱개 간선
