# 11286
# import sys
# import heapq

# input = sys.stdin.readline

# n = int(input())
# hq = []

# for _ in range(n):
#     x = int(input())

#     if x:
#         heapq.heappush(hq, (abs(x), x))
#     else:
#         if hq:
#             a, b = heapq.heappop(hq)
#             print(b)
#         else:
#             print("0")

# 1918
# import sys

# input = sys.stdin.readline

# arr = input().strip()
# d = {"+": 1, "-": 1, "*": 2, "/": 2}

# stack = []
# out = []

# for x in arr:
#     if "A" <= x <= "Z":
#         out.append(x)
#     elif x == "(":
#         stack.append(x)
#     elif x == ")":
#         while stack and stack[-1] != "(":
#             out.append(stack.pop())
#         stack.pop()
#     else:
#         while stack and stack[-1] != "(" and d[stack[-1]] >= d[x]:
#             out.append(stack.pop())
#         stack.append(x)

# while stack:
#     out.append(stack.pop())

# print("".join(out))

# 14503
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# dc = [0, 1, 0, -1]
# dr = [-1, 0, 1, 0]

# cnt = 0

# while True:
#     if graph[r][c] == 0:  # 1
#         graph[r][c] = 2
#         cnt += 1

#     for i in range(4):
#         d = (d + 3) % 4
#                            # 3
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
#             r = nr
#             c = nc
#             break

#         if i == 3:                  # 2
#             nr = r - dr[d]
#             nc = c - dc[d]
#             if graph[nr][nc] == 1:
#                 print(cnt)
#                 exit()
#             else:
#                 r = nr
#                 c = nc

# 9012
# import sys
# input = sys.stdin.readline

# n = int(input())


# for _ in range(n):
#     arr = input().strip()
#     stack = []
#     check = 0

#     for x in arr:
#         if x =='(':
#             stack.append(x)
#         else:
#             if not stack:
#                 print('NO')
#                 check=1
#                 break
#             stack.pop()

#     if not check:
#         if stack:
#             print('NO')
#         else:
#             print('YES')

# #1654
# import sys
# input = sys.stdin.readline

# n, k = map(int,input().split())
# arr = [int(input().strip()) for _ in range(n)]
# arr.sort()

# left = 1
# right = arr[-1]

# while left <= right:
#   half = (left + right)//2
#   cnt = 0

#   for x in arr:
#     cnt += x//half

#   if cnt <k:
#     right = half - 1
#   else:         # 개수가 k보다 같거나 크면 최대한 자르는 길이를 키워야함.
#     left = half + 1

# print(right)

# 10799
# import sys
# input = sys.stdin.readline

# s = input().strip()

# stack = []
# ans = 0
# prev = ""

# for ch in s:
#   if ch == '(':
#     stack.append('(')
#     prev = ch
#   else:
#     stack.pop()
#     if prev == '(':
#       ans += len(stack)
#     else:
#       ans += 1
#     prev = ch

# print(ans)

# 1931
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr= []

# for _ in range(n):
#   start, end = map(int,input().split())
#   arr.append((end,start))

# arr.sort()

# cnt =1
# end = arr[0][0]
# start = arr[0][1]

# for a,b in arr[1:]:
#   if b >= end:
#     end = a
#     start = b
#     cnt +=1

# print(cnt)

# 4949
# import sys
# input = sys.stdin.readline

# while True:
#   arr = input()
#   if arr[0] =='.':
#     break

#   stack=[]
#   con = True


#   for x in arr:
#     if x =='(':
#       stack.append(x)
#     elif x=='[':
#       stack.append(x)
#     elif x ==')':
#       if not stack or stack[-1] != '(':
#         con = False
#         print('no')
#         break
#       stack.pop()
#     elif x == ']':
#       if not stack or stack[-1] != '[':
#         con = False
#         print('no')
#         break
#       stack.pop()

#   if con and not stack:
#     print('yes')
#   if con and stack:
#     print('no')

# 1715
# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# arr = [int(input()) for _ in range(n)]

# if n==1:
#   print('0')
#   exit()

# heapq.heapify(arr)
# total = []

# while arr:
#   a = heapq.heappop(arr)
#   b = heapq.heappop(arr)
#   deck = a+b

