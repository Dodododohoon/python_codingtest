# Divide & Conquer & Combine
# # 패턴
# def solve(problem):
#     if base_case(problem):          #더이상 나눌 수 없으면
#         return
#     sub1, sub2 = divide(problem)    #문제를 나누고
#     res1 = solve(sub1)              #각각 해결
#     res2 = solve(sub2)
#     return combine(res1, res2)      #결과 합치기

# 2630
#import sys

#input = sys.stdin.readline

#n = int(input())
#paper = [list(map(int, input().split())) for _ in range(n)]

#white = 0
#blue = 0

#def solve(r, c, d):
#    global white, blue
#    
#    first = paper[r][c]
#    same = True
#    
#    for i in range(r, r+d):
#        for j in range(c, c+d):
#            if paper[i][j] != first:
#                same = False
#                break
#            
#    if same:
#        if first == 1:
#            blue += 1
#            return
#        else:
#            white += 1
#            return
#    
#    solve(r,c,d//2)
#    solve(r,c+d//2,d//2)
#    solve(r+d//2,c,d//2)
#    solve(r+d//2,c+d//2,d//2)

#solve(0,0,n)
#print(white)
#print(blue)

# 1992
#import sys
#input = sys.stdin.readline

#n = int(input())
#li = [input().strip() for _ in range(n)]

#out = []

#def solve(r,c,d):
#    first = li[r][c]
#    same = True
#    
#    for i in range(r, r+d):
#        for j in range(c, c+d):
#            if li[i][j] != first:
#                same = False
#                break
#    
#    if same:
#        if first == '1':
#            out.append('1')
#            return
#        else:
#            out.append('0')
#            return
#    
#    out.append('(')
#    solve(r,c,d//2)
#    solve(r,c+d//2,d//2)
#    solve(r+d//2,c,d//2)
#    solve(r+d//2,c+d//2,d//2)
#    out.append(')')

#solve(0,0,n)
#print(''.join(out))

# 1780

# 1629

# 11401

# 2740

# 10830

# 11444


# 6549
