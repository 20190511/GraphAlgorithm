"""
문제
공항에는 G개의 탑승구가 있으며, 각각의 탑승구는 1번부터 G번까지의 번호로 구분됩니다.
공항에는 P개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1번부터 gi번째 (1 <= gi <= G) 탑승구 중 하나에 영구적으로 도킹해야 합니다.
이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있습니다.
또한 P개의 비행기를 순서대로 도킹하다가, 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우, 
그 시점에서 공항의 운행을 중지합니다.
공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 합니다.
비행기를 최대 몇 대 도킹할 수 있는지를 출력하는 프로그램을 작성하세요.

입력 조건
첫째 줄에는 탑승구의 수 G (1 <= G <= 100,000)가 주어집니다.
둘째 줄에는 비행기의 수 P (1 <= P <= 100,000)가 주어집니다.
다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보 gi (1 <= gi <= G)가 주어집니다.
이는 i번째 비행기가 1번부터 gi번째 (1 <= gi <= G) 탑승구 중 하나에 도킹할 수 있다는 의미입니다.

출력 조건
첫째 줄에 도킹할 수 있는 비행기의 최대 개수를 출력합니다.

[INPUT]
4
3 
4
1 
1

[OUTPUT]
2

[INPUT 2]
4
6
2
2
3
3
4
4

[OUTPUT 2]
3


[문제 풀이 및 피드백]
1.서로소 집합 알고리즘을 이용하면 계속 들어오는 입력값이 리스트에 존재하는지의 여부를
빠르게 확인할 수 있다.
(리스트에서 find() 보다 빠름.)

2. 문제에서 p의 입력이 1~p까지의 공항을 의미하였는데 잘못이해하고 풀었다.
    입력조건을 제대로 확인하자.

[피드백 2]
p의 값을 우선적으로 도킹할 수 있는 포트의 큰 숫자부터 도킹을 시도하면 된다.
    -> 그래서 find(par,pList[i]) 를 활용하여 루트가 0번이 될때까지 시도하면된다.
        만약 도킹이 된다면 find(par,root,root-1)를 하여 도킹을 계속해주자.
"""
import sys
input=sys.stdin.readline
def find(p,x):
    if x != p[x]:
        p[x] = find(p, p[x])
    return p[x]

def union(p,a,b):
    a,b = find(p,a),find(p,b)
    if a<b: p[b]=a
    else: p[a]=b 

g = int(input())
p = int(input())

pList = []
#공항개수 기준으로 정할 것.
par = [i for i in range(g+1)]
for i in range(p):
    pList.append(int(input()))

result = 0
for i in range(p):
    root = find(par,pList[i])
    if root == 0:
        break
    else:
        result += 1 
        union(par,root,root-1)
print(result)
        
