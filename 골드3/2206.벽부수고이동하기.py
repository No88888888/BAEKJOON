'''

'''

import sys
input = sys.stdin.readline
from collections import deque
def bfs(x, y):
    q = deque()
    q.append((x, y, 1)) # x, y, 남은 스킬 사용횟수
    visited[x][y] = [1,1]
    while q:
        x, y, skill= q.popleft()
        for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0:
                if arr[nx][ny] == '1': # 벽을 만났을 때
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

N, M =map(int, input().split())

arr = [list(input()) for _ in range(N)]

visited = [[[0,0] for i in range(M)] for _ in range(N)]

bfs(0,0)

ans = visited[N-1][M-1]
if sum(ans) == 0:
    print(-1)
else:
    if ans[0] * ans[1] == 0:
        print(max(ans))
    else:
        print(min(ans))