# 1463    -  못 품. heap. 시간 초과, dp 틀림.
# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = [0] * (n+1)

# for i in range(2,n+1):
#    dp[i] = dp[i-1] +1
#
#    if i %3 ==0:
#        dp[i] = min(dp[i], dp[i//3] +1)
#    if i%2 ==0:
#        dp[i] = min(dp[i], dp[i//2]+1)
#
# print(dp[n])

#1463
#import sys
#import heapq
#INF = int(1e6)
#input = sys.stdin.readline

#n = int(input())

#dp = [INF] * (n+1)
#dp[n] = 0
#for i in range(n,0,-1):
#    cnt = dp[i]
#    if i %3 ==0:
#        dp[i//3] = min(cnt +1, dp[i//3])
#    if i %2 ==0:
#        dp[i//2] = min(cnt +1, dp[i//2])
#    dp[i-1] = min(cnt +1, dp[i-1])
#        
#print(dp[1])

#hq = [(0,n)]                         - 얘가 안된 이유 : heap 접근은 좋았는데, 나는 힙 해주면 중복은 알아서 밀릴꺼고 1나오면 끝날꺼니깐 중복처리 안해줘도 상관없겠다 싶었다. 근데 push하는 것 또한 시간 잡아먹고 한 루프당 최대 3번 push가 있으니 중복 처리는 필수네.

#while hq:
#    cnt, num = heapq.heappop(hq)
#    
#    if num == 1:
#        break
#    
#    if num %3 ==0:
#        heapq.heappush(hq,(cnt+1, num//3))
#    if num %2 ==0:
#        heapq.heappush(hq, (cnt+1, num//2))
#    heapq.heappush(hq, (cnt+1, num-1))

#print(cnt)


# # 2579        - 깔끔하게 clear, 너무 강렬해서 그냥 기억이남.
# import sys

# input = sys.stdin.readline

# n = int(input())
# li = [int(input()) for _ in range(n)]

# if n==1:
#     print(li[0])
#     exit()
# if n==2:
#     print(li[0]+li[1])
#     exit()


# dp = [0] * (n + 1)

# dp[1] = li[0]
# dp[2] = li[0] + li[1]


# for i in range(3, n + 1):
#     dp[i] = max(dp[i - 3] + li[i - 2], dp[i - 2]) + li[i - 1]

# print(dp[n])

# 9095        - 10~20분 컷. 나름 dp 잘짰다 싶긴했고 나름 잘 풀었는데 더 깔끔한 방식이 있네
# import sys

# input = sys.stdin.readline

# t = int(input())

# dp_1 = [0] * (11)
# dp_2 = [0] * (11)
# dp_3 = [0] * (11)

# dp_1[1] = 1
# dp_2[1] = 0
# dp_3[1] = 0

# dp_1[2] = 1 
# dp_2[2] = 1
# dp_3[2] = 0

# for i in range(3, 11):
#     dp_1[i] = dp_1[i - 1] + dp_2[i - 1] + dp_3[i - 1]
#     dp_2[i] = dp_1[i - 1]
#     dp_3[i] = dp_2[i - 1]

# for _ in range(t):
#     n = int(input())
#     print(dp_1[n] + dp_2[n] + dp_3[n])

#9095
#import sys
#input = sys.stdin.readline

#t = int(input())
#dp = [0] * 11
#dp[1] = 1
#dp[2] = 2
#dp[3] = 4

#for i in range(4,11):
#    dp[i] = dp[i-1] +dp[i-2] + dp[i-3]

#for _ in range(t):
#    n = int(input())
#    
#    print(dp[n])
    
#11726
#import sys
#input =sys.stdin.readline

#n = int(input())

#if n==1:
#    print('1')
#else:
#    
#    dp = [0] * (n+1)
#    dp[1] = 1
#    dp[2] = 2
#    
#    for i in range(3,n+1):
#        dp[i] = (dp[i-1] + dp[i-2]) % 10007
#    
#    print(dp[n])
    

