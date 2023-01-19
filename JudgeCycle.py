"""
3 3
1 2
1 3
2 3
"""

#서로소 집합을 활용한 사이클 판단.
def find_union(parent, x):
  if x != parent[x]:
    parent[x] = find_union(parent,parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_union(parent,a)
  b = find_union(parent,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
v,e = map(int, input().split())
parent = [0] * (v+1)
parent[0] = 0
for i in range(1,v+1):
  parent[i] = i

cycle = False
for _ in range(e):
  a,b = map(int, input().split())
  if find_union(parent, a) == find_union(parent, b):
    cycle = True
    break 
  else:
    union_parent(parent, a, b)

if cycle:
  print("Cycle !")
else:
  print("NO Cycle")
