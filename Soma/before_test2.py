# #2110 - binary search
# import sys

# n, c = map(int, input().split())

# arr = [int(input()) for _ in range(n)]
# arr.sort()

# ans=0
# left = 1
# right = arr[-1]

# while left <= right:
#   mid = (left + right)//2

#   prev = arr[0]
#   cnt = 1
#   dis = 0

#   for x in arr[1:]:
#     dis = x - prev
#     if dis >= mid:
#       cnt += 1
#       dis = 0
#       prev = x

#   if cnt >= c:
#     ans = mid
#     left = mid +1
#   else:
#     right = mid - 1

# print(ans)

# 1753 - dijkstra
# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# v, e = map(int, input().split())
# k = int(input())

# dist = [INF] * (v+1)
# dist[k]=0
# graph = [[] for _ in range(v+1)]

# for _ in range(e):
#   u, v, w = map(int, input().split())
#   graph[u].append((v,w))

# hq = [(0,k)]

# while hq:
#   cur, loc = heapq.heappop(hq)

#   if cur > dist[loc]:
#     continue

#   for nxt, score in graph[loc]:
#     nd = cur + score
#     if dist[nxt] > nd:
#       dist[nxt] = nd
#       heapq.heappush(hq,(nd, nxt))

# for x in dist[1:]:
#   if x == INF:
#     print('INF')
#   else:
#     print(x)

# 1717   - Union Find
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())

# parent = [i for i in range(n+1)]

# def find(a):
#   if a != parent[a]:
#     parent[a] = find(parent[a])
#   return parent[a]

# def union(a,b):
#   a=find(a)
#   b=find(b)

#   if a==b:
#     return

#   parent[b] = a


# for _ in range(m):
#   op, a, b = map(int,input().split())

#   if op ==0:
#     union(a,b)
#   elif op==1:
#     if find(a) == find(b):
#       print('YES')
#     else:
#       print('NO')

# #1197   - MST
# import sys
# import heapq
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# v, e = map(int,input().split())

# parent = [i for i in range(v+1)]
# hq = []
# ans = 0

# def find(a):
#   if a != parent[a]:
#     parent[a] = find(parent[a])
#   return parent[a]


# for _ in range(e):
#   a,b,c = map(int,input().split())
#   heapq.heappush(hq, (c,a,b))

# while hq:
#   w, a, b = heapq.heappop(hq)

#   a = find(a)
#   b = find(b)

#   if a == b:
#     continue

#   parent[b] = a
#   ans += w
#                cnt 추가해주면 좋음. if cnt == v-1 -> break

# print(ans)

# 1806
# import sys
# input = sys.stdin.readline

# n, s = map(int,input().split())
# arr = list(map(int,input().split()))

# if arr[0] >=s:    #애초에 첫항이 s보다 크면 1이니깐 끝.
#   print('1')
#   exit()

# l = 0
# i=1
# j=0
# num = arr[i] + arr[j]     #초기값.
# ans = 100001

# while j <= i and i <= n-1:    # j가 i보다 크면 끝, i가 인덱스 넘어가면 끝.
#   if ans ==1:
#     print('1')
#     exit()

#   if num >= s:    #합이 s보다 크면.  j를 오른쪽으로.
#     if j == n-1:  #그전에 j가 인덱스 끝이면. i=n-1이고 길이가 1이니깐. 끝
#       print('1')
#       exit()
#     ans = min(ans, i-j+1)   #이때 길이가 정답이니깐.
#     num -= arr[j]     #합에서 j빼고
#     j+=1              #j를 오른쪽으로 한칸.
#   else:             #합이 s보다 작으면 i를 오른쪽으로
#     if i==n-1:      #i가 인덱스 끝인데 합이 s보다 작으면 끝.
#       break
#     i+=1
#     num += arr[i]   #그리고 합에다가 i더하고

# if j>i:
#     print('1')
#     exit()

# if ans == 100001:
#   print('0')
# else:
#   print(ans)

# 2470     -  투포인터
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# arr.sort()

# i=0
# j=n-1

# m = int(2e9)
# m_i = 0
# m_j = 0

# while i<j:
#   total = arr[i] + arr[j]

#   if total ==0:   #합이 0이면 바로 출력 끝.
#     print(arr[i], arr[j])
#     exit()
#   elif total >0: #합이 0보다 크면. 양수를 줄인다. j를 왼쪽으로
#     if m> total:
#       m = total
#       m_i = i
#       m_j = j
#     j-=1
#   else:          #합이 0보다 작으면. 음수를 줄인다. i를 오른쪽으로
#     if m> abs(total):
#       m = abs(total)
#       m_i = i
#       m_j = j
#     i+=1

# print(arr[m_i], arr[m_j])


# #2178 - bfs
# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n,m = map(int,input().split())

# graph = [list(map(int, input().strip())) for _ in range(n)]
# score = [[10000]*m for _ in range(n)]

# dr = [1,-1,0,0]
# dc = [0,0,1,-1]

# q = deque([(0,0,0)])
# score[0][0] = 1

# while q:
#   s, row, col = q.popleft()

#   for i in range(4):
#     nr = row + dr[i]
#     nc = col + dc[i]

#     if 0<= nr < n and 0<= nc <m and graph[nr][nc] == 1:
#       graph[nr][nc]=2
#       score[nr][nc]=min(score[nr][nc], score[row][col] + 1)

#       if nr ==n-1 and nc ==m-1:
#         print(score[n-1][m-1])
#         exit()

#       q.append((s+1,nr,nc))


# #1916 - 다익스트라
# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n+1)]
# dist = [INF] * (n+1)

# for _ in range(m):
#   a,b,c = map(int,input().split())

#   graph[a].append((b,c))

# start, end = map(int,input().split())

# dist[start]=0
# hq = [(0,start)]

# while hq:
#   cur, loc = heapq.heappop(hq)

#   if cur > dist[loc]:
#     continue

#   for nxt, cost in graph[loc]:
#     nd = cur + cost
#     if nd < dist[nxt]:
#       dist[nxt] = nd
#       heapq.heappush(hq,(nd,nxt))

# print(dist[end])
