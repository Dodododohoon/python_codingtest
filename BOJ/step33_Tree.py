#그래프 만들 듯이 인접리스트형식으로 세팅해두고
#필요한 트리전용정보를 리스트(parent, subtree 등)를 만들어서 뽑아냄.

#11725
#import sys
#sys.setrecursionlimit(10**7)
#input = sys.stdin.readline

#n = int(input())
#graph = [[] for _ in range(n+1)]
#parent= [0]*(n+1)

#for _ in range(n-1):
#    a,b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

#def dfs (u,p):
#    parent[u] = p
#    for x in graph[u]:
#        if x != p:
#            dfs(x,u)

#dfs(1,0)

#print('\n'.join(map(str, parent[2:])))

#1167
#import sys
#sys.setrecursionlimit(10**7)

#n = int(input())
#graph = [[]for _ in range(n+1)]

#visited = [False] * (n+1)
#depth = [0] * (n+1)

#for _ in range(n):
#    li = list(map(int, input().split()))
#    if len(li)>2:
#        for i in range(1,len(li)-1,2):
#            a,b = li[i], li[i+1]
#            graph[li[0]].append((a,b))
#    
#def dfs(u):
#    visited[u] = True
#    for nxt, d in graph[u]:    
#        if visited[nxt] == False:
#            depth[nxt] = depth[u] + d
#            dfs(nxt)

#dfs(1)

#k = depth.index(max(depth))
#depth = [0] *(n+1)
#visited = [False]*(n+1)

#dfs(k)

#print(max(depth))

#지름을 깊이로 잘못 이해해서 dfs 하나만 했는데 알고보니 가장 먼 두 노드 값이었음.
#그리고 depth로 한번에 처리하려고 한거 조금 아쉽고.
#나머지는 좀 깔끔한 듯. 

#1967
#import sys
#sys.setrecursionlimit(10**6)

#input = sys.stdin.readline

#n = int(input())

#graph = [[] for _ in range(n+1)]
#visited = [False] * (n+1)
#dist = [0] * (n+1)

#for _ in range(n-1):
#    a, b, c = map(int, input().split())
#    graph[a].append((b,c))
#    graph[b].append((a,c))

#def dfs(s):
#    visited[s] = True
#    
#    for nxt, w in graph[s]:
#        if visited[nxt] == False:
#            dist[nxt] = dist[s] + w
#            dfs(nxt)
#    
#dfs(1)
#k = dist.index(max(dist))

#visited = [False] * (n+1)
#dist = [0] * (n+1)

#dfs(k)

#print(max(dist))
    
#1991


#2263


#5639


#4803

