n, m = map(int, (input().split()))
# N : 바구니 갯수, M : M번 공을 넣는다
i_values = []
j_values = []
k_values = []
for _ in range(m):
    i, j, k = map(int, (input().split()))
    i_values.append(i)
    j_values.append(j)
    k_values.append(k)
# K : 층수, N : 호수
basket = [0 for _ in range(n)] # n = 5 [0, 0, 0, 0, 0]

def NOP(i, j, k):
    for x in range(i - 1, j):
        basket[x] = k

for x in range(m):
    NOP(i_values[x], j_values[x], k_values[x])

for i in basket:
    print(i, end=' ')
