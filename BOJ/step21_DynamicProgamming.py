# 동적 계획법 핵심은 중복되는 계산은 기억해두고 푼다.
# 메모리를 사용해서 연산을 줄인다.

# 24416
# n = int(input())

# if n==1 or n==2:
#    print(1,0)
# else:
#    f1, f2 =1, 1
#    for _ in range(3, n+1):
#        f1 ,f2 = f2, f2+ f1
#    print(f2, n-2)

# 9184
# import sys
# input = sys.stdin.readline

# cache ={}

# def w(a,b,c):
#    if a<= 0 or b <= 0 or c <= 0:
#        return 1
#    elif a> 20 or b>20 or c>20:
#        return w(20,20,20)
#    elif (a,b,c) in cache:
#        return cache[(a,b,c)]
#
#    if a < b< c :
#        cache[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
#    else:
#        cache[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) +w(a-1,b,c-1) - w(a-1,b-1,c-1)
#    return cache[(a,b,c)]

# for line in sys.stdin:
#    a,b,c = map(int, line.split())
#    if a==-1 and b==-1 and c==-1:
#        break
#    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")

# 동적계획법 거의 첫 문제.

# 1904
# import sys
# input = sys.stdin.readline

# n = int(input())

# memo = {}
# memo[1] = 1
# memo[2] = 2
#
# for i in range (3,n+1):
#    memo[i] = (memo[i-1]+memo[i-2])%15746
#
# print(memo[n])
# -------============밑에 recusionError
# def dp(n):
#    global memo
#    if n in memo:
#        return memo[n]
#    else:
#        memo[n] = dp(n-1) +dp(n-2)
#        return memo[n]
#
# print(dp(n)%15746)

# 딕셔너리 그냥 리스트 써도 상관없음
# 처음에 재귀 형태로 썼다가 for 문으로 바텀업 DP하니깐 클리어

# 9461
# import sys

# input = sys.stdin.readline

# pn = [1, 1, 1, 2, 2]

# n = int(input())
# for _ in range(n):
#     num = int(input())
#     if num > len(pn):
#         for i in range(len(pn), num):
#             pn.append(pn[i - 1] + pn[i - 5])
#     print(pn[num - 1])

# 1912
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0 for _ in range(n)]
# dp[0] = arr[0]

# for i in range(1, n):
#     dp[i] = max(arr[i], dp[i - 1] + arr[i])

# print(max(dp))

# 아.. 풀만했는데 아 .. 종이 있었으면 나앗을라나?
# 점화식만 뽑아내면 어렵지 않음.

# 1149
# import sys
# input = sys.stdin.readline

# n= int(input())

# a,b,c = map(int, input().split())

# for _ in range(n-1):
#    p,q,r = map(int, input().split())
#
#    s1 = p + min(b,c)
#    s2 = q +min(a,c)
#    s3 = r + min(a,b)
#
#    a, b,c = s1,s2,s3
#
# print(min(a,b,c))

# DP 테이블을 만들 수 있음.
# dp[i][0] = R[i] + min(dp[i-1][1], dp[i-1][2]) 이런식으로

# 내께 메모리도 아껴서 더 좋긴한데 난 학습하고 있으니. 테이블 쓰려고 해보자.

# 1932
# import sys
# input = sys.stdin.readline

# n=int(input())

# li=[list(map(int, input().split())) for _ in range(n)]
# dp = li[:]

# for i in range(0, n):
#    if i ==0:
#        continue
#    for j in range(i+1):
#        if j==0:
#            dp[i][0] = li[i][0] + li[i-1][0]
#        elif j==i:
#            dp[i][j] = li[i][j] + li[i-1][j-1]
#        else:
#            dp[i][j] = li[i][j] + max(li[i-1][j-1], li[i-1][j])

# print(max(dp[n-1]))

# dp = li[:] 이부분 자칫하다간 틀릴뻔 했음. (얕은 복사)
# 내가 우려했던대로 같은 값을 가르키고 있는게 맞네? append로 해서 다르게 출력되길레 다르구나 했는데. append해서 추가된 값은 따로고
# 기존 내부 값들은 똑같이 가르키고 있대.
# li나 dp 수정하면 같이 바뀌는거지.

# 깊은 복사 하려면. dp = [x[:] for x in li] 이렇게 해야함.

# 2579
import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
arr.insert(0, 0)

dp = [0 for _ in range(n + 1)]


if n >= 4:
    dp[1] = arr[1]
    dp[2] = arr[2] + arr[1]
    dp[3] = max(arr[1], arr[2]) + arr[3]

    for i in range(4, n + 1):
        dp[i] = max(dp[i - 2], arr[i - 1] + dp[i - 3]) + arr[i]
    print(dp[n])

elif n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1] + arr[2])
elif n == 3:
    print(max(arr[1], arr[2]) + arr[3])


# 1463

# 10844

# 2156

# 11053

# 11054

# 2565

# 9251

# 12865
