# 그래프 만들 듯이 인접리스트형식으로 세팅해두고
# 필요한 트리전용정보를 리스트(parent, subtree 등)를 만들어서 뽑아냄.

# 11725
# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# n = int(input())
# graph = [[] for _ in range(n+1)]
# parent= [0]*(n+1)

# for _ in range(n-1):
#    a,b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

# def dfs (u,p):
#    parent[u] = p
#    for x in graph[u]:
#        if x != p:
#            dfs(x,u)

# dfs(1,0)

# print('\n'.join(map(str, parent[2:])))

# 1167
# import sys
# sys.setrecursionlimit(10**7)

# n = int(input())
# graph = [[]for _ in range(n+1)]

# visited = [False] * (n+1)
# depth = [0] * (n+1)

# for _ in range(n):
#    li = list(map(int, input().split()))
#    if len(li)>2:
#        for i in range(1,len(li)-1,2):
#            a,b = li[i], li[i+1]
#            graph[li[0]].append((a,b))
#
# def dfs(u):
#    visited[u] = True
#    for nxt, d in graph[u]:
#        if visited[nxt] == False:
#            depth[nxt] = depth[u] + d
#            dfs(nxt)

# dfs(1)

# k = depth.index(max(depth))
# depth = [0] *(n+1)
# visited = [False]*(n+1)

# dfs(k)

# print(max(depth))

# 지름을 깊이로 잘못 이해해서 dfs 하나만 했는데 알고보니 가장 먼 두 노드 값이었음.
# 그리고 depth로 한번에 처리하려고 한거 조금 아쉽고.
# 나머지는 좀 깔끔한 듯.

# 1967
# import sys
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# n = int(input())

# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# dist = [0] * (n+1)

# for _ in range(n-1):
#    a, b, c = map(int, input().split())
#    graph[a].append((b,c))
#    graph[b].append((a,c))

# def dfs(s):
#    visited[s] = True
#
#    for nxt, w in graph[s]:
#        if visited[nxt] == False:
#            dist[nxt] = dist[s] + w
#            dfs(nxt)
#
# dfs(1)
# k = dist.index(max(dist))

# visited = [False] * (n+1)
# dist = [0] * (n+1)

# dfs(k)

# print(max(dist))


# 1991
#import sys
#input =sys.stdin.readline


#n = int(input())
#graph = [[] for _ in range(n)]

#for _ in range(n):
#    a,b,c = map(str, input().split())
#    graph[ord(a)-65].append(b)
#    graph[ord(a)-65].append(c)

#def preorder(s):
#    print(chr(s+65), end='')
#    for x in graph[s]:
#        if x == '.':
#            continue
#        preorder(ord(x)-65)

#def inorder(s):
#    for i in range(2):
#        x = graph[s][i]
#        if i==0:
#            if x =='.':
#                print(chr(s+65), end='')
#                continue
#            inorder(ord(x)-65)
#            print(chr(s+65), end='')
#        else:
#            if x =='.':
#                continue
#            inorder(ord(x)-65)

#def postorder(s):
#    for x in graph[s]:
#        if x == '.':
#            continue
#        postorder(ord(x)-65)
#    print(chr(s+65), end='')

#preorder(0)
#print()
#inorder(0)
#print()
#postorder(0)

#정답은 맞췄는데 정석보다는 좀 가독성 떨어지는듯.
#정석은 ord써서 idx맞춰서 집어 넣되 함수에서 그냥 grahp[idx][0], [1] 이렇게만 씀.
#그럼 for문 필요도 없고 각 함수당 6줄 컷 가능. 담에는 더 깔끔하게 ㄲ

#1991
#import sys
#input = sys.stdin.readline

#print(ord('A'))
#print(chr(65))
#print(ord('.')) 46

#n = int(input())

#graph = [[] for _ in range(n+1)]


#for _ in range(n):
#    a,b,c = map(str, input().split())
#    
#    
#    graph[ord(a)-64].append(ord(b)-64)        # . 이면 -1 저장
#    graph[ord(a)-64].append(ord(c)-64)

