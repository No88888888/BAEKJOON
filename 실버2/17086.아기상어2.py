'''
문제
N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자. 

입력
첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.

출력
첫째 줄에 안전 거리의 최댓값을 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    shark = deque()
    shark.append((x,y))
    while shark:
        x, y = shark.popleft()
        for di, dj in delta:
            ni, nj = x + di, y+ dj
            if 0<= ni < N and 0 <= nj < M and not visited[ni][nj]:  # 범위 내면서 미방문
                if arr[ni][nj] == 0:                    # 0이면
                    visited[ni][nj] = visited[x][y] + 1 # 거리 표시
                    shark.append((ni,nj))               # 인큐하고 계속 탐색
                else:                                   # 상어면
                    result.append(visited[x][y])        # 지금까지 거리(안전거리) result에 넣고 탐색 종료
                    return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1))
result = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:  
            bfs(i, j)       # 0인 곳에서 bfs 탐색 시작
print(max(result))          # 전체 탐색 후 최대 안전거리 출력
                            
                    