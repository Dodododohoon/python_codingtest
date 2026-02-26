# 9095
# import sys
# input = sys.stdin.readline

# t = int(input())

# dp = [0] * 11
# dp[0] = 1
# dp[1] = 1
# dp[2] = 2
# for i in range(3,11):
#    dp[i] = dp[i-1] + dp[i-2] +dp[i-3]

# for _ in range(t):
#    n = int(input())
#    print(dp[n])

# 1697 - 시작값 에러 있음. & 더 짧게 가능.
# import sys
# from collections import deque

# n, k = map(int, input().split())
# time = [0] * 100001

# q = deque([(0,n)])

# while q:
#    t, loc = q.popleft()
#
#    if loc == k:
#        break
#
#    nx = 2*loc
#    if 0 <= nx <= 100000 and time[nx] == 0:
#        time[nx] = t+1
#        q.append((t+1,nx))
#
#    nx = loc +1
#    if 0 <= nx <= 100000 and time[nx] ==0:
#        time[nx] = t+1
#        q.append((t+1,nx))
#
#    nx = loc -1
#    if 0 <= nx <= 100000 and time[nx] == 0:
#        time[nx] = t+1
#        q.append((t+1,nx))

# print(time[k])

# 2293
# import sys
# input = sys.stdin.readline

# n,k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]
# dp = [0] * 10001
# dp[0] = 1

# for coin in coins:
#    for i in range(coin, k+1):
#        dp[i] += dp[i-coin]

# print(dp[k])

# 11052
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# dp = [0]*(n+1)
# dp[1] = arr[0]

# dp[2] = max(dp[1]+arr[0], arr[1])

# for i in range(3,n+1):
#    for j in range(i):
#        dp[i] = max(dp[i], dp[j] + arr[i-j-1])

# print(dp[n])

# 2225
# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())

# dp = [[0] * (k+1) for _ in range(n+1)]

# for i in range(1,k+1):
#    dp[0][i] = 1
# for i in range(1,n+1):
#    dp[i][1] = 1

# for i in range(1,n+1):
#    for j in range(2,k+1):
#        for m in range(i+1):
#            dp[i][j] += dp[m][j-1] % 1000000000
# print(dp[n][k]%1000000000)

# 1309
# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = [0] * (n+1)
# dp[0] = 1
# dp[1] = 3

# for i in range(2, n+1):
#    dp[i] = (2* dp[i-1] + dp[i-2])%9901
# print(dp[n]%9901)

# 9184
# import sys
# input = sys.stdin.readline

# dp =[[[0]*21 for _ in range(21)] for _ in range(21)]

# for i in range(21):
#    for j in range(21):
#        for m in range(21):
#            if i == 0 or j ==0 or m == 0:
#                dp[i][j][m] = 1
#                continue
#            if i<j<m:
#                dp[i][j][m] = dp[i][j][m-1] +dp[i][j-1][m-1] - dp[i][j-1][m]
#            else:
#                dp[i][j][m] = dp[i-1][j][m] + dp[i-1][j-1][m]+dp[i-1][j][m-1]-dp[i-1][j-1][m-1]

# while True:
#    a,b,c = map(int,input().split())
#    if a==-1 and b==-1 and c==-1:
#        break
#    if a <= 0 or b <= 0 or c <= 0:
#        print(f'w({a}, {b}, {c}) = {dp[0][0][0]}')
#        continue
#    if a >20 or b >20 or c > 20:
#        print(f'w({a}, {b}, {c}) = {dp[20][20][20]}')
#    else:
#        print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')

# 1012
# import sys
# from collections import deque
# input =sys.stdin.readline

# t = int(input())

# for _ in range(t):
#    m,n,k = map(int,input().split())
#
#    graph = [[0] * m for _ in range(n)]
#    cnt = 1
#    dx = [1,-1,0,0]
#    dy = [0,0,1,-1]
#
#    for _ in range(k):
#        x, y = map(int,input().split())
#
#        graph[y][x] = 1
#
#    def bfs(a,b,c):
#        q=deque([(a,b)])
#        while q:
#            y, x = q.popleft()
#
#            for i in range(4):
#                nx = x + dx[i]
#                ny = y + dy[i]
#
#                if 0<=nx<m and 0<=ny<n and graph[ny][nx] ==1:
#                    graph[ny][nx] = c
#                    q.append((ny,nx))
#
#    for i in range(n):
#            for j in range(m):
#                if graph[i][j] == 1:
#                    cnt +=1
#                    graph[i][j] = cnt
#                    bfs(i,j,cnt)
#
#    print(cnt-1)


# 1806 - 부분합
# import sys
# input = sys.stdin.readline

# n, s =map(int,input().split())
# arr = list(map(int,input().split()))

# ans = n + 1
# total = 0

# start, end = 0, 0
# while start <= end:
#
#    if end == n-1 and total < s:
#        break
#    if start == end:
#        total = arr[start]
#
#    if total >= s:
#        ans = min(ans, end-start+1)
#        if ans == 1:
#            break
#        total -= arr[start]
#        start +=1
#    else:
#        if end < n-1:
#            end += 1
#            total += arr[end]
#
# if ans == n+1:
#    print('0')
# else:
#    print(ans)

# 1920
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = set(map(int,input().split()))
# m = int(input())
# check = list(map(int,input().split()))

# for x in check:
#    if x in arr:
#        print('1')
#    else:
#        print('0')

# arr.sort()

# for x in check:
#    left, right = 0, len(arr)-1
#
#    while left <= right:
#        half = (left + right)//2
#        num = arr[half]
#
#        if num == x:
#            print('1')
#            break
#        elif num > x:
#            right = half - 1
#        else:
#            left = half + 1
#
#    if num != x:
#        print('0')

