"""
학생들에게 0~N번의 번호를 부여할 때, 총 N+1개의 팀이 존재한다.
이떄 선생님은 두가지 옵션을 선택할 수 있다.  
  1. "팀 합치기" : 두 팀을 합치는 것
  2. "같은 팀 여부 확인": 특정한 두 학생이 같은 팀에 들어가 있는가 확인하는 것.

선생님이 M개의 연산을 하여 연산결과를 출력하는 프로그램을 작성하여라

첫째줄에 N,M 이 주어진다. (1<=N,M<=100,000)
다음 M개의 줄에는 0 a b 나 1 a b 형태로 값이 주어진다.
0 a b 는 a와 b 학생이 속한 팀을 합치는 것이고
1 a b 는 a와 b가 같은 팀에 속해있는지의 여부를 확인하는 것이다.
a,b는 양의 정수다.

같은 팀 여부 확인
[INPUT]
7 8 
0 1 3 
1 1 7 
0 7 6 
1 7 1 
0 3 7 
0 4 2 
0 1 1 
1 1 1

[OUTPUT]
NO
NO
YES
"""

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
par = [0]*(n+1)
for i in range(1, n+1):
    par[i] = i

def find_union(p,x):
    if x != p[x]:
        p[x] = find_union(p,p[x])
    return p[x]

def union(p,a,b):
    a,b = find_union(p,a), find_union(p,b)
    if a<b:
        p[b] = a
    else:
        p[a] = b

result = []
for _ in range(m):
    c,a,b = map(int, input().split())
    if c == 0:
        union(par,a,b)
    if c == 1:
        if find_union(par, a) == find_union(par, b):
            result.append("YES")
        else:
            result.append("NO")

print(*result)
        
