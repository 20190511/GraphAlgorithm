"""
1647번 : 도시 분할 계획
https://www.acmicpc.net/problem/1647

[내 풀이 - 풀이 동일]
크루스칼 알고리즘 후 가장 긴 길 끊어버리면된다.
"""

import sys
input = sys.stdin.readline
def find(p,x):
    if x != p[x]:
        p[x] = find(p,p[x])
    return p[x]

def union(p,a,b):
    a,b = find(p,a),find(p,b)
    if a<b:
        p[b] = a
    else:
        p[a] = b 

n,m = map(int, input().split())
p = [0]*(n+1)
for i in range(1,n+1):
    p[i] = i 
mList = []

for _ in range(m):
    a,b,cost = map(int, input().split())
    mList.append((cost,a,b))
mList.sort()

result = 0
maxs = 0
for cost,a,b in mList:
    if find(p,a) != find(p,b):
        union(p,a,b)
        result += cost
        maxs = cost
print(result-maxs)
        
        
    
