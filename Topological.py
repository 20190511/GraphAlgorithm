# 사이클이 없는 그래프의 모든 노드를 방향성을 거스르지 않고 나열
"""
O(V+E)
  # 모든 노드를 거치면서 해당노드의 간선들을 다 체크하기 때문.
  

7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
from collections import deque
v,e = map(int, input().split())
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]
for _ in range(e):
  #a->b
  a,b = map(int,input().split())
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  reseult = []
  q = deque()
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      #i번 노드와 연결된 노드 진입차수 모두 제거
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
  for i in result:
    print(i, end=" ")

topology_sort()
