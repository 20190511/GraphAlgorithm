"""
6 4
1 4
2 3
2 4
5 6
"""

"""
# 느린 find_parent 기법
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x
"""

def find_parent(parent, x):
  #루트 노드가 아니라면, 루트노드를 찾을 때 까지 호출.
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


#두 원소가 속한 집합을 합치기.
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


v,e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

for i in range(e):
  a,b = map(int, input().split())
  union_parent(parent,a,b)

#모든 노드의 루트노드를 출력해줌.
print("각 원소가 속한 집합 :", end=" ")
for i in range(1, v+1):
  print(find_parent(parent, i),end=" ")
print()

print("부모 테이블 :", end=" ")
for i in range(1, v+1):
  print(parent[i], end=" ")

 
