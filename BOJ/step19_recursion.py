# 27433
def fect(x):
    if x == 1 or x == 0:
        return 1
    else:
        return fect(x - 1) * x


n = int(input())

print(fect(n))
