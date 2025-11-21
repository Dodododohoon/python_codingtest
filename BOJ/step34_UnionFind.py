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
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
rank = [0] * (n+1)

def find(a):
    if parent[a] != a :
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] +=1

for i in range(n):
    li = list(map(int,input().split()))
    for j in range(n):
        if li[j]==1:
            union(i+1,j+1)

li = list(map(int,input().split()))
check = find(li[0])

for x in li:
    if check != find(x):
        print('NO')
        break
else:
    print("YES")


#4195


#20040


