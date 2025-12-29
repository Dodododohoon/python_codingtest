# 1463    -  못 품. heap. 시간 초과, dp 틀림.
# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = [0] * (n+1)

# for i in range(2,n+1):
#    dp[i] = dp[i-1] +1
#
#    if i %3 ==0:
#        dp[i] = min(dp[i], dp[i//3] +1)
#    if i%2 ==0:
#        dp[i] = min(dp[i], dp[i//2]+1)
#
# print(dp[n])

# # 2579        - 깔끔하게 clear, 너무 강렬해서 그냥 기억이남.
# import sys

# input = sys.stdin.readline

# n = int(input())
# li = [int(input()) for _ in range(n)]

# if n==1:
#     print(li[0])
#     exit()
# if n==2:
#     print(li[0]+li[1])
#     exit()


# dp = [0] * (n + 1)

# dp[1] = li[0]
# dp[2] = li[0] + li[1]


# for i in range(3, n + 1):
#     dp[i] = max(dp[i - 3] + li[i - 2], dp[i - 2]) + li[i - 1]

# print(dp[n])

# 9095        - 10~20분 컷. 나름 dp 잘짰다 싶긴했고 나름 잘 풀었는데 더 깔끔한 방식이 있네
# import sys

# input = sys.stdin.readline

# t = int(input())

# dp_1 = [0] * (11)
# dp_2 = [0] * (11)
# dp_3 = [0] * (11)

# dp_1[1] = 1
# dp_2[1] = 0
# dp_3[1] = 0

# dp_1[2] = 1
# dp_2[2] = 1
# dp_3[2] = 0

# for i in range(3, 11):
#     dp_1[i] = dp_1[i - 1] + dp_2[i - 1] + dp_3[i - 1]
#     dp_2[i] = dp_1[i - 1]
#     dp_3[i] = dp_2[i - 1]

# for _ in range(t):
#     n = int(input())
#     print(dp_1[n] + dp_2[n] + dp_3[n])

# 11726 - 10분 컷 매우 쉽노
# import sys

# input = sys.stdin.readline

# n = int(input())

# dp = [0] * (n + 1)

# dp[1] = 1

# if n>=2:
#   dp[2] = 2
#   for i in range(3, n + 1):
#       dp[i] = dp[i - 1] + dp[i - 2]

# print(dp[n] % 10007)
