#서로소 집합(Disjoint Set)을 관리하는 자료구조
#대표 기능: 두 원소가 같은 그룹인지 확인(find), 두 그룹 합치기(union)

#1717
#import sys
#sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

#n,m = map(int, input().split())

#parent = [i for i in range(n+1)]
#rank = [0] * (n+1)

#def find(a):
#    if parent[a] != a:
#        parent[a] = find(parent[a])
#    return parent[a]

#def union(a, b):
#    a = find(a)
#    b = find(b)
#    if a != b:
#        if rank[a] > rank[b]:
#            parent[b] = a
#        else:
#            parent[a]=b
#            if rank[a] == rank[b]:
#                rank[b] +=1
#    
#def uf(a,b):
#    if find(a) == find(b):
#        return 'YES'
#    else:
#        return 'NO'

#for _ in range(m):
#    l,m,n = map(int,input().split())
#    if l ==0:
#        union(m,n)
#    else:
#        print(uf(m,n))
        
#1976
#import sys
#sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

#n = int(input())
#m = int(input())

#parent = [i for i in range(n+1)]
#rank = [0] * (n+1)

#def find(a):
#    if parent[a] != a :
#        parent[a] = find(parent[a])
#    return parent[a]

#def union(a,b):
#    a = find(a)
#    b = find(b)
#    if a != b:
#        if rank[a] < rank[b]:
#            parent[a] = b
#        else:
#            parent[b] = a
#            if rank[a] == rank[b]:
#                rank[a] +=1

#for i in range(n):
#    li = list(map(int,input().split()))
#    for j in range(n):
#        if li[j]==1:
#            union(i+1,j+1)

#li = list(map(int,input().split()))
#check = find(li[0])

#for x in li:
#    if check != find(x):
#        print('NO')
#        break
#else:
#    print("YES")


#4195                            키랑 값이랑 연결 짓는 문제는 딕셔너리로. O(1)임.
#import sys
#sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

#t = int(input())

#for _ in range(t):
#    f = int(input())
#    parent = [i for i in range(2*f +1)]
#    dict = {}
#    cnt = [1] * (2*f + 1)
#    idx = 0
#    
#    def find(a):
#        if a != parent[a]:
#            parent[a] = find(parent[a])
#        return parent[a]
#        
#    def union(a,b):
#        a = find(a)
#        b = find(b)
#        
#        if a != b:
#            parent[b] = a
#            temp = cnt[a]
#            cnt[a] += cnt[b]
#            cnt[b] += temp
#            
#    for _ in range(f):
#        a,b = map(str, input().split())
#        
#        if not a in dict:
#            dict[a] = idx
#            idx+=1
#        index_a = dict.get(a)
#        if not b in dict:
#            dict[b] = idx
#            idx +=1
#        index_b = dict.get(b)
#        
#        union(index_a,index_b)
#        print(cnt[find(index_a)])
        
#20040


#---------------------
#1976
#import sys
#input =sys.stdin.readline

#n = int(input())
#m = int(input())

#graph = [list(map(int, input().split())) for _ in range(n)]
#parent = [i for i in range(n+1)]
#rank = [0] * (n+1)

#check = list(map(int, input().split()))

#def find(v):
#    if parent[v] != v:
#        parent[v] = find(parent[v])
#    return parent[v]

#def union(a,b):
#    a = find(a)
#    b = find(b)
#    
#    if a==b:
#        return
#    
#    if rank[a] < rank[b]:
#        parent[a] = b
#    else:
#        parent[b] = a
#        if rank[a] == rank[b]:
#            rank[a] += 1
#       
#for i in range(n):
#    for j in range(n):
#        if graph[i][j] == 1:
#            union(i+1,j+1)

#root = parent[check[0]]
#for x in check[1:]:
#    if parent[x] != root:
#        print('NO')
#        exit()

#print('YES')

#4195
#import sys
#input = sys.stdin.readline

#t = int(input())

#for _ in range(t):
#    f = int(input())
#    d = {}
#    idx = 1
#    parent = [i for i in range(2*f+1)]
#    size = [1] * (2*f+1)
#    
#    def find(a):
#        if parent[a] != a:
#            parent[a] = find(parent[a])
#        return parent[a]
#    
#    def union(a,b):
#        a=find(a)
#        b=find(b)
#        
#        if a==b:
#            return size[a]
#        
#        if size[a] < size[b]:
#            parent[a] = b
#            size[b] += size[a]
#            return size[b]
#        else:
#            parent[b] = a
#            size[a] += size[b]
#            return size[a]    
#    
#    for _ in range(f):
#        arr = list(map(str, input().split()))
#        
#        for x in arr:
#            if x in d:
#                continue
#            d[x] = idx
#            idx += 1
#        
#        a= d[arr[0]]
#        b= d[arr[1]]
#        
#        ans = union(a,b)
#        print(ans)
#        
        
        
    
