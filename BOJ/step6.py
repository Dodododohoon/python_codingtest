# 25083
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\\/")
# print("      |")
# print("      |")

# 3003
# import sys

# li1 = [1, 1, 2, 2, 2, 8]
# li2 = list(map(int, sys.stdin.readline().split()))

# for i in range(6):
#    print(li1[i] - li2[i], end=" ")

# 2444
# n = int(input())
# for i in range(2 * n - 1):
#     if i <= n - 1:
#         print(" " * ((n - 1) - i), "*" * (2 * i + 1), " ", sep="")
#     else:
#         print(" " * (i - (n - 1)), "*" * (2 * ((2 * n - 2) - i) + 1), " ", sep="")

# 10988
# import sys

# li = sys.stdin.readline().strip()
# if li == li[::-1]:
#     print("1")
# else:
#     print("0")

# 1157
# import sys

# li = sys.stdin.readline().strip()
# li_ord = list(map(ord, li.upper()))  # 65'A'~90'Z'
# li_cnt = [0] * 26

# for i in range(65, 91):
#     li_cnt[i - 65] = li_ord.count(i)

# if li_cnt.count(max(li_cnt)) == 1:
#     idx = li_cnt.index(max(li_cnt))
#     print(chr(idx + 65))
# else:
#     print("?")

# 2941
# import sys

# li = sys.stdin.readline().strip()
# li = li.replace("dz=", "*")
# li = li.replace("c=", "*")
# li = li.replace("c-", "*")
# li = li.replace("d-", "*")
# li = li.replace("lj", "*")
# li = li.replace("nj", "*")
# li = li.replace("s=", "*")
# li = li.replace("z=", "*")
# print(len(li))

# 1316
# import sys

# num = int(sys.stdin.readline().strip())
# cnt = 0

# for _ in range(num):
#     li = sys.stdin.readline().strip()
#     check = 0
#     for i in range(len(li)):
#         if check == 1:
#             break
#         elif i == len(li) - 1:
#             cnt += 1
#             break
#         elif li[i] == li[i + 1]:
#             continue
#         else:
#             for j in range(i + 1, len(li)):
#                 if li[j] == li[i]:
#                     check = 1
#                     break
# print(cnt)
# ===========================================
# import sys

# def is_group(s:str) -> bool:
#     seen = set()
#     prev = None
#     for ch in s:
#         if ch != prev:
#             if ch in seen:
#                 return False
#             if prev is not None:
#                 seen.add(prev)
#         prev = ch
#     return True

# n=int(sys.stdin.readline())
# ans = 0
# for _ in range(n):
#     if is_group(sys.stdin.readline().strip()):
#         ans+=1
# print(ans)

# 25206
import sys


def lecture(s: str):
    li = s.split()
