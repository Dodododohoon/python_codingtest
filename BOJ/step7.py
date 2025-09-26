# 2738
# n, m = map(int, input().split())

# li1 = []
# li2 = []
# li_sum = [[0] * m for _ in range(n)]

# for i in range(n):
#     li1.append(list(map(int, input().split())))
# for i in range(n):
#     li2.append(list(map(int, input().split())))

# for i in range(n):
#     for j in range(m):
#         li_sum[i][j] = li1[i][j] + li2[i][j]

# for i in range(n):
#     for j in range(m):
#         print(li_sum[i][j], end=" ")
#     print()
#n, m = map(int, input().split())

#A = [list(map(int, input().split())) for _ in range(n)]
#B = [list(map(int, input().split())) for _ in range(n)]

#for i in range(n):
#    for j in range(m):
#        print(A[i][j] + B[i][j], end=" ")
#    print()

# 2566
import sys

li = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
li_max = []
#num_max=0
idx_1=0
idx_2=0
for i in range(2):
    li_max.append(max(li[i]))

num_max = max(li_max)
idx_1=li_max.index(max(li_max))
idx_2=li[idx_1].index(max(li_max))


    

# 10798

# 2563
