'''
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''

        
from collections import deque
import sys
input = sys.stdin.readline

def exodus():
    delta = (-1,0), (0,1), (1,0), (0,-1)
    stack = deque([(0, 0, 1)])
    while stack:
        x, y, magic = stack.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] == '1':                             # 벽이라면
                    if magic == 1 and visited[nx][ny][1] == 0:      # 마법 안썼고 마법써서 방문한 곳이 아니라면
                        visited[nx][ny][1] = visited[x][y][0] + 1   # 마법써서 도착했을 때 거리를 1 더함
                        stack.append((nx, ny, 0))                   # 마법 쓴 상태로 인 스택
                elif miro[nx][ny] == '0':                           # 벽 아니라면
                    if magic == 1 and visited[nx][ny][0] == 0:      # 마법을 안썼고 마법 안썼을 떄 방문한 곳이 아니라면
                        visited[nx][ny][0] = visited[x][y][0] + 1   # 마법 안쓰고 방문했을 떄 거리 1 더함
                        stack.append((nx,ny, magic))                # 마법 안 쓴 상대로 인스택
                    elif magic == 0 and visited[nx][ny][1] == 0:    # 마법 쓴 상태고 마법 쓰고 방문한 곳이 아니라면
                        visited[nx][ny][1] = visited[x][y][1] + 1   # 마법 써서 방문한 거리 1 더함
                        stack.append((nx,ny,magic))                 # 마법 쓴 상태로 인스택
                        
N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)] # 미로

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]    # 3차원 visited(0번인덱스=마법 안쓰고 해당 좌표왔을때 거리,1번인덱스=마법 쓰고 해당 좌표 왔을 떄 거리)
visited[0][0] = [1,1]                                       # 출발 좌표 방문 표시
exodus()

if visited[N-1][M-1] == [0,0]:                              # 도착지점 방문 못했으면
    print(-1)                                               # -1 출력
else:                                                       # 방문했다면
    if visited[N-1][M-1][0] * visited[N-1][M-1][1] == 0:    # 벽을 뚫고 갔을때나 안뚫고 갔을때 둘 중 하나만 도착했다면
        print(max(visited[N-1][M-1]))                       # 가능했던 경우의 거리를 출력
    else:                                                   # 둘다 도착 가능했다면
        print(min(visited[N-1][M-1]))                       # 둘 중 최소 거리 출력