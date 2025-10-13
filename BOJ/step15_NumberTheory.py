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
import sys

input = sys.stdin.readline


def is_prime(x):
    if x < 2:
        return False
    elif x in (2, 3):
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(x ** (0.5)), 2):
            if x % i == 0:
                return False
        return True


n = int(input())
for _ in range(n):
    num = int(input())
    while is_prime(num) == False:
        num += 1
    print(num)


# 1929


# 4948


# 17103


# 13909
