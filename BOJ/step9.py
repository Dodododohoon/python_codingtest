# 5086
# import sys

# n, m = 1, 1

# while True:
#     n, m = map(int, sys.stdin.readline().split())
#     if n == 0 and m == 0:
#         break
#     elif m % n == 0:
#         print("factor")
#     elif n % m == 0:
#         print("multiple")
#     else:
#         print("neither")

# 2501
# n, k = map(int, input().split())

# li = []

# for i in range(1, n+1):
#     if n % i == 0:
#         li.append(i)

# try:
#     print(li[k - 1])
# except IndexError:
#     print("0")

# 9506

# while True:
#     n = int(input())
#     if n == -1:
#         break
#     li = []
#     for i in range(1, n):
#         if n % i == 0:
#             li.append(i)

#     if n == sum(li):
#         print(n, "=", end=" ")
#         print(" + ".join(map(str, li)))
#     else:
#         print(f"{n} is NOT perfect.")

# 1978
# import sys

# n = int(sys.stdin.readline())
# num = map(int, sys.stdin.readline().split())
# cnt = 0

# for s in num:
#     if s == 1:
#         continue
#     if s == 2 or s == 3:
#         cnt += 1
#         continue
#     for i in range(2, s):
#         if s % i == 0:
#             break
#         elif i == (s - 1):
#             cnt += 1

# print(cnt)

# 2581
import sys


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


m = int(sys.stdin.readline())
k = int(sys.stdin.readline())
li = []

for i in range(m, k + 1):
    if is_prime(i):
        li.append(i)
if len(li) > 1:
    print(sum(li))
    print(li[0])
else:
    print("-1")

# 11653