# 11726 - 10분 컷 매우 쉽노
# import sys

# input = sys.stdin.readline

# n = int(input())

# dp = [0] * (n + 1)

# dp[1] = 1

# if n>=2:
#   dp[2] = 2
#   for i in range(3, n + 1):
#       dp[i] = dp[i - 1] + dp[i - 2]

# print(dp[n] % 10007)

#1149       - 배열 이상하게 세팅해서 좀 걸렸음. 점화식 뽑는데는 한 10~20분 걸린듯?
#import sys
#input = sys.stdin.readline

#n = int(input())

#li = [list(map(int, input().split())) for _ in range(n)]

#dp = [[0] * (3) for _ in range(n+1)]

#dp[1][0] = li[0][0]
#dp[1][1] = li[0][1]
#dp[1][2] = li[0][2]

#for i in range(2,n+1):
#    dp[i][0] = li[i-1][0] + min(dp[i-1][1], dp[i-1][2])
#    dp[i][1] = li[i-1][1] + min(dp[i-1][0], dp[i-1][2])
#    dp[i][2] = li[i-1][2] + min(dp[i-1][0], dp[i-1][1])

#print(min(dp[n]))

#1260
#import sys
#from collections import deque
#input = sys.stdin.readline

#n,m,v = map(int,input().split())

#graph = [[] for _ in range(n+1)]
#visited = [False] * (n+1)

#for _ in range(m):
#    a,b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

#for i in range(1,n+1):
#    graph[i].sort()

#out_dfs=[v]
#visited[v] = True

#def dfs(k):
#    for nxt in graph[k]:
#        if visited[nxt] == False:
#            visited[nxt] = True
#            out_dfs.append(nxt)
#            dfs(nxt)
#            
#dfs(v)

#visited = [False] * (n+1)
#visited[v] = True
#q=deque()
#q.append(v)
#out_bfs=[v]

#while q:
#    w = q.popleft()
#    
#    for nxt in graph[w]:
#        if visited[nxt] == False:
#            visited[nxt] = True
#            q.append(nxt)
#            out_bfs.append(nxt)

#print(' '.join(map(str, out_dfs)))
#print(' '.join(map(str, out_bfs)))

#1260                    - 10~15분 컷. DFS, BFS 기본 구조는 이제 깔끔하게 이해 한 듯.
#import sys
#from collections import deque
#sys.setrecursionlimit(10**6)

#input = sys.stdin.readline

#n, m, v = map(int,input().split())

#graph = [[] for _ in range(n+1)]
#visited = [False] *(n+1)
#visited[v] = True

#for _ in range(m):
#    a,b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

#for i in range(n+1):
#    graph[i].sort()

#out_dfs = [v]
#out_bfs = [v]

#def dfs(r):
#    for nxt in graph[r]:
#        if not visited[nxt]:
#            visited[nxt] = True
#            out_dfs.append(nxt)
#            dfs(nxt)

#def bfs(r):
#    q = deque()
#    q.append(r)
#    
#    while q:
#        x = q.popleft()
#        
#        for nxt in graph[x]:
#            if not visited[nxt]:
#                visited[nxt] = True
#                out_bfs.append(nxt)
#                q.append(nxt)

#dfs(v)

#visited = [False] *(n+1)
#visited[v] = True

#bfs(v)

#print(' '.join(map(str, out_dfs)))
#print(' '.join(map(str, out_bfs)))

#2667
#import sys
#from collections import deque

#input = sys.stdin.readline

#n = int(input())
#arr=[[] for _ in range(n)]

#for i in range(n):
#    temp = input().strip()
#    for x in temp:
#        arr[i].append(int(x))

#q=deque()
#block = 2
#cnt = 0
#out=[]

