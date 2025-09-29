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

while True:
    n = int(input())
    if n == -1:
        break
    li = []
    for i in range(1, n):
        if n % i == 0:
            li.append(i)

    if n == sum(li):
        print(n, "=", end=" ")
        print(" + ".join(map(str, li)))
    else:
        print(f"{n} is NOT perfect.")

# 1978

# 2581

# 11653
