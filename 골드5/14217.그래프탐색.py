'''
문제
남규나라의 왕 zych는 도로 정비 계획을 발표하였다. 두 도시를 잇는 도로들을 새로 만들거나, 안전상의 문제로 도로를 없애기도 할 계획이다. 도로 정비 계획은 두 도시와, 만들건지, 없앨건지에 대한 정보가 주어지는데, 도로를 정비하는 일은 매우 큰 일이기에 계획을 순서대로 하나씩 시행해 나갈 것이다. 상황에 따라서는 계획에 포함돼서 만들어진 도로를 제거할 수도 있다.

Zych는 차후 도로 정비 계획에 참고하기 위하여, 각 도시들이 수도에 방문하는데 최소 몇 개의 도시들을 방문해야 하는지 조사하기로 하였다.

남규나라의 초기 도시상태가 주어지고 도로 정비계획이 주어질 때, 한 도로가 정비될 때마다 각 도시별로 수도를 방문하는 데 최소 방문 도시들을 출력하시오.

입력
첫째 줄에는 도시의 개수 n,도로의 개수 m이 주어진다. 다음 m개의 줄에는 두 도시가 주어진다.(2≤n≤500,1≤m≤n*(n-1)/2)

다음 줄에는 도로 정비 계획에 들어가 있는 도로의 수 q가 주어지고, 다음 q줄에는 a i j가 주어지는데, a가 1일때는 두 도시 i,j를 잇는 도로를 만들고, a가 2일때는 i,j를 잇는 도로를 없앤다. (1≤q≤500,1≤a≤2, 1≤i,j≤n)

두 도시 사이에 이미 도로가 있는데 또 도로를 만들거나, 도로가 없는데 없애는 불가능한 경우는 입력으로 들어오지 않는다.

수도는 1번도시이다.

출력
q줄에 각 도시별로 수도를 방문하는 데 최소 방문 도시들을 출력하시오. 만약 수도를 방문하지 못한다면 -1을 출력하시오.
'''
import sys
input = sys.stdin.readline

def bfs():                  # 너비우선 탐색
    visited = [-1] * (N+1)  
    visited[1] = 0          
    stack = [1]             # 1번 도시에서 다른 도시까지의 거리를 구한다
    while stack:
        v = stack.pop(0)
        for w in cities[v]:
            if visited[w] == -1:            # w가 미방문 도시면
                visited[w] = visited[v] + 1 # 1번 도시부터 그 전 도시 v까지의 거리에 1을 더해준다
                stack.append(w)
    print(*visited[1:])     # 1번부터 끝까지의 visited 리스트가 각 도시별 1번도시까지의 거리
    

N, M = map(int, input().split())
cities = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    cities[a].append(b)                 # 초기 도시 관계 cities 생성
    cities[b].append(a)

q = int(input())
for _ in range(q):
    q, i, j = map(int, input().split()) # 도로 계획 
    if q == 1:              # 1이면
        cities[i].append(j) # 도시간 도로 생성
        cities[j].append(i)
    else:                   # 2이면
        cities[i].remove(j) # 도시간 도로 폐쇄
        cities[j].remove(i)
    bfs()                   # 탐색
