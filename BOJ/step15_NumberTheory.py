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
import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


input = sys.stdin.readline

n = int(input())
a = int(input())
s1 = set()
s1.add(a)
gap = 1000000000

for _ in range(n - 1):
    b = int(input())
    s1.add(b)
    k = b - a
    g = gcd(k, gap)
    if gap > k:
        gap = g

total_tree = (b - a) // gap + 1
add_tree = total_tree - len(s1)

print(gap)
print(total_tree)
print(add_tree)


# 4134


# 1929


# 4948


# 17103


# 13909
