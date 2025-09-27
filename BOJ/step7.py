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
#import sys

#li = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
#li_max = []
#idx_1=0
#idx_2=0

#for i in range(9):
#    li_max.append(max(li[i]))

#idx_1=li_max.index(max(li_max))
#idx_2=li[idx_1].index(max(li_max))

#print(max(li_max))
#print(idx_1 + 1, idx_2 + 1)    

# 10798
#import sys

#li=[sys.stdin.readline().strip() for _ in range (5)]

#for i in range(15):
#    for j in range(5):
#        try:
#            print(li[j][i], end='')        out.append(li[j][i]) -> print('', join(out))
#        except IndexError:
#            continue

# max_len = max(len(s) for s in li) -> li행의 최대길이를 구할 수 있음.

                                    
# 2563
#n = int(input())                    브루트포스

#li=[[0]*100 for _ in range(100)]

#for i in range(n):
#    x, y = map(int, input().split())
#    for k in range(x, x+10):
#        for m in range(y, y+10):
#            li[k][m] = 1

#count=0
#for i in range(100):
#    for j in range(100):
#        if li[i][j]==1:
#            count+=1

#print(count)

#n= int(input())                set
#covered  =set()

#for i in range(n):
#    x, y = map(int, input().split())
#    for k in range(x, x+10):
#        for m in range(y, y+10):
#            covered.add((k, m))
#            
#print(len(covered))