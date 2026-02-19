#2240 자두나무
#import sys
#input =sys.stdin.readline

#t,w = map(int,input().split())

#arr = [int(input()) for _ in range(t)]

#dp=[[0] * (w+1) for _ in range(t+1)]

#for i in range(1,t+1):
#    for j in range(0,w+1):
#        if arr[i-1] == 1:
#            if j ==0:
#                dp[i][j] = dp[i-1][j] +1
#            elif j % 2 ==0:
#                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
#            else:
#                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
#        else:
#            if j % 2 ==1:
#                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + 1
#            elif j ==0:
#                dp[i][j] = dp[i-1][j]
#            else:
#                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
#            

#print(max(dp[t]))

#14502 - 연구소, 골드4
#import sys
#from collections import deque
#input = sys.stdin.readline


#n , m = map(int, input().split())
#graph = [list(map(int, input().split())) for _ in range(n)]

#def bfs(a1,a2,b1,b2,c1,c2):
#    temp = [row[:] for row in graph]
#    temp[a1][a2] = 1
#    temp[b1][b2] = 1
#    temp[c1][c2] = 1
#    
#    dx = [1,-1]
#    dy = [1,-1]
#    q=deque()
#    
#    for i in range(n):
#        for j in range(m):
#            if temp[i][j] ==2:
#                q.append((i,j))
#                
#    while q:
#        y, x =q.popleft()
#        
#        for d in dx:
#            nx = x+d
#            if nx >= 0 and nx <m:
#                if temp[y][nx] == 0:
#                    temp[y][nx] = 2
#                    q.append((y,nx))
#        
#        for d in dy:
#            ny = y+d
#            if ny>=0 and ny < n:
#                if temp[ny][x] ==0:
#                    temp[ny][x] = 2
#                    q.append((ny,x))
#                        
#    cnt = 0
#    
#    for i in range(n):
#        for j in range(m):
#            if temp[i][j] ==0:
#                cnt += 1
#    
#    return cnt

#ans = 0

#for a in range(n*m-2):
#    row_a = a//m
#    col_a = a%m
#    if graph[row_a][col_a] != 0:
#        continue
#    for b in range(a+1,n*m-1):
#        row_b = b//m
#        col_b = b%m
#        if graph[row_b][col_b] != 0:
#            continue
#        for c in range(b+1, n*m):
#            row_c = c//m
#            col_c = c%m
#            if graph[row_c][col_c] != 0:
#                continue
#            ans = max(ans, bfs(row_a,col_a,row_b,col_b,row_c,col_c))
#                    
#print(ans)
#--------answer
#import sys
#from collections import deque
#input = sys.stdin.readline

#n,m = map(int,input().split())
#graph = [list(map(int,input().split())) for _ in range(n)]

#virus = []
#empty = 0
#for i in range(n):
#    for j in range(m):
#        if graph[i][j] == 2:
#            virus.append((i,j))
#        if graph[i][j] == 0:
#            empty += 1

#ans = 0
#dx = [1,-1,0,0]
#dy = [0,0,1,-1]

#def dfs():
#    temp = [row[:] for row in graph]
#    q = deque()
#    infected = 0
#    
#    for y, x in virus:
#        q.append((y,x))
#    
#    while q:
#        y, x = q.popleft()
#        
#        for i in range(4):
#            nx = x + dx[i]
#            ny = y + dy[i]
#            
#            if 0<= nx <m and 0<= ny <n and temp[ny][nx] ==0:
#                temp[ny][nx] = 2
#                infected +=1
#                q.append((ny,nx))
#    
#    return infected
#    
#def wall(start, block):
#    global ans
#    
#    if block ==3:
#        infected = dfs()
#        
#        safe = empty - 3 - infected
#        if safe > ans:
#            ans = safe
#        return
#    
#    for idx in range(start, n*m):
#        row = idx//m
#        col = idx%m
#        
#        if graph[row][col] != 0:
#            continue
#        
#        graph[row][col] =1
#        wall(start+1,block+1)
#        graph[row][col] = 0
#        

#wall(0,0)
#print(ans)