#   total.append(deck)
#   if arr:
#     heapq.heappush(arr,deck)

# print(sum(total))

# 1920
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = set(map(int,input().split()))
# m = int(input())
# check = list(map(int,input().split()))

# for x in check:
#   if x in arr:
#     print('1')
#   else:
#     print('0')

# 10799
# import sys
# input = sys.stdin.readline

# s = input().strip()

# stack =[]
# cnt =0
# prev = ''

# for x in s:
#   if x=='(':
#     stack.append(x)
#     prev = x
#   else:
#     if prev == '(':
#       stack.pop()
#       cnt += len(stack)
#     else:
#       stack.pop()
#       cnt += 1
#     prev = x

# print(cnt)

# 1715
# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# if n==1:
#   print('0')
#   exit()

# heapq.heapify(arr)
# total = 0

# while arr:
#   a = heapq.heappop(arr)
#   b = heapq.heappop(arr)
#   s = a+b
#   total += s
#   if not arr:
#     break
#   heapq.heappush(arr, s)

# print(total)

# 1475
# import sys
# input = sys.stdin.readline

# li = list(map(int, input().strip()))

# d=dict()
# for i in range(9):
#   d[i]=0

# for x in li:
#   if x==9:
#     d[6] +=1
#     continue
#   d[x] += 1

# num =0

# for x in d:
#   if x ==6:
#     if d[x] %2 ==0:
#       num = max(num, d[x]//2)
#     else:
#       num = max(num, d[x]//2+1)
#     continue
#   num = max(num, d[x])

# print(num)

# #4949
# import sys
# input = sys.stdin.readline


# while True:
#   stack = []
#   s = input()
#   if s[0] == '.':
#     break
#   wrong = False

#   for ch in s:
#     if ch == '(' or ch=='[':
#       stack.append(ch)
#     elif ch == ')':
#       if stack and stack[-1] =='(':
#         stack.pop()
#       else:
#         wrong = True
#         break
#     elif ch ==']':
#       if stack and stack[-1] =='[':
#         stack.pop()
#       else:
#         wrong = True
#         break

#   if not wrong and not stack:
#     print('yes')
#   else:
#     print('no')

# 1697
# import sys
# from collections import deque

# input = sys.stdin.readline

# n, k =map(int,input().split())

# MAX = 100001
# dp = [-1] * (MAX)
# dp[n] =0

# q = deque([(0,n)])
# while q:
#   time, loc = q.popleft()

#   if loc == k:
#     break

#   nxt = loc + 1
#   if 0<= nxt < MAX and dp[nxt] == -1:
#     dp[nxt] = time + 1
#     q.append((time+1, nxt))

#   nxt = loc - 1
#   if 0<= nxt < MAX and dp[nxt] == -1:
#     dp[nxt] = time + 1
#     q.append((time+1, nxt))

#   nxt = 2*loc
#   if 0<= nxt < MAX and dp[nxt] == -1:
#     dp[nxt] = time + 1
#     q.append((time+1, nxt))

# print(dp[k])

# 2110
# import sys
# input = sys.stdin.readline

# n,c = map(int,input().split())
# house = [int(input()) for _ in range(n)]
# house.sort()

# left = 1
# right = house[-1] - house[0]
# ans = 0

# while left<=right:
#   mid = (left+ right)//2

#   cnt = 1
#   last = house[0]

#   for i in range(1,n):
#     if house[i] - last >= mid:
#       last = house[i]
#       cnt +=1

#   if cnt >= c:
#     ans = mid
#     left = mid +1
#   else:
#     right = mid - 1

# print(ans)

# #1978
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# def is_prime(k):
#   if k==1:
#     return False
#   if k==2 or k==3:
#     return True

#   for i in range(2,int(k**(0.5))+1):
#     if k%i ==0:
#       return False

#   return True

# cnt = 0
# for x in arr:
#   if is_prime(x):
#     cnt+=1

# print(cnt)


# 11286
# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# hq = []

# for _ in range(n):
#   x = int(input())

#   if x==0:
#     if hq:
#       print(heapq.heappop(hq)[1])
#     else:
#       print('0')
#   else:
#     heapq.heappush(hq, (abs(x),x))
