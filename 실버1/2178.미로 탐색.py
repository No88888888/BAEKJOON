'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''
def bfs(stx, sty):  # bfs 탐색
    global visited
    q = []
    q.append([stx,sty])
    visited[stx][sty] = 1
    di = [-1, 0, 1, 0] 
    dj = [0, 1, 0, -1] # 상우하좌

    while True:
        v = q.pop(0)
        for i in range(4):
            ni = v[0] + di[i]
            nj = v[1] + dj[i]
            if 0<=ni<=N and 0<=nj<=M and maze[ni][nj] == 1 and visited[ni][nj] == 0: # 범위 내면
                q.append([ni, nj])                          # 인큐
                visited[ni][nj] = visited[v[0]][v[1]] + 1   # 출발지로부터의 거리를 저장
                if ni == N and nj == M:                         # 도착지면
                    return visited[ni][nj]                      # 출발지에서 도착지까지의 거리 반환

N, M = map(int, input().split())
maze = [[0]*(M+2)] + [[0]+list(map(int, input()))+[0] for _ in range(N)] + [[0]*(M+2)]  # 상하좌우 0으로 패딩
visited = [[0]*(M+2) for _ in range(N+2)]
for i in range(N+2):
    for j in range(M+2):
        if maze[i][j] == 0:
            visited[i][j] = 1       # maze의 길 말고는 전부 1로 변환
stx,sty = 1, 1                      # 출발 좌표

print(bfs(stx,sty))

#-----------------------------------------------

import numpy as np                  

def bfs(stx, sty):
    global visited
    q = []
    q.append([stx,sty])
    visited[stx][sty] = 1
    di = [-1, 0, 1, 0] 
    dj = [0, 1, 0, -1] 
    
    while True:
        v = q.pop(0)
        for i in range(4):
            ni = v[0] + di[i]
            nj = v[1] + dj[i]
            if 0<=ni<=N and 0<=nj<=M and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = visited[v[0]][v[1]] + 1
            if ni == N and nj == M:
                return visited[ni][nj]

N, M = map(int, input().split())
o = [list(map(int, input())) for _ in range(N)]
maze = np.pad(o,[(1,1),(1,1)], mode='constant') # numpy 사용한 패딩(numpy 외부모듈 이유로 사용불가)
visited = [[0]*(M+2) for _ in range(N+2)]
for i in range(N+2):
    for j in range(M+2):
        if maze[i][j] == 0:
            visited[i][j] = 1
stx,sty = 1, 1

print(bfs(stx,sty))