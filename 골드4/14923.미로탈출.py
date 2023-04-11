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
# def exodus():
#     delta = (-1,0), (0,1), (1,0), (0,-1)
#     stack = [(Hx, Hy, 1)]
#     visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
#     visited[Hx][Hy] = [0,-1]
#     while stack:
#         x, y, magic = stack.pop(0)
#         if x == Ex and y == Ey:
#             return visited[x][y][0] 
#         for dx, dy in delta:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 if miro[nx][ny] == 1:
#                     if magic == 1 and visited[nx][ny][1] == -1:
#                         stack.append((nx, ny, 0))
#                         visited[nx][ny][1] = visited[x][y][0] + 1
#                 elif miro[nx][ny] == 0:
#                     if magic == 1 and visited[nx][ny][0] == -1:
#                         stack.append((nx,ny, magic))
#                         visited[nx][ny][0] = visited[x][y][0] + 1
#                     elif magic == 0 and visited[nx][ny][1] == -1:
#                         stack.append((nx,ny,magic))
#                         visited[nx][ny][1] = visited[x][y][1] + 1
#                 print(nx, ny)
#     return -1
# N, M = map(int, input().split())
# Hx, Hy = map(int, input().split())
# Hx -= 1
# Hy -= 1
# Ex, Ey = map(int, input().split())
# Ex -= 1
# Ey -= 1
# miro = [list(map(int, input().split())) for _ in range(N)]
# print('----------------------')
# print(exodus())



def bfs(x, y):
    q = []
    q.append((x, y, 1)) # x, y, 남은 스킬 사용횟수
    visited[x][y] = [1,1]
    while q:
        x, y, skill= q.pop(0)
        for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0:
                if arr[nx][ny] == 1: # 벽을 만났을 때
                    if visited[nx][ny][1] == 0 and skill == 1: 
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        q.append((nx, ny, 0))
                else: # 벽이 아닐때
                    if skill == 0 and visited[nx][ny][1] == 0:
                        visited[nx][ny][1] = visited[x][y][1] + 1
                        q.append((nx, ny, 0))
                    elif skill == 1 and visited[nx][ny][0] == 0:
                        visited[nx][ny][0] = visited[x][y][0] + 1
                        q.append((nx, ny, 1))
            print(visited)



N, M =map(int, input().split())
hx, hy = map(int, input().split())
hx -= 1
hy -= 1
ex, ey = map(int, input().split())
ex -= 1
ey -= 1

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [[[0,0] for i in range(M)] for _ in range(N)]

bfs(hx, hy)

ans = visited[ex][ey]
if sum(ans) == 0:
    print(-1)
else:
    if ans[0] * ans[1] == 0:
        print(max(ans) - 1)
    else:
        print(min(ans) - 1)