# 2738
n, m = map(int, input().split())

li1 = [] * n
li2 = [] * m
li_sum = [[0] * n for _ in range(n)]

for i in range(n):
    li1.append(list(map(int, input().split())))
for i in range(m):
    li2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        li_sum[i][j] = li1[i][j] + li2[i][j]

for i in range(n):
    for j in range(n):
        print(li_sum[i][j], end=" ")
    print()


# 2566

# 10798

# 2563