#for i in range(n):
#    for j in range(n):
#        if arr[i][j] ==1:
#            q.append((i,j))
#            while q:
#                col, row = q.popleft()
#                
#                if arr[col][row] ==1:
#                    arr[col][row] = block
#                    cnt+=1
#                    
#                    if row < n-1:
#                        q.append((col, row+1))
#                    if col < n-1:
#                        q.append((col+1, row))
#                    if row >0:
#                        q.append((col, row-1))
#                    if col >0:
#                        q.append((col-1, row))
#            block +=1
#            out.append(cnt)
#            cnt=0
#                    
#print(block-2)
#out.sort()
#print('\n'.join(map(str, out)))

#1697
#import sys
#import heapq
#INF = int(1e9)
#input= sys.stdin.readline

#n,k = map(int,input().split())

#if n==k:
#    print('0')
#    exit()

#hq = [(0,n)]
#time = [INF] * 200001

#while hq:
#    sec, loc = heapq.heappop(hq)
#    
#    if loc == k:
#        print(sec)
#        break
#    if loc < k and time[loc+1] > sec +1:
#        time[loc+1] = sec +1
#        heapq.heappush(hq,(sec+1, loc+1))
#    if loc >0 and time[loc-1] > sec+1:
#        time[loc-1] = sec+1
#        heapq.heappush(hq,(sec+1, loc-1))
#    if loc < k and time[loc*2] > sec+1:
#        time[loc*2] = sec +1
#        heapq.heappush(hq,(sec+1, 2 * loc))

#import sys
#from collections import deque

#input= sys.stdin.readline

#n,k = map(int,input().split())

#MAX = 100000
#q=deque([n])
#visited = [-1] * (MAX+1)
#visited[n] = 0

#while q:
#    loc = q.popleft()
#    if loc == k:
#        print(visited[k])
#        break
#    
#    for nxt in (loc -1, loc+1, loc *2):
#        if 0<= nxt <= MAX and visited[nxt] == -1 :
#            visited[nxt] = visited[loc] + 1
#            q.append(nxt)


#1697
#import sys
#import heapq
#input = sys.stdin.readline
#INF = int(1e9)

#n, k = map(int, input().split())

#hq = [(0,n)]

#time = [INF] * (100001)
#time[n] = 0

#while hq:
#    t, loc = heapq.heappop(hq)
#    
#    if loc == k:
#        print(t)
#        break
#    
#    nx = 2*loc
#    if 0 <= nx <= 100000 and time[nx] > t+1:
#        time[nx] = t+1
#        heapq.heappush(hq,(t+1,nx))
#    
#    nx = loc - 1
#    if 0 <= nx <= 100000 and time[nx] > t+1:
#        time[nx] = t+1
#        heapq.heappush(hq,(t+1,nx))
#            
#    nx = loc + 1
#    if 0 <= nx <= 100000 and time[nx] > t+1:
#        time[nx] = t+1
#        heapq.heappush(hq,(t+1,nx))

#1697
#import sys
#from collections import deque
#INF = int(1e9)

#input = sys.stdin.readline

#n, k = map(int, input().split())

#visited = [INF] * 100001
#visited[n] = 0

#q = deque([n])

#while q:
#    loc = q.popleft()
#    t= visited[loc]
#    
#    if loc == k:
#        print(t)
#        break
#    
#    nxt = loc -1
#    if 0<= nxt <= 100000 and visited[nxt] == INF:
#        visited[nxt] = t+1
#        q.append(nxt)
#    
#    nxt = loc +1
#    if 0<= nxt <= 100000 and visited[nxt] == INF:
#        visited[nxt] = t+1
#        q.append(nxt)
#    
#    nxt = 2 * loc
#    if 0<= nxt <= 100000 and visited[nxt] == INF:
#        visited[nxt] = t+1
#        q.append(nxt)

#1904
#import sys
#input = sys.stdin.readline

#n = int(input())

#dp = [0] * (n+1)
#dp[1] = 1
#if n>1:
#    dp[2] = 2

