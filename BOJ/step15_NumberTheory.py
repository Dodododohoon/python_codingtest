# 1934
# def gcd(a,b):
#    while b:
#        a, b = b, a%b
#    return a

# def lcm(a,b):
#    return a * b //gcd(a,b)

# t = int(input())

# for _ in range(t):
#    n, m = map(int,input().split())
#    print(lcm(n,m))

# 13241
# def gcd(a,b):
#    while b:
#        a, b = b, a%b
#    return a

# def lcm(a,b):
#    return a * b //gcd(a,b)

# n, m = map(int,input().split())
# print(lcm(n,m))

# 1735
# def gcd(a,b):
#    while b:
#        a,b=b,a%b
#    return a

# def lcm(a,b):
#    return a*b//gcd(a,b)

# a1, a2 = map(int, input().split())
# b1, b2 = map(int, input().split())
# c1, c2 = a1*b2+b1*a2,a2*b2

# k=gcd(c1,c2)
# print(c1//k, c2//k)

# 2485
# import sys

# input = sys.stdin.readline


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# n = int(input())
# trees = [int(input()) for _ in range(n)]

# g = 0
# for i in range(1, n):
#     g = gcd(g, trees[i] - trees[i - 1])

# total = (trees[-1] - trees[0]) // g + 1  # 등차수열 항 개수
# print(total - n)

# 원리는 이해했는데, 계속 꼬여서 안풀리더라 그래서 걍 gpt로 품.. 담에 풀면 무조건 맞을 듯.

# 4134
# import sys
# input = sys.stdin.readline

# def is_prime(x):
#     if x < 2:
#         return False
#     elif x in (2, 3):
#         return True
#     elif x % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(x ** (0.5))+1, 2):
#             if x % i == 0:
#                 return False
#         return True


# n = int(input())
# for _ in range(n):
#     num = int(input())
#     while is_prime(num) == False:
#         num += 1
#     print(num)

# while not xxx 쓸 수 있네
# 처음에 is_prime 함수에서 x**0.5하고 +1을 안 넣어줘서 틀렸었음.

# # 1929
# m, n = map(int, input().split())

# li = [False] * (n + 1)
# li[2] = True

# for x in range(3, n + 1, 2):
#     li[x] = True

# for i in range(3, int(n ** (0.5)) + 1, 2):
#     if li[i] == True:
#         start = i * i
#         step = 2 * i
#         for x in range(start, n + 1, step):
#             li[x] = False


# for x in range(m, n+1):
#     if li[x]:
#         print(x)

# 다시 한번풀어보자. 솔찍히 내 힘으로 푼게 아니다.

# 4948


# 17103


# 13909
import sys
import math

input = sys.stdin.readline

n = int(input().strip())

print(math.isqrt(n))  # n의 정수 제곱근

# 그냥 gpt 받음.
