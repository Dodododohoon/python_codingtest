##BackTracking

# 15649 - 바로 안 떠올랐음.
# import sys
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# n, m = map(int, input().split())
# visited = [False] * (n+1)
# arr=[]

# def BT(num):
#    if num == m:
#        print(' '.join(map(str, arr)))
#        return
#    for i in range(1,n+1):
#        if visited[i] == False:
#            visited[i] = True
#            arr.append(i)
#            BT(num+1)
#            arr.pop()
#            visited[i] = False
#
# BT(0)

# 15650
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# arr=[]

# def bt(k):
#    if len(arr) == m:
#        print(' '.join(map(str, arr)))
#        return
#    for i in range(k,n+1):
#        arr.append(i)
#        bt(i+1)
#        arr.pop()
#
# bt(1)
# ---------------------------------------------------------
##Dynamic Programming - 점화식이 메인
# 2579
# import sys

# input = sys.stdin.readline
# n = int(input())
# arr = [int(input()) for _ in range(n)]
# arr.insert(0,0)

# if n ==1:
#    print(arr[1])
#    exit()
# if n==2:
#    print(arr[1]+arr[2])
#    exit()

# dp = [0] * (n+1)
# dp[1] = arr[1]
# dp[2] = arr[1]+arr[2]


# for i in range(3, n+1):
#    dp[i] = max(dp[i-2], dp[i-3]+arr[i-1]) + arr[i]

# print(dp[n])
# --------------------------------------------------
##Prefix Sum - 1차원은 일단 깔끔, 2차원도 적응해보자.
# 11659
# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())

# li = list(map(int, input().split()))

# prefix = [0] * (n+1)

# for i in range(1,n+1):
#    prefix[i] = prefix[i-1] + li[i-1]

# for _ in range(m):
#    i, j =map(int, input().split())
#    print(prefix[j] - prefix[i-1])

# 11660
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(n)]

# prefix = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#    for j in range(1, n + 1):
#        prefix[i][j] = (
#            prefix[i - 1][j]
#            + prefix[i][j - 1]
#            - prefix[i - 1][j - 1]
#            + arr[i - 1][j - 1]
#        )

# for _ in range(m):
#    x1, y1, x2, y2 = map(int, input().split())
#    print(
#        prefix[x2][y2]
#        - prefix[x1 - 1][y2]
#        - prefix[x2][y1 - 1]
#        + prefix[x1 - 1][y1 - 1]
#    )

# -------------------------------------
# Greedy
# 1931
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = []

# for _ in range(n):
#    x1, x2 = map(int, input().split())
#    arr.append((x1,x2))

# arr.sort(key=lambda x : (x[1], x[0]))

# finish = -1
# cnt = 0

# for a,b in arr:
#    if a >= finish:
#        cnt +=1
#        finish = b

# print(cnt)

# ---------------------------------------------
# Divide & Conquer
# 2630
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n = int(input())

# arr = [list(map(int, input().split())) for _ in range(n)]

# cnt_b = 0
# cnt_w = 0

# def dc(row, col, size):
#     global cnt_b, cnt_w
#     check = arr[row][col]
#     same = True

#     if size == 1:
#         if check:
#             cnt_b +=1
#         else:
#             cnt_w +=1
#         return

#     for i in range(row, row+size):
#         for j in range(col, col+size):
#             if arr[i][j] != check:
#                 same= False
#                 break
#         if arr[i][j] != check:
#             break

#     if same :
#         if check:
#             cnt_b +=1
#         else:
#             cnt_w +=1
#     else:
#         dc(row,col,size//2)
#         dc(row+size//2,col,size//2)
#         dc(row,col+size//2,size//2)
#         dc(row+size//2,col+size//2,size//2)

# dc(0,0,n)
# print(cnt_w)
# print(cnt_b)

# -------------------------------------------------
# Binary Search
# 1920
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# check = list(map(int, input().split()))

# arr.sort()


# def bs(target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return 1
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return 0


# for x in check:
#     print(bs(x))
