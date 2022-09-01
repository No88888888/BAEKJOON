'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''
# def dfs(v, N):
#     top = -1
#     visited[v] = 1
#     while True:
#         for w in adjList[v]:        # v위치에서 w가
#             if visited[w] == 0:     # 방문하지 않았다면
#                 top += 1            # top 포인터 +1
#                 stack[top] = v      # stack 최상위에 v 저장
#                 v = w               # w로 v 변환
#                 visited[w] = 1      # 새 방문지 w도 1로 방문 표시
#                 break
#             if w == N:              # 새 방문지가 N, 목적지라면
#                 return 1            # 1 반환
#         else:                       # v에서 방문할 w가 없거나 다 방문 했다면
#             if top != -1:           # top이 -1이 아니면
#                 v = stack[top]      # stack[top]을 이전 정점인 v로 돌리고
#                 top -=1             # top -=1
#             else:                   # top이 -1이라면 출발지 돌아옴
#                 return 0 
def dfs(v):                 # 재귀 dfs
    visited[v] = 1
    print(v, end=' ')       
    for i in adjList[v]:
        if visited[i] == 0:
            dfs(i)
            

def bfs(v):                 # bfs
    visited = [0] * (N+1)
    visited[v] = 1
    q = []
    q.append(v)
    while q:
        v = q.pop(0)
        print(v, end=' ') 
        for i in adjList[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
   

N, M, V = map(int, input().split())
adjList = [[] for _ in range(N+1)]
for i in range(M):                  # graph
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
    
for i in adjList:                   # 정렬
    i.sort()
    
visited = [0] * (N+1)
dfs(V)
print()
bfs(V)