# 10816
# import sys
# from bisect import bisect_left, bisect_right
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# check = list(map(int,input().split()))

# arr.sort()

# dic = dict()

# for x in arr:
#    if x in dic:
#        dic[x] +=1
#    else:
#        dic[x] = 1

# for x in check:
#    if x in dic:
#        print(dic[x])
#    else:
#        print('0')

# for x in check:
#    left = bisect_left(arr,x)
#    right = bisect_right(arr,x)
#    if left < n:
#        print(right - left, end=' ')
#    else:
#        print('0', end=' ')

# 1167
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())

# graph = [[] for _ in range(n+1)]

# for _ in range(n):
#    arr = list(map(int, input().split()))
#
#    for i in range(1,len(arr)-1,2):
#        graph[arr[0]].append((arr[i],arr[i+1]))

# def bfs(v):
#    q = deque([(0,v)])
#
#    while q:
#        cur, w = q.popleft()
#
#        for nxt, u in graph[w]:
#            d = cur + u
#            if dist[nxt] == -1:
#                dist[nxt] = d
#                q.append((d,nxt))

# dist = [-1] * (n+1)
# dist[1] = 0
# bfs(1)

# right = dist.index(max(dist))
# dist = [-1] * (n+1)
# dist[right] = 0
# bfs(right)
# print(max(dist))

# 1976
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# parent = [i for i in range(n+1)]

# def find(a):
#    if a != parent[a]:
#        parent[a] = find(parent[a])
#    return parent[a]
#
# def union(a,b):
#    a=find(a)
#    b=find(b)
#    if a==b:
#        return
#    parent[b] = a

# for i in range(n):
#    arr = list(map(int,input().split()))
#    for j in range(len(arr)):
#        if arr[j] == 1:
#            union(i+1,j+1)

# check = list(map(int,input().split()))
# collect = find(check[0])
# for x in check:
#    if collect != find(x):
#        print('NO')
#        exit()
# print('YES')

# 14502
# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(n)]


# def bfs(r1, c1, r2, c2, r3, c3):
#     temp = [list(arr[i]) for i in range(n)]
#     q = deque()
#     temp[r1][c1] = 1
#     temp[r2][c2] = 1
#     temp[r3][c3] = 1
#     cnt = 0

#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]

#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 2:
#                 q.append((i, j))

#     while q:
#         row, col = q.popleft()

#         for i in range(4):
#             x = col + dx[i]
#             y = row + dy[i]

#             if 0 <= x < m and 0 <= y < n and temp[y][x] == 0:
#                 temp[y][x] = 2
#                 q.append((y, x))

#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 cnt += 1
#     return cnt


# ans = 0

# for i in range(n * m - 2):
#     row_i, col_i = i // m, i % m
#     if arr[row_i][col_i] != 0:
#         continue
#     for j in range(i + 1, n * m - 1):
#         row_j, col_j = j // m, j % m
#         if arr[row_j][col_j] != 0:
#             continue
#         for k in range(j + 1, n * m):
#             row_k, col_k = k // m, k % m
#             if arr[row_k][col_k] != 0:
#                 continue

#             ans = max(ans, bfs(row_i, col_i, row_j, col_j, row_k, col_k))

# print(ans)

# 14503
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
# cnt = 0

# while True:
#     check = 0
#     if graph[r][c] == 0:  # 1
#         graph[r][c] = 2
#         cnt += 1

#     for i in range(4):
#         nx = c + dx[i]
#         ny = r + dy[i]

#         if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
#             check = 1
#             break

#     if check == 1:  # 3
#         for i in range(4):
#             d = (d + 3) % 4
#             x = c + dx[d]
#             y = r + dy[d]
#             if graph[y][x] == 0:
#                 c = x
#                 r = y
#                 break

#     if check == 0:  # 2
#         c = c - dx[d]
#         r = r - dy[d]
#         if graph[r][c] == 1:
#             print(cnt)
#             exit()

# 2667
# import sys
# from collections import deque

# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int, input().strip())) for _ in range(n)]

# out = []

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]


# def bfs(row, col):
#     q = deque([(row, col)])
#     graph[row][col] = 0
#     cnt = 1
#     while q:
#         r, c = q.popleft()

#         for i in range(4):
#             nr = r + dy[i]
#             nc = c + dx[i]
#             if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 1:
#                 graph[nr][nc] = 0
#                 cnt += 1
#                 q.append((nr, nc))
#     out.append(cnt)


# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             bfs(i, j)

# out.sort()
# print(len(out))
# print("\n".join(map(str, out)))

# 1918
# import sys
# input = sys.stdin.readline

# s = input().strip()

# prio ={'+':1, '-':1, '*':2, '/':2}

# stack = []
# out=[]

# for x in s:
#   if 'A'<= x <='Z':
#     out.append(x)
#   elif x=='(':
#     stack.append(x)
#   elif x==')':
#     while stack[-1] != '(':
#       out.append(stack.pop())
#     stack.pop()
#   else:
#     while stack and stack[-1] != '(' and prio[stack[-1]] >= prio[x]:
#       out.append(stack.pop())
#     stack.append(x)

# while stack:
#   out.append(stack.pop())

# print(''.join(out))

# 11052
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# dp = [0] * (n+1)

# dp[1] = arr[0]
# if n==1:
#   print(dp[1])
#   exit()

# for i in range(n+1):
#   for j in range(i):
#     dp[i] = max(dp[i], dp[j]+arr[i-j-1])

# print(dp[n])

#