#for i in range(3,n+1):
#    dp[i] = (dp[i-1] + dp[i-2]) % 15746

#print(dp[n])

#1904
#import sys
#input = sys.stdin.readline

#n = int(input())

#dp = [0] * (n+1)
#dp[1] = 1

#if n >= 2:
#    dp[2] = 2
#    
#    for i in range(3,n+1):
#        dp[i] = (dp[i-1]+ dp[i-2])%15746
#print(dp[n])

#2293
#import sys
#input = sys.stdin.readline

#n,k = map(int, input().split())
#coins = [int(input()) for _ in range(n)]
#dp = [0] * (k+1)
#dp[0] = 1
#coins.sort()

#for coin in coins:
#    for i in range(coin, k+1):
#        dp[i] += dp[i-coin]

#print(dp[k])

#2293
#import sys
#input = sys.stdin.readline

#n,k = map(int,input().split())
#coins = [int(input()) for _ in range(n)]

#coins.sort()

#dp = [0] * (k+1)
#dp[0] = 1

#for coin in coins:
#    for i in range(coin, k+1):
#        dp[i] += dp[i-coin]

#print(dp[k])


#2293            - 아이디어 보고도 이해하기 힘들었음. 조합,순열 차이. 어렵네
#import sys
#input = sys.stdin.readline

#n,k = map(int, input().split())
#coins = [int(input()) for _ in range(n)]

#coins.sort()
#dp = [0]*(k+1)
#dp[0]=1

#for coin in coins:
#    for i in range(coin, k+1):
#        dp[i] += dp[i - coin]

#print(dp[k])

#11057
#import sys

#n = int(input())

#dp = [[0] * 10 for _ in range(n+1)]

#for i in range(10):
#    dp[1][i] = 1

#for i in range(2,n+1):
#    for j in range(10):
#        dp[i][j] = sum(dp[i-1][0:j+1])%10007

#print(sum(dp[n])%10007)

#import sys

#n = int(input())

#dp = [1] * 10

#for _ in range(n-1):
#    for i in range(9,-1,-1):
#        dp[i] = sum(dp[0:i+1])%10007

#print(sum(dp)%10007)

#11057                혼자 풀긴함. 근데 조금씩 잘 못 써서 틀림. 그래도 bt하다가 수식으로 하다가 dp로 풀고 그럼. 1차원 DP로 가능.
#import sys
#input = sys.stdin.readline

#n = int(input())
#dp = [[0] *10 for _ in range(n+1)]

#for i in range(10):
#    dp[1][i] = 1

#if n >= 2:
#    for i in range(2,n+1):
#        for j in range(0, 10):
#            if j ==0:
#                dp[i][j] = 1
#            else:
#                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%10007
#    
#print(sum(dp[n])% 10007)

#def bt(r, len):        넣을때 부터 찝찝했음. 10^n
#    global cnt
#    if len == n :
#        cnt += 1
#        if cnt > 10007:
#            cnt= cnt % 10007
#        return
#    
#    for i in range(r, 10):
#        bt(i, len +1)
#bt(0,0)

#11052
#import sys

#n = int(input())

#arr = list(map(int, input().split()))

#dp = [0] * (n+1)
#arr.insert(0,0)

#dp[1] = arr[1]

#for i in range(1, n+1):
#    for j in range(1,i+1):
#        dp[i] = max(dp[i], dp[i-j] + arr[j])

#print(dp[n])

#2225
#import sys

#input = sys.stdin.readline

#n,k = map(int,input().split())

#dp = [[1] * (n+1) for _ in range(k+1)]

#for i in range(2,k+1):
#    for j in range(0,n+1):
#        dp[i][j] = sum(dp[i-1][:j+1]) % 1000000000   #점화식 더 깔끔하게 가능

#print(dp[k][n]%1000000000)



#2225                    혼자 못 풀었음. 아무리 생각해도 전 문제는 나름 직접 끌고 왔는데 이건 못 푼게 좀 빡침.
#import sys

