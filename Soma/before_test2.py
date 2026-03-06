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

# 1806    - 투포인터
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

# 1644  - 투포인터, 소수
# import sys

# input = sys.stdin.readline

# n = int(input())

# is_prime = [True] * (n + 1)

# is_prime[0] = False
# is_prime[1] = False

# p = 2
# while p * p <= n:
#     if is_prime[p]:
#         step = p
#         start = p * p  # p*p-1은 이미 전에서 지워짐. ex. 5*3은 3일때 이미 없어짐.
#         for i in range(start, n + 1, step):
#             is_prime[i] = False
#         # is_prime[start:n+1:step] = [False] * (((n - start) // step) + 1) 훨씬 빠르긴 함.
#     p += 1

# prime = []
# for i in range(2, n + 1):
#     if is_prime[i]:
#         prime.append(i)

# cnt = 0
# total = 0
# left = 0

# for right in range(len(prime)):
#     total += prime[right]
#     while total >= n:
#         if total == n:
#             cnt += 1
#         total -= prime[left]
#         left += 1

# print(cnt)
# -----------------
# s = set(i for i in range(3, n + 1, 2))
# s.add(2)

# for i in range(3, n + 1, 2):
#     if i in s:
#         num = 0
#         k = 2
#         while num <= n:
#             num = i * k
#             if num in s:
#                 s.remove(num)
#             k += 1

# li = list(s)
# li.sort()

# cnt = 0
# total = 0
# left = 0

# for right in range(len(li)):
#     total += li[right]
#     while total >= n:
#         if total == n:
#             cnt += 1
#         total -= li[left]
#         left += 1

# print(cnt)

# 2206 - bfs
# import sys
# from collections import deque
# input = sys.stdin.readline

# n,m = map(int,input().split())

# graph = [list(map(int, input().strip())) for _ in range(n)]
# dist = [[[0]*2 for _ in range(m)] for _ in range(n)]
# #벽을 뚫고 해당지점에 먼저 도착한 애보다
# #아직 벽을 안 뚫고 해당지점에 도착한 애가 더 빠를 수 있음. 아직 벽을 뚫을 수 있으니.
# dist[0][0][0]=1

# dr = [1,-1,0,0]
# dc = [0,0,1,-1]

# q=deque([(0,0,0)])

# while q:
#   row, col, brk = q.popleft()

#   if row == n-1 and col ==m-1:
#     print(dist[row][col][brk])
#     exit()

#   for i in range(4):
#     nr = row + dr[i]
#     nc = col + dc[i]

#     if not (0<= nr <n and 0<=nc<m):
#       continue

#     if graph[nr][nc] ==0 and dist[nr][nc][brk] ==0:  #다음칸 빈칸일 때
#       dist[nr][nc][brk] = dist[row][col][brk] + 1
#       q.append((nr,nc,brk))

#     elif graph[nr][nc] ==1 and dist[nr][nc][1] ==0 and brk ==0:
#       #다음칸 벽일때 아직 안뚫었고, 이미 한번 뚫은애가 안 지나갔으면
#       dist[nr][nc][1] = dist[row][col][brk] + 1
#       q.append((nr,nc,1))

# print('-1')

# 10986  - prefix, dict
# import sys
# input =sys.stdin.readline

# n,m = map(int, input().split())
# arr = list(map(int,input().split()))

# prefix = [0] * (n+1)

# for i in range(1,n+1):
#   prefix[i] = (prefix[i-1]+arr[i-1])%m

# cnt=0
# d = {}

# for x in prefix[1:]:
#   if x in d:
#     d[x] +=1
#   else:
#     d[x] = 1

# for x in d:
#   if x==0:
#     cnt += ((d[x])*(d[x]+1))//2
#   else:
#     cnt += ((d[x])*(d[x]-1))//2

# print(cnt)
# for i in range(1,n+1):
#   for j in range(i):
#     if prefix[i]-prefix[j] ==0:
#       cnt +=1


# 1629 - divide & conquer
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# a,b,c = map(int,input().split())
# # (a*a)mod c = ((a mod c) * (a mod c) mod c)

# def dc(a,b,c):
#   if b==1:
#     return a%c
#   elif b%2==0:
#     return (dc(a,b//2,c)**2)%c
#   else:
#     return ((a%c) * ((dc(a,(b-1)//2,c)**2) %c))%c

# print(dc(a,b,c))

# #2293 - dp
# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# coins = [int(input()) for _ in range(n)]

# dp = [0]*(k+1)
# dp[0] = 1

# for coin in coins:
#   for i in range(coin,k+1):
#     dp[i] += dp[i-coin]

# print(dp[k])

# 1806 - 투포인터, 슬라이딩 윈도우
# import sys
# input =sys.stdin.readline
# MAX = 100000

# n,s = map(int,input().split())
# arr = list(map(int,input().split()))

# cnt = 0
# total = 0
# j=0
# ans = MAX

# for i in range(n):
#   total += arr[i]
#   cnt+=1
#   while total >=s:
#     ans=min(ans,cnt)
#     total -= arr[j]
#     j+=1
#     cnt-=1

# if ans == MAX:
#   print('0')
# else:
#   print(ans)

# #2225 - dp
# import sys
# input =sys.stdin.readline

# n,k = map(int,input().split())

# dp = [[0]*(k+1) for _ in range(n+1)]

# for i in range(k+1):
#   dp[0][i]=1
# for j in range(n+1):
#   dp[j][1]=1

# for i in range(1,n+1):
#   for j in range(2,k+1):
#     dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000000

# print(dp[n][k]%1000000000)

# # #11053
# import sys
# import bisect
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# lis = []

# for x in arr:
#   pos = bisect.bisect_left(lis,x)

#   if pos == len(lis):
#     lis.append(x)
#   else:
#     lis[pos] = x

# print(len(lis))

# dp = [1]*(n+1)

# for i in range(1,n+1):
#   for j in range(1, i):
#     if arr[j-1] < arr[i-1]:
#       dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))

# 1647 - MST
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())

# arr = [list(map(int,input().split())) for _ in range(m)]
# arr.sort(key=lambda x:x[2])

# parent = [i for i in range(n+1)]

# def find(s):
#   if s != parent[s]:
#     parent[s] = find(parent[s])
#   return parent[s]

# cnt = 0
# total = 0

# for x in arr:
#   a,b,c = x[0], x[1], x[2]

#   a=find(a)
#   b=find(b)

#   if a==b:
#     continue

#   parent[b] = a
#   cnt +=1
#   total +=c

#   if cnt == n-1:
#     total -=c
#     print(total)
#     break

# #1976
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# check = list(map(int,input().split()))

# parent=[i for i in range(n+1)]

# def find(a):
#   if a != parent[a]:
#     parent[a] = find(parent[a])
#   return parent[a]

# def union(a,b):
#   a= find(a)
#   b = find(b)

#   if a==b:
#     return
#   parent[b] = a

# for i in range(n):
#   for j in range(n):
#     if i==j:
#       continue
#     if arr[i][j] ==1:
#       union(i+1,j+1)

# for i in range(m):
#   check[i] = find(check[i])

# s = set(check)

# if len(s) ==1:
#   print('YES')
# else:
#   print('NO')

#2696
# import sys
# import heapq
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#   m = int(input())

#   arr=[]
#   for _ in range(m//10+1):
#     tmp = list(map(int,input().split()))
#     arr+=tmp
  
#   right = []  #오름차순. 여기에 중앙값
#   left = []  #내림차순
#   out=[]

#   for i in range(m):
#     if i==0:
#       heapq.heappush(right,arr[i])
#       out.append(right[0])
#       continue

#     if arr[i] > right[0]:
#       heapq.heappush(right,arr[i])
#     else:
#       heapq.heappush(left,-arr[i])
    
#     l = len(left)
#     r = len(right)
#     if l > r:   # left가 right보다 길거나 같으면 l->r
#       heapq.heappush(right,-heapq.heappop(left)) 
#     elif l+1 <r:  #right가 left 1더한거보다 크다면. r->l
#       heapq.heappush(left,-heapq.heappop(right)) 

    
#     if i%2 ==0:
#       out.append(right[0])

#   print(len(out))
#   for i in range(len(out)):
#     if i !=0 and (i)%10==0:
#       print()
#     print(out[i],end=' ')

#1654
# import sys
# input = sys.stdin.readline

# k,n = map(int,input().split())

# arr = [int(input()) for _ in range(k)]
# arr.sort()

# left = 1
# right = arr[-1]
# ans = 0

# while left <= right:
#   mid = (left + right)//2
#   cnt = 0
#   for x in arr:
#     cnt += x // mid

#   if cnt >= n :
#     ans = mid
#     left = mid +1
#   else:
#     right = mid -1

# print(ans)

# #2805
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))

# left = 0
# right = max(arr)
# ans = 0

# while left <= right:
#   mid = (left + right)//2
#   total = 0

#   for x in arr:
#     if x>mid:
#       total+=x-mid
  
#   if total == m:
#     ans=mid
#     break
#   elif total > m:
#     ans=mid
#     left = mid+1
#   else:
#     right = mid-1

# print(ans)
