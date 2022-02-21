# N = int(input())
# bookList = []
# countBook = []
#
# for i in range(N):
#     book = input()
#     bookList.append(book)
#     counter = bookList.count(book)
#     countBook.append(counter)
#
# mostFreq = countBook.index(max(countBook))
# print(bookList[mostFreq]
# print(max(bookList))



# Answer

d = dict()
for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

# print(d.keys())
# print(d.values())
# print(d.items())

m = max(d.values())
candi = []
for k, v in d.items():
    if v == m:
        candi.append(k)

candi.sort()
print(candi[0])