#input= sys.stdin.readline

#n,k = map(int,input().split())

#dp = [[0] * (n+1) for _ in range(k+1)]

#for i in range(k+1):
#    dp[i][0] = 1
#for i in range(n+1):
#    dp[1][i] = 1

#for i in range(1,k+1):
#    for j in range(1,n+1):
#        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

#print(dp[k][n])

#1309
#import sys
#input = sys.stdin.readline


#n = int(input())


#dp = [0] * (n+1)
#dp[0] = 1
#dp[1] = 3

#for i in range(2,n+1):
#    dp[i] = (2* dp[i-1] + dp[i-2])%9901
#print(dp[n]%9901)

#1309                    깔끔하게 혼자 클리어.
#import sys
#input = sys.stdin.readline

#n = int(input())

#dp = [0] * (n+1)
#dp[0] = 1
#dp[1] = 3

#for i in range(2,n+1):
#    dp[i] = (dp[i-1] + (dp[i-1] - dp[i-2]) + dp[i-2] * 2) % 9901

#print(dp[n])

#1924                            그냥 하드 코딩으로 품. 딱히 뭐 더 규칙 찾는게 더 비효율같아서. 근데 month리스트 따로 두는 게 더 괜찮은 듯.
#import sys
#input = sys.stdin.readline

#x,y = map(int, input().split())

#day = ['SUN']
#week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
#day = day + (week*52)
#day.append('MON')

#if x == 1:
#    print(day[y])
#if x == 2:
#    print(day[31+y])
#if x == 3:
#    print(day[31+28+y])
#if x == 4:
#    print(day[31+28+31+y])
#if x == 5:
#    print(day[31+28+31+30+y])
#if x == 6:
#    print(day[31+28+31+30+31+y])
#if x == 7:
#    print(day[31+28+31+30+31+30+y])
#if x == 8:
#    print(day[31+28+31+30+31+30+31+y])
#if x == 9:
#    print(day[31+28+31+30+31+30+31+31+y])
#if x == 10:
#    print(day[31+28+31+30+31+30+31+31+30+y])
#if x == 11:
#    print(day[31+28+31+30+31+30+31+31+30+31+y])
#if x == 12:
#    print(day[31+28+31+30+31+30+31+31+30+31+30+y])

#15649                                외워진건지 모르겠는데 깔끔하게 풀어감. 딱딱딱 그냥
#import sys
#sys.setrecursionlimit(10**6)

#input = sys.stdin.readline

#n,m = map(int, input().split())

#visited = [False] * (n+1)
#out = []

#def bt(k):
#    if k == m:
#        print(' '.join(map(str, out)))
#        return
#    for i in range(1,n+1):
#        if not visited[i]:
#            visited[i] = True
#            out.append(i)
#            bt(k+1)
#            visited[i] = False
#            out.remove(i)           #out.pop()이 훨씬 효율
#    
#bt(0)

#9663
#import sys

#input = sys.stdin.readline

#n = int(input())

#down = [False] * (n)
#right = [False] * (2*n -1)
#left = [False] * (2*n -1)
#cnt = 0

#def bt(row):
#    global cnt
#    
#    if row == n:
#        cnt += 1
#        return
#    
#    for col in range(n):
#        r = row-col + (n-1)
#        l = row+col
#        if down[col] == False and right[r] == False and left[l] == False:
#            down[col] = right[r] = left[l] = True
#            bt(row+1)
#            down[col] = right[r] = left[l] = False

#bt(0)
#print(cnt)

#9663                직접 clear 전체 범위 세팅하는 거 다시 생각해보셈. 2n+1아님
#import sys
#input = sys.stdin.readline

#n = int(input())

#row = [True] * (n)
#up = [True] * (2*n +1)
#down = [True] * (2*n + 1)

#cnt =0

