# 28278
#import sys

#input = sys.stdin.readline


#def stack_one(x, li):
#    li.append(x)


#def stack_two(li):
#    try:
#        print(li[-1])
#        li.pop()
#    except IndexError:
#        print("-1")


#def stack_three(li):
#    print(len(li))


#def stack_four(li):
#    if len(li):
#        print("0")
#    else:
#        print("1")


#def stack_five(li):
#    try:
#        print(li[len(li) - 1])
#    except IndexError:
#        print("-1")


#n = int(input())
#stack = []

#for _ in range(n):
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
#import sys
#input=sys.stdin.readline
#stack=[]

#n = int(input())
#for _ in range(n):
#    num=int(input())
#    if num==0:
#        stack.pop()
#    else:
#        stack.append(num)
#print(sum(stack))
        
# 9012
#import sys
#input=sys.stdin.readline

#n=int(input())

#for _ in range(n):
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
#import sys
#input = sys.stdin.readline

#while True:
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



# 18258


# 2164


# 11866


# 28279


# 2346


# 24511
