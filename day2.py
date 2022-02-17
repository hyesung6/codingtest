# N 만큼
# N=4인 경우
# 위에서부터 1234 카드가 있고
# 1을 버리고 2를 가장 밑으로 옮겨 342를 만든다
# 1장이 남을 때까지 반복한다.


N = int(input())

card = range(1, N+1)
deck = []
for i in card:
    deck.append(i)

while len(deck) > 1:
    del deck[0]
    deck.append(deck[0])
    del deck[0]

print(deck[0])