#def bt(col):
#    global n, cnt
#    
#    if col == n:
#        cnt +=1
#        return
#    
#    for i in range(n):
#        if row[i] and up[i+col] and down[n+i-col]:
#            row[i] = False
#            up[i+col] = False
#            down[n+i-col] = False
#            
#            bt(col+1)
#            
#            row[i] = up[i+col] = down[n+i-col] = True 
#            
#bt(0)

#print(cnt) 

#15650
#import sys
#input = sys.stdin.readline

#n,m = map(int, input().split())
#out = []

#def bt(k, cnt):
#    if cnt == m:
#        print(' '.join(map(str, out)))
#        return
#    
#    for i in range(k+1,n+1):
#        out.append(i)
#        bt(i,cnt+1)
#        out.pop()
#        
#bt(0,0)

#15651
#import sys
#input = sys.stdin.readline

#n,m = map(int, input().split())
#out = []

#def bt(k):
#    if k == m:
#        print(' '.join(map(str, out)))
#        return
#    
#    for i in range(1,n+1):
#        out.append(i)
#        bt(k+1)
#        out.pop()

#bt(0)


#15652
#import sys
#input = sys.stdin.readline

#n,m = map(int, input().split())

#out = []

#def bt(k):
#    if len(out) == m:
#        print(' '.join(map(str, out)))
#        return
#        
#    for i in range(k, n+1):
#        out.append(i)
#        bt(i)
#        out.pop()

#bt(1)

#8958
#import sys
#input = sys.stdin.readline

#n = int(input())

#for _ in range(n):
#    arr = input()
#    dp = [0] * (len(arr))
#    
#    for i in range(len(arr)):
#        if arr[i] == 'O':
#            if i == 0 :
#                dp[i] = 1
#            else:
#                dp[i] = dp[i-1] + 1 
#    
#    print(sum(dp))



#8958
#import sys
#input =sys.stdin.readline

#n = int(input())

#for _ in range(n):
#    s = input()
#    score = 0
#    con = 1
#    
#    if s[0] == 'O':
#        score += 1
#    
#    for i in range(1, len(s)):
#        if s[i] == 'O':
#            if s[i-1] == 'O':
#                con +=1
#            else:
#                con = 1
#            score += con
#    print(score)


#1012
#import sys
#sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

#t = int(input())

#for _ in range(t):
#    m,n,k = map(int,input().split())
#    cnt  = 0    
#    graph=[[0]*m for _ in range(n)]
#    
#    for _ in range(k):
#        x,y = map(int,input().split())
#        graph[y][x] = 1
#    
#    def dfs(row,col):
#        if row > 0:
#            if graph[row-1][col] ==1:
#                graph[row-1][col] = 2
#                bfs(row-1,col)
#        if col > 0:
#            if graph[row][col-1] ==1:
#                graph[row][col-1] = 2
#                bfs(row,col-1)
#        if col < (m-1):
#            if graph[row][col+1] ==1:
#                graph[row][col+1] = 2
#                bfs(row,col+1)            
#        if row < (n-1):
#            if graph[row+1][col] ==1:
#                graph[row+1][col] = 2
#                bfs(row+1,col)
#    
#    for i in range(n):
#        for j in range(m):
#            if graph[i][j] ==1:
#                 cnt += 1
#                 bfs(i,j)
#    print(cnt)

#11052                직접 clear, 문제 직접 푸는 방법을 좀 더 깔끔하게 해보자.
#import sys
#input =sys.stdin.readline

#n = int(input())
#li = list(map(int, input().split()))
# # p = [0] + list(map(int, input().split()))  # 1-index, 보기 좋네

#dp = [0] * (n+1)

#dp[1] = li[0]
#arr= []

#for i in range(2,n+1):
#    for j in range(i):
#        arr.append(dp[i-j-1] + li[j])
#        #dp[i] = max(dp[i], dp[i - k] + p[k])        #바로 바로 max 갱신
#    dp[i] = max(arr)
#    arr.clear()

#print(dp[n])

