#“백트래킹(Backtracking)”은 모든 경우의 수를 탐색하되, 불가능한 경우는 일찍 포기하고 되돌아가는 알고리즘이에요.
#즉, **완전탐색(Brute Force)**를 똑똑하게 줄인 형태라고 볼 수 있습니다.
#재귀가 기본형태니깐 트리구조를 생각하는게 Best

#15649
#import sys
#input = sys.stdin.readline

#n,m = map(int, input().split())
#visited = [False] * (n+1)
#arr = []

#def BT(num):
#    if num ==m:
#        print(' '.join(map(str, arr)))
#        return
#    for i in range(1,n+1):
#        if visited[i] ==False:
#            visited[i] = True
#            arr.append(i)
#            BT(num+1)
#            visited[i]=False
#            arr.pop()

#BT(0)

#15650
#import sys
#input = sys.stdin.readline

#n, m = map(int, input().split())
#visited = [False] * (n+1)
#arr=[]

#def df(num,k):
#    if num ==m:
#        print(' '.join(map(str, arr)))
#        return
#    for i in range(k,n+1):
#        arr.append(i)
#        df(num+1,i+1)
#        arr.pop()
#    
#df(0, 1)
#아 visited를 쓸필요가 없네? 생각해보니 맞네, 순열일때는 필요하고, 조합일때는 필요 없고.

#15651
#import sys
#input = sys.stdin.readline

#n, m = map(int, input().split())
#arr=[]

#def df(num):
#    if num ==m:
#        print(' '.join(map(str, arr)))
#        return
#    for i in range(1,n+1):
#        arr.append(i)
#        df(num+1)
#        arr.pop()
#    
#df(0)

#변수명 num -> depth로 바꾸자.

#15652

#9663

#2580

#14888

#14889