'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adjlist = [[] for _ in range(N+1)]

for _ in range(M):                      # 간선정보 저장
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
    
visited = [0]*(N+1)
cnt = 0

for i in range(1, N+1):
    if not adjlist[i]:                  # 간선이 없다면 혼자 단독 
        cnt += 1
    if adjlist[i] and not visited[i]:   # 간선이 있다면
        stack = [i]
        cnt += 1
        while stack:                    # 이어진 노드들을 찾기 위한 dfs탐색
            v = stack.pop()
            for w in adjlist[v]:
                if not visited[w]:
                    visited[w] = 1
                    stack.append(w)
print(cnt)                              # 총 연결 요소 출력