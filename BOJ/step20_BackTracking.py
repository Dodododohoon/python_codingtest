#“백트래킹(Backtracking)”은 모든 경우의 수를 탐색하되, 불가능한 경우는 일찍 포기하고 되돌아가는 알고리즘이에요.
#즉, **완전탐색(Brute Force)**를 똑똑하게 줄인 형태라고 볼 수 있습니다.

#15649
n,m = map(int, input().split())

for i in range(1,n+1):
    for j in range(1, m+1):
        if j==i:
            continue
        print(i, j)


#15650

#15651

#15652

#9663

#2580

#14888

#14889