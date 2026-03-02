#1918
import sys
input = sys.stdin.readline

s = input().strip()

stack = []
out = []

prio = {'+': 1, '-':1, '*':2, '/':2}

for ch in s:
  if 'A' <= ch <= 'Z':
    out.append(ch)
  elif ch == '(':
    stack.append(ch)
  elif ch == ')':
    while stack and stack[-1] != '(':
      out.append(stack.pop())
    stack.pop()
  else:
    while stack and stack[-1] !='(' and prio[stack[-1]] >= prio[ch]:
      out.append(stack.pop())
    stack.append(ch)

while stack:
  out.append(stack.pop())

print(''.join(out))