#out = []
#visited = [False] * (n+1)

#def preorder(v):
#    if visited[v]:
#        return
#    
#    out.append(chr(v+64))
#    visited[v] = True
#    
#    for x in graph[v]:
#        if x == -18:
#            continue
#        
#        preorder(x)
#        if not visited[x]: 
#            out.append(chr(x+64))
#    
#preorder(1)    
#print(''.join(out))
#    
#out = []
#visited = [False] * (n+1)

#def inorder(v):
#    for x in graph[v]:
#        if x != -18:
#            inorder(x)
#            if not visited[x]:
#                out.append(chr(x+64))
#                visited[x] = True
#            
#        if not visited[v]:
#            out.append(chr(v+64))
#            visited[v]=True
#        
#inorder(1)
#print(''.join(out))

#out = []
#visited = [False] * (n+1)

#def postorder(v):
#    for x in graph[v]:
#        if x != -18:
#            postorder(x)
#            if not visited[x]:
#                out.append(chr(x+64))
#                visited[x] = True
#            
#    if not visited[v]:
#        out.append(chr(v+64))
#        visited[v]=True

#postorder(1)
#print(''.join(out))

#import sys
#input = sys.stdin.readline

#n = int(input())

#left = [-1] * 26
#right = [-1] * 26 

#for _ in  range(n):
#    a,b,c = input().split()
#    
#    left[ord(a)-ord('A')] = -1 if b == '.' else ord(b) - ord('A')
#    right[ord(a)-ord('A')] = -1 if c == '.' else ord(c) - ord('A')

#def preorder(v):
#    if v == -1:
#        return
#    print(chr(v+65), end='')
#    preorder(left[v])
#    preorder(right[v])

#def inorder(v):
#    if v ==-1:
#        return
#    inorder(left[v])
#    print(chr(v+65), end='')
#    inorder(right[v])

#def postorder(v):
#    if v ==-1:
#        return
#    postorder(left[v])
#    postorder(right[v])
#    print(chr(v+65), end='')

#preorder(0)
#print()
#inorder(0)
#print()
#postorder(0)

# 2263
#import sys
#input =sys.stdin.readline

#n = int(input())


# 5639


# 4803
#----------------------------REVIEW
#11725
#import sys
#from collections import deque
#input =sys.stdin.readline
#q=deque([1])

#n = int(input())

#graph = [[] for _ in range(n+1)]
#visited = [False] * (n+1)
#visited[1] = 1

#for _ in range(n-1):
#    a, b = map(int, input().split())
#    
#    graph[a].append(b)
#    graph[b].append(a)
#    
#while q:
#    cur = q.popleft()
#    
#    for nxt in graph[cur]:
#        if visited[nxt] ==False:
#            visited[nxt] = cur
#            q.append(nxt)

#print('\n'.join(map(str, visited[2:])))

#1167
#import sys
#from collections import deque
#input = sys.stdin.readline

#v = int(input())
#graph = [[] for _ in range(v+1)]
#dist = [-1] * (v+1)

#arr = [list(map(int,input().split())) for _ in range(v)]

#for i in range(v):
#    node = arr[i][0]  
#    for j in range(1, len(arr[i]) - 1, 2):
#        graph[node].append((arr[i][j], arr[i][j+1]))

#q = deque([(0,1)])
#dist[1] = 0

#while q:
#    d, r = q.popleft()
#    
#    for nxt, w in graph[r]:
#        if dist[nxt] ==-1:
#            dist[nxt] = d+w
#            q.append((d+w, nxt))
#        
#right = dist.index(max(dist))
#dist = [-1] * (v+1)
#dist[right] = 0

#q = deque([(0,right)])

#while q:
#    d, r = q.popleft()
#    
#    for nxt, w in graph[r]:
#        if dist[nxt] == -1:
#            dist[nxt] = d+w
#            q.append((d+w, nxt))
#    
#print(max(dist))