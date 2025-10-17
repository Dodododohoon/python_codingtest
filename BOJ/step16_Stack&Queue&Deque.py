# 28278
# import sys

# input = sys.stdin.readline


# def stack_one(x, li):
#    li.append(x)


# def stack_two(li):
#    try:
#        print(li[-1])
#        li.pop()
#    except IndexError:
#        print("-1")


# def stack_three(li):
#    print(len(li))


# def stack_four(li):
#    if len(li):
#        print("0")
#    else:
#        print("1")


# def stack_five(li):
#    try:
#        print(li[len(li) - 1])
#    except IndexError:
#        print("-1")


# n = int(input())
# stack = []

# for _ in range(n):
#    order = list(map(int, input().split()))
#    if order[0] == 1:
#        num = order[1]
#        stack_one(num, stack)
#    if order[0] == 2:
#        stack_two(stack)
#    if order[0] == 3:
#        stack_three(stack)
#    if order[0] == 4:
#        stack_four(stack)
#    if order[0] == 5:
#        stack_five(stack)

# try/except -> if & if not으로 고치기
# return 0, 1쓰면서 출력 킵해뒀다가 sys.stdout로 한번에 출력하기.(한줄한줄 바로 출력안해도 문제 없음)

# 10773
# import sys
# input=sys.stdin.readline
# stack=[]

# n = int(input())
# for _ in range(n):
#    num=int(input())
#    if num==0:
#        stack.pop()
#    else:
#        stack.append(num)
# print(sum(stack))

# 9012
# import sys
# input=sys.stdin.readline

# n=int(input())

# for _ in range(n):
#    ps=input().strip()
#    cnt=0
#    for x in ps:
#        if cnt ==-1:
#            break
#        elif x =='(':
#            cnt+=1
#        else:
#            cnt-=1
#    print('YES' if cnt==0 else 'NO')

# 4949
# import sys
# input = sys.stdin.readline

# while True:
#    stack=[]
#    con = True
#    str = input()
#    if str[0] == '.':
#        break
#    for x in str:
#        if x== '(' or x=='[':
#            stack.append(x)
#        if x==')':
#             if len(stack) ==0:
#                 con=False
#                 break
#             else:
#                  if stack[-1] =='(':
#                      stack.pop()
#                  else:
#                      con=False
#                      break
#        if x==']':
#             if len(stack) ==0:
#                 con=False
#                 break
#             else:
#                  if stack[-1] =='[':
#                      stack.pop()
#                  else:
#                      con=False
#                      break
#    print('yes' if con and not stack else 'no')

#        if x==')':        =>이게 더 씸플
#             if not stack or stack[-1] !='(':
#                 con=False
#                 break
#             stack.pop()

# not stack or stack[-1] 이게 indexError 안뜨는 이유가 not stack부터 검사해서.
# 마지막 출력때 and not stack 틀렸었음.

# 12789
# import sys
# input = sys.stdin.readline

# n=int(input())
# li=map(int, input().split())
# stack=[]
# cnt=1
# ok ='Nice'

# def check(s,k):
#    if len(s)>0 and s[-1] ==k:
#        s.pop()
#        return True
#    return False

# for x in li:
#    if len(stack) >0 and stack[-1] < x:
#        ok = 'Sad'
#        break
#    stack.append(x)
#    while check(stack, cnt):
#        cnt+=1
#        True

# print(ok)

# 꽤 오래 풀음. 스트레쓰 때문일 수도 있고 뭔가 이런 해석 문제는 또 처음이라 그런거 같기도하고.
# if len(s) >0 이렇게 말고 그냥 if s 해도 됨.

# 18258
# import sys
# from collections import deque

# n = int(sys.stdin.readline())
# q=deque()
# sign =[]

# for _ in range(n):
#    order=sys.stdin.readline().split()
#    cmd = order[0]
#    if cmd== "push":
#        q.append(order[1])
#    if cmd =='pop':
#        if q:
#            sign.append(q[0])
#            q.popleft()
#        else:
#            sign.append('-1')
#    if cmd =='size':
#        sign.append(len(q))
#    if cmd =='empty':
#        if q:
#            sign.append('0')
#        else:
#            sign.append('1')
#    if cmd =='front':
#        if q:
#            sign.append(q[0])
#        else:
#            sign.append('-1')
#    if cmd =='back':
#        if q:
#            sign.append(q[-1])
#        else:
#            sign.append('-1')

# print('\n'.join(map(str, sign)))

# 아무리 요소값이 하나여도 order[0]이랑 order은 다르다. str, list
# 따라서 order[0] == 'pop'이 참이어도 order == 'pop'은 무조건 False다 (자료형 달라서)

# q.append(x)        # 오른쪽(뒤)에 삽입 → enqueue
# q.appendleft(x)    # 왼쪽(앞)에 삽입
# q.pop()            # 오른쪽(뒤)에서 꺼냄
# q.popleft()        # 왼쪽(앞)에서 꺼냄 → dequeue
# q.clear()          # 큐 비우기
# q.reverse()        # 순서 뒤집기

# 2164
# from collections import deque
# n=int(input())

# q=deque([i for i in range(1,n+1)])

# while len(q)>1:
#    q.popleft()
#    if len(q) ==1:
#        break
#    tmp = q[0]
#    q.popleft()
#    q.append(tmp)
# print(q[0])

# 굳이 if 없어도 됨. 두번째꺼는 개수가 줄어드는 건 아니니깐
# q.append(q.popleft())가능 q.popleft()자체가 반환값이 있어서.

# 11866
# from collections import deque

# n, k = map(int, input().split())

# q=[i for i in range(1,n+1)]        인덱스 풀이
# li=[]
# idx=0
# print('<',end='')
# while len(q)>0:
#    idx = (idx +k -1) % len(q)
#    li.append(q.pop(idx))
# print(', '.join(map(str,li)), end='>')

# q=deque([i for i in range(1,n+1)])    rotate 풀이
# li=[]

# while len(q)>0:
#    q.rotate(-(k-1))
#    li.append(q.popleft())
# print(f"<{', '.join(map(str, li))}>")

# # 28279
# from collections import deque
# import sys

# input = sys.stdin.readline

# n = int(input())
# q = deque()
# out = []

# for _ in range(n):
#     order = input().split()
#     if order[0] == "1":
#         q.appendleft(order[1])
#     elif order[0] == "2":
#         q.append(order[1])
#     elif order[0] == "3":
#         if q:
#             out.append(q.popleft())
#         else:
#             out.append("-1")
#     elif order[0] == "4":
#         if q:
#             out.append(q.pop())
#         else:
#             out.append("-1")
#     elif order[0] == "5":
#         out.append(len(q))
#     elif order[0] == "6":
#         if q:
#             out.append("0")
#         else:
#             out.append("1")
#     elif order[0] == "7":
#         if q:
#             out.append(q[0])
#         else:
#             out.append("-1")
#     elif order[0] == "8":
#         if q:
#             out.append(q[-1])
#         else:
#             out.append("-1")

# sys.stdout.write("\n".join(map(str, out)))

# 2346
from collections import deque
import sys

input = sys.stdin.readline


n = int(input())
li = input().split()
q = deque(i for i in range(1, n + 1))
out = []

dic = {i: int(li[i - 1]) for i in range(1, n + 1)}

while q:
    num = q.popleft()  # 제일 왼쪽에 있는거 pop 저장
    out.append(num)  # 뺀 거 기억
    k = dic[num]  # 뺀 수 종이 확인
    if k > 0:  # 종이 수 만큼 이동
        q.rotate(-(k - 1))
    else:
        q.rotate(-k)

sys.stdout.write(" ".join(map(str, out)))
print(li)
print(dic)


# 24511
