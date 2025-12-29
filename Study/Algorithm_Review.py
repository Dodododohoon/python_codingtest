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

# 15649
# import sys
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# n, m = map(int, input().split())

# visited = [False] * (n+1)
# out = []

# def bt():
#    if len(out) == m:
#        print(' '.join(map(str, out)))
#        return
#
#    for i in range(1,n+1):
#        if visited[i]:
#            continue
#        else:
#            visited[i] = True
#            out.append(i)
#            bt()
#        out.pop()
#        visited[i]=False

# bt()

#9663
#import sys
#input = sys.stdin.readline

#n = int(input())

#col = [False] * (n)
#right = [False] * (2*n-1)
#left = [False] * (2*n-1)

#cnt =0

#def bt(k):
#    global cnt
#    global n
#    
#    if k == n:
#        cnt +=1
#        return
#    
#    for j in range(n):
#        r = j-k+(n-1)
#        l = j+k
#        
#        if col[j] or right[r] or left[l]:
#            continue
#        
#        col[j] = right[r] = left[l] = True
#        bt(k+1)
#        col[j] = right[r] = left[l] = False
#                
#bt(0)
#print(cnt)
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

# -------------------------------------------------
# Prioity Queue
# 11279
# import sys
# import heapq
# input = sys.stdin.readline

# hq = []

# n = int(input())

# for _ in range(n):
#    x = int(input())
#
#    if x == 0:
#        if hq:
#            print(-heapq.heappop(hq))
#        else:
#            print('0')
#    else:
#        heapq.heappush(hq, -x)

# ---------------------------------------
# Two Pointer
# 3273
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))
# x = int(input())

# arr.sort()

# left = 0
# right = len(arr)-1
# cnt =0

# while left<right:
#    sum = arr[left] + arr[right]
#    if sum == x:
#        cnt +=1
#        left +=1
#        right -= 1
#    elif sum>x:
#        right-=1
#    else:
#        left +=1

# print(cnt)

# --------------------------------------
# Depth First Search
# 24479
# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n, m, r = map(int, input().split())

# graph = [[] for _ in range(n + 1)]
# visited = [0] * (n + 1)

# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# for i in range(n):
#     graph[i].sort()

# cnt = 1
# visited[r] = 1


# def dfs(start):
#     global cnt
#     for x in graph[start]:
#         if visited[x] == 0:
#             cnt += 1
#             visited[x] = cnt
#             dfs(x)

# dfs(r)

# print("\n".join(map(str, visited[1:])))

# ------------------------------------------
# Breadth First Search
# 24444
# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m, r = map(int, input().split())

# q = deque()
# graph = [[] for _ in range(n + 1)]
# visited = [0] * (n + 1)

# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# for i in range(n + 1):
#     graph[i].sort()


# def bfs():
#     global cnt
#     while q:
#         start = q.popleft()

#         for x in graph[start]:
#             if visited[x] == 0:
#                 cnt += 1
#                 visited[x] = cnt
#                 q.append(x)

# q.append(r)
# visited[r] = 1
# cnt = 1

# bfs()
# print("\n".join(map(str, visited[1:])))

# -------------------------------------
# Shortest Path
# 1753
#import sys
#import heapq

#input = sys.stdin.readline

#INF = int(1e9)

#v, e = map(int, input().split())
#k = int(input())
#hq = [(0, k)]

#graph = [[] for _ in range(v + 1)]
#visited = [INF] * (v + 1)
#visited[k] = 0

#for _ in range(e):
#    a, b, c = map(int, input().split())
#    graph[a].append((c, b))

#for i in range(1, v + 1):
#    graph[i].sort()

#while hq:
#    cur_dist, start = heapq.heappop(hq)

#    if visited[start] < cur_dist:
#        continue

#    for w, nxt in graph[start]:
#        nd = cur_dist + w
#        if visited[nxt] > nd:
#            visited[nxt] = nd
#            heapq.heappush(hq, (nd, nxt))

#for i in range(1, v + 1):
#    if visited[i] == INF:
#        print("INF")
#    else:
#        print(visited[i])


# 1753
# import sys
# import heapq

# input = sys.stdin.readline
# hq = []
# INF = int(1e9)

# v, e = map(int, input().split())
# k = int(input())

# graph = [[] for _ in range(v+1)]
# dist = [INF] * (v+1)
# dist[k] = 0

# for _ in range(e):
#    a,b,c = map(int, input().split())
#    graph[a].append((b,c))

# heapq.heappush(hq, (0,k))

# while hq:
#    cur_dist, u = heapq.heappop(hq)
#
#    for nxt, w in graph[u]:
#        nd = cur_dist + w
#        if nd < dist[nxt]:
#            dist[nxt] = nd
#            heapq.heappush(hq, (nd,nxt))

# for i in range(1,v+1):
#    if dist[i] == INF:
#        print('INF')
#    else:
#        print(dist[i])

# --------------------------------------------------------
# Union Find
# 1717
# import sys
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# n,m=map(int, input().split())

# parent = [i for i in range(n+1)]
# rank = [0]*(n+1)

# def find(x):
#    if parent[x] != x:
#        parent[x] = find(parent[x])
#    return parent[x]

# def union(a,b):
#    a = find(a)
#    b = find(b)
#
#    if a==b:
#        return
#
#    if rank[b] > rank[a]:
#        parent[a] = b
#    else:
#        parent[b] = a
#        if rank[a] == rank[b]:
#            rank[a] += 1

# for _ in range(m):
#    a, b, c = map(int, input().split())
#    if a == 0:
#        union(b,c)
#    else:
#        if find(b) == find(c):
#            print("YES")
#        else:
#            print("NO")

#1976
#import sys
#sys.setrecursionlimit(10**6)

#input = sys.stdin.readline

#n = int(input())
#m = int(input())

#parent = [i for i in range(n+1)]
#graph = [list(map(int, input().split())) for _ in range(n)]
#plan = list(map(int, input().split()))
#status = True

#def find(r):
#    if parent[r] != r:
#        parent[r] = find(parent[r])
#    return parent[r]

#def union(a,b):
#    a = find(a)
#    b = find(b)
#    
#    if a != b:    
#        parent[b] = a

#for i in range(n):
#    for j in range(n):
#        if graph[i][j] == 1:
#            union(i+1,j+1)

#root = find(plan[0])

#for x in plan:
#    if root != find(x):
#        status = False
#        break

#if status:
#    print('YES')
#else:
#    print('NO')

# ------------------------------------------------------------------
# Minimum Spanning Tree (MST)
# 1197
# import sys
# import heapq
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# v, e = map(int, input().split())
# hq = []
# cnt =0

# parent = [i for i in range(v+1)]
# rank = [0] * (v+1)

# for _ in range(e):
#    a,b,c = map(int, input().split())
#    heapq.heappush(hq, (c,a,b))
#
# def find(r):
#    if parent[r] != r:
#        parent[r] = find(parent[r])
#    return parent[r]

# def union(a,b):
#    a=find(a)
#    b=find(b)
#
#    if a==b:
#        return
#
#    if rank[a] > rank[b]:
#        parent[b] = a
#    else:
#        parent[a] = b
#        if rank[a] == rank[b]:
#            rank[b] += 1
#
# while hq:
#    c, a, b = heapq.heappop(hq)
#
#    if find(a) == find(b):
#        continue
#    else:
#        union(a,b)
#        cnt+=c

# print(cnt)
