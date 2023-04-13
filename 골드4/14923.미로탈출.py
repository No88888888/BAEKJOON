'''
문제
홍익이는 사악한 마법사의 꾐에 속아 N x M 미로 (Hx, Hy) 위치에 떨어졌다. 다행히도 홍익이는 마법사가 만든 미로의 탈출 위치(Ex, Ey)를 알고 있다. 하지만 미로에는 곳곳에 마법사가 설치한 벽이 있어 홍익이가 탈출하기 어렵게 하고 있다.

홍익이는 마법사의 연구실에서 훔친 지팡이가 있어, 벽을 길로 만들 수 있다. 그렇지만, 안타깝게도 마법의 지팡이는 단 한 번만 사용할 수 있다.

이때, 홍익이를 도와 미로에서 탈출할 수 있는지 알아보고, 할 수 있다면 가장 빠른 경로의 거리 D는 얼마인지 알아보자.

인접한 칸으로 이동하는데 똑같은 시간이 들고, 벽을 부수는 데 시간이 걸리지 않는다.

입력
N M
Hx Hy
Ex Ey
N X M 행렬
2 ≤ N ≤ 1000, 2 ≤ M ≤ 1000
1 ≤ Hx, Hy, Ex, Ey ≤ 1000
(Hx, Hy)≠ (Ex, Ey)
행렬은 0과 1로만 이루어져 있고, 0이 빈 칸, 1이 벽이다.
출력
D (탈출 할 수 없다면, -1을 출력한다.)
'''
from collections import deque
import sys
input = sys.stdin.readline

def exodus():
    delta = (-1,0), (0,1), (1,0), (0,-1)
    stack = deque([(Hx, Hy, 1)])
    while stack:
        x, y, magic = stack.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] == 1:                               # 벽이라면
                    if magic == 1 and visited[nx][ny][1] == 0:      # 마법 안썼고 마법써서 방문한 곳이 아니라면
                        visited[nx][ny][1] = visited[x][y][0] + 1   # 마법써서 도착했을 때 거리를 1 더함
                        stack.append((nx, ny, 0))                   # 마법 쓴 상태로 인 스택
                elif miro[nx][ny] == 0:                             # 벽 아니라면
                    if magic == 1 and visited[nx][ny][0] == 0:      # 마법을 안썼고 마법 안썼을 떄 방문한 곳이 아니라면
                        visited[nx][ny][0] = visited[x][y][0] + 1   # 마법 안쓰고 방문했을 떄 거리 1 더함
                        stack.append((nx,ny, magic))                # 마법 안 쓴 상대로 인스택
                    elif magic == 0 and visited[nx][ny][1] == 0:    # 마법 쓴 상태고 마법 쓰고 방문한 곳이 아니라면
                        visited[nx][ny][1] = visited[x][y][1] + 1   # 마법 써서 방문한 거리 1 더함
                        stack.append((nx,ny,magic))                 # 마법 쓴 상태로 인스택
N, M = map(int, input().split())
Hx, Hy = map(int, input().split())      # 출발 좌표
Hx -= 1                                 # 인덱스 맞추기
Hy -= 1
Ex, Ey = map(int, input().split())      # 도착위치
Ex -= 1                                 # 인덱스 맞추기
Ey -= 1
miro = [list(map(int, input().split())) for _ in range(N)]  # 미로

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]    # 3차원 visited(0번인덱스=마법 안쓰고 해당 좌표왔을때 거리,1번인덱스=마법 쓰고 해당 좌표 왔을 떄 거리)
visited[Hx][Hy] = [1,1]                 # 출발 좌표 방문 표시
exodus()

if visited[Ex][Ey] == [0,0]:                                # 도착지점 방문 못했으면
    print(-1)                                               # -1 출력
else:                                                       # 방문했다면
    if visited[Ex][Ey][0] * visited[Ex][Ey][1] == 0:        # 벽을 뚫고 갔을때나 안뚫고 갔을때 둘 중 하나만 도착했다면
        print(max(visited[Ex][Ey])-1)                       # 가능했던 경우의 거리를 출력
    else:                                                   # 둘다 도착 가능했다면
        print(min(visited[Ex][Ey])-1)                       # 둘 중 최소 거리 출력