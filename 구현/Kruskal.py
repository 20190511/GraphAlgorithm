"""
#신장트리 알고리즘
# 사이클이 발생하지 않으면서 최소한의 경로비용으로
  모든 노드를 이을 수 있는 간선을 구성하는 알고리즘.
  O(ElogE) #간선을 정렬하는데 걸리는 시간.

7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""
def find_union(parent, x):
  if x != parent[x]:
    parent[x] = find_union(parent, parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a = find_union(parent,a)
  b = find_union(parent,b)
  if a<b:
    parent[b] = parent[a]
  else:
    parent[a] = parent[b]


v,e = map(int, input().split())
parent = [0]*(v+1)
for i in range(1, v+1):
  parent[i] = i

elist = []
result = 0
for i in range(e):
  a,b,c = map(int, input().split())
  elist.append((c,a,b))

elist.sort()

for edges in elist:
  cost,a,b = edges
  if find_union(parent,a) != find_union(parent,b):
    result += cost
    union_parent(parent,a,b)
print(result)
