# 그래프 : 정점(Vertex)과 간선(Edge)로 이루어진 자료구조.
# DFS : Depth First Search. 깊이 우선 탐색. 한 경로를 끝까지 탐색한 후, 다음 경로
# BFS : Breadth First Search. 너비 우선 탐색. 현재 정점에서 가까운 노드부터 탐색


# 24479
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n,m,r = map(int, input().split())

# node = [[] for _ in range(n+1)]
# visited = [0] *(n+1)

# for _ in range(m):
#    a,b = map(int, input().split())
#    node[a].append(b)
#    node[b].append(a)

# for i in range(1,n+1):
#    node[i].sort()

# cnt = 0

# def dfs(r):
#    global cnt
#    cnt+=1
#    visited[r] = cnt
#
#    for x in node[r]:
#        if visited[x] == 0:
#            dfs(x)
#    return

# dfs(r)
# print('\n'.join(map(str, visited[1:])))

# 24480
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n, m, r = map(int, input().split())

# visited = [0]*(n+1)
# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#    a, b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

# for i in range(1,n+1):
#    graph[i].sort(reverse=True)

# cnt =0

# def dfs(r):
#    global cnt
#    cnt+=1
#    visited[r] = cnt
#
#    for x in graph[r]:
#        if visited[x] == 0:
#            dfs(x)
#    return
# dfs(r)

# print('\n'.join(map(str, visited[1:])))

# 24444
# from collections import deque
# import sys

# input = sys.stdin.readline

# n,m,r = map(int, input().split())

# graph = [[] for _ in range(n+1)]
# q = deque()
# visited = [0] *(n+1)

# for _ in range(m):
#    a,b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

# for i in range(1, n+1):
#    graph[i].sort()
#
# def bfs(r):
#    cnt = 1
#    visited[r] = cnt
#
#    q.append(r)
#
#    while q:
#        u = q.popleft()
#        for x in graph[u]:
#            if not visited[x]:
#                cnt+=1
#                visited[x] = cnt
#                q.append(x)

# bfs(r)
# print('\n'.join(map(str, visited[1:])))


# 24445
# import sys
# from collections import deque

# input = sys.stdin.readline
# q=deque()

# n,m,r = map(int, input().split())

# visited= [0] *(n+1)
# graph=[[] for _ in range(n+1)]

# for _ in range(m):
#    a,b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

# for i in range(1,n+1):
#    graph[i].sort(reverse=True)

# def dfs(r):
#    cnt=1
#    visited[r] = cnt
#
#    q.append(r)
#
#    while q:
#        u = q.popleft()
#        for x in graph[u]:
#            if visited[x] ==0:
#                cnt +=1
#                visited[x] = cnt
#                q.append(x)
#
# dfs(r)
# print('\n'.join(map(str, visited[1:])))

# 2606
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# visited = [False] * (n+1)
# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#    a,b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

# cnt=0

# def bfs(r):
#    global cnt
#    visited[r] = True
#    q=deque([r])
#
#    while q:
#        u = q.popleft()
#        for x in graph[u]:
#            if visited[x] == False:
#                visited[x] =True
#                cnt+=1
#                q.append(x)
# bfs(1)
# print(cnt)

# 1260
# import sys
# from collections import deque

# input = sys.stdin.readline
# n, m, v = map(int, input().split())

# graph= [[] for _ in range(n+1)]

# for _ in range(m):
#    a,b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

# for i in range(1, n+1):
#    graph[i].sort()


# visited = [0] * (n+1)
# ord = [v]
# cnt = 0

# def dfs(v):
#    global cnt
#    cnt += 1
#    visited[v] = cnt
#
#    for x in graph[v]:
#        if visited[x] == 0:
#            ord.append(x)
#            dfs(x)


# def bfs(v):
#    global cnt
#    cnt =1
#    visited[v] =cnt
#    q.append(v)
#
#
#    while q:
#        u = q.popleft()
#
#        for x in graph[u]:
#            if visited[x] ==0:
#                q.append(x)
#                cnt +=1
#                visited[x] =cnt
#                ord.append(x)
#
# dfs(v)
# print(' '.join(map(str, ord)))

# visited = [0] * (n+1)
# cnt=0
# q = deque()
# ord=[v]

# bfs(v)

# print(' '.join(map(str, ord)))


# 2667
#import sys

#input = sys.stdin.readline

#n = int(input())

#li = [input() for _ in range(n)]
#visited = [[False] *(n) for _ in range(n)]

#apt = 0
#ans = []
#cnt =0

#def dfs(row,col):
#    if visited[row][col] != False:
#        return
#    if li[row][col] == '0':
#        return
#        
#    global cnt
#    
#    if li[row][col] == '1':
#        visited[row][col] = apt
#        cnt+=1
#        if row >0:
#            dfs(row-1,col)
#        if col > 0:
#            dfs(row,col-1)
#        if col < n-1:
#            dfs(row,col+1)
#        if row < n-1:
#            dfs(row+1,col)
#        
#        
#for i in range(n):
#    for j in range(n):
#        if li[i][j] == '1' and visited[i][j] == False:
#            apt +=1
#            cnt = 0 
#            dfs(i,j)
#            ans.append(cnt)
#            
#print(apt)
#ans.sort()
#for i in range(apt):
#    print(ans[i])

#dfs로 풀었는데 다음에는 bfs로 ㄲㄲ

# 1012

# 2178

# 7562

# 7576

# 7569

# 16928

# 2206

# 1707




#---------review
#2606
#import sys
#input = sys.stdin.readline

#n = int(input())
#m = int(input())

#graph = [[] for _ in range(n+1)]
#visited = [False] * (n+1)
#visited[1] = True

#for _ in range(m):
#    a,b = map(int, input().split())
#    
#    graph[a].append(b)
#    graph[b].append(a)
#    
#def dfs(v):
#    for nxt in graph[v]:
#        if visited[nxt] == False:
#            visited[nxt] = True
#            dfs(nxt)

#dfs(1)

#print(visited.count(True) -1)