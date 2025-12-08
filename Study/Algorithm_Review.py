#BackTracking
#15649 - 바로 안 떠올랐음.
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n+1)
arr=[]

def BT(num):
    if num == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1,n+1):
        if visited[i] == False:
            visited[i] = True
            arr.append(i)
            BT(num+1)
            arr.pop()
            visited[i] = False
            
BT(0)
