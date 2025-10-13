# 28278
import sys

input = sys.stdin.readline


def stack_one(x, li):
    li.append(x)


def stack_two(li):
    try:
        print(li[-1])
        li.pop()
    except IndexError:
        print("-1")


def stack_three(li):
    print(len(li))


def stack_four(li):
    if len(li):
        print("0")
    else:
        print("1")


def stack_five(li):
    try:
        print(li[len(li) - 1])
    except IndexError:
        print("-1")


n = int(input())
stack = []

for _ in range(n):
    order = list(map(int, input().split()))
    if order[0] == 1:
        num = order[1]
        stack_one(num, stack)
    if order[0] == 2:
        stack_two(stack)
    if order[0] == 3:
        stack_three(stack)
    if order[0] == 4:
        stack_four(stack)
    if order[0] == 5:
        stack_five(stack)

# try/except -> if & if not으로 고치기
# return 0, 1쓰면서 출력 킵해뒀다가 sys.stdout로 한번에 출력하기.(한줄한줄 바로 출력안해도 문제 없음)

# 10773


# 9012


# 4949


# 12789


# 18258


# 2164


# 11866


# 28279


# 2346


# 24511
