# 27323
# A = int(input())
# B = int(input())

# print(A*B)

# 1085
import sys

x, y, w, h = map(int, sys.stdin.readline().split())

if w - x > x:
    num1 = x
else:
    num1 = w - x

if h - y > y:
    num2 = y
else:
    num2 = h - y

if num1 > num2:
    print(num2)
else:
    print(num1)

# 3009


# 15894


# 9063


# 10101


# 5073


# 14215
