# Divide & Conquer & Combine
# 패턴
# def solve(problem)
#2630
import sys
input=sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def solve(r,c,size):
    global white, blue
    
    first = paper[r][c]
    same = True
    
    for i in range(r, r+size):
        if not same: break
        for j in range(c, c+size):
            if paper[i][j] !=first:
                same = False
                break
    if same:
        if first == 0:
            white += 1
        else: blue += 1
        return
    
    half = size //2
    solve(r,c, half)
    solve(r,c+half,half)
    solve(r+half,c,half)
    solve(r+half,c+half,half)



#1992

#1780

#1629

#11401

#2740

#10830

#11444


#6549