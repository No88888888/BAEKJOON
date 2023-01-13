'''
문제
미키의 뒷마당에는 특정 수의 양이 있다. 그가 푹 잠든 사이에 배고픈 늑대는 마당에 들어와 양을 공격했다.

마당은 행과 열로 이루어진 직사각형 모양이다. 글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.

한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면, 두 칸은 같은 영역 안에 속해 있다고 한다. 마당에서 "탈출"할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주한다.

다행히 우리의 양은 늑대에게 싸움을 걸 수 있고 영역 안의 양의 수가 늑대의 수보다 많다면 이기고, 늑대를 우리에서 쫓아낸다. 그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.

맨 처음 모든 양과 늑대는 마당 안 영역에 존재한다.

아침이 도달했을 때 살아남은 양과 늑대의 수를 출력하는 프로그램을 작성하라.

입력
첫 줄에는 두 정수 R과 C가 주어지며(3 ≤ R, C ≤ 250), 각 수는 마당의 행과 열의 수를 의미한다.

다음 R개의 줄은 C개의 글자를 가진다. 이들은 마당의 구조(울타리, 양, 늑대의 위치)를 의미한다.

출력
하나의 줄에 아침까지 살아있는 양과 늑대의 수를 의미하는 두 정수를 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
field = [list(input()) for _ in range(N)]
delta = (-1,0), (0,1), (1,0), (0,-1)
visited = [[0]* M for _ in range(N)]
sheep, wolf = 0, 0                                      # 최종 양, 늑대 수

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and field[i][j] != '#':   #미방문이고 울타리가 아니라면
            temp_sheep, temp_wolf = 0, 0                # 영역마다의 양, 늑대 수
            stack = deque()
            stack.append((i,j))
            visited[i][j] = 1
            while stack:                                # 영역 탐색
                x, y = stack.popleft()                  
                if field[x][y] == 'o':                  # 해당 칸이 양이면
                    temp_sheep += 1                     # 영역 양 수 + 1
                elif field[x][y] == 'v':                # 해당 칸이 늑대면
                    temp_wolf += 1                      # 영역 늑대 수 + 1
                for di, dj in delta:                    # 4방 탐색
                    ni, nj = x + di, y + dj
                    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and field[ni][nj] != '#':   # 필드 내, 미방문, 울타리 아니면
                        stack.append((ni,nj))           # 인스택
                        visited[ni][nj] = 1             # 방문 처리
            if temp_sheep > temp_wolf:                  # 해당 영역 내 양이 늑대보다 많으면
                sheep += temp_sheep                     # 생존 양 수 +
            else:                                       # 늑대가 양보다 많거나 같으면
                wolf += temp_wolf                       # 생존 늑대 수 +
            
print(sheep, wolf)  # 최종 양, 늑대 수 츨력

# 이왜틀????????
# N, M = map(int, input().split())
# field = [list(input()) for _ in range(N)]
# delta = (-1,0), (0,1), (1,0), (0,-1)
# visited = [[0]* M for _ in range(N)]
# sheep, wolf = 0, 0

# for i in range(N):
#     for j in range(M):
#         if visited[i][j] == 0 and field[i][j] != '#':
#             temp_sheep, temp_wolf = 0, 0
#             if field[i][j] == 'o':
#                 temp_sheep += 1
#             elif field[i][j] == 'v':
#                 temp_wolf += 1
#             stack = [(i, j)]
#             visited[i][j] = 1
#             while stack:
#                 x, y = stack.pop(0)
#                 for di, dj in delta:
#                     ni, nj = x + di, y + dj
#                     if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and field[ni][nj] != '#':
#                         if field[ni][nj] == 'o':
#                             temp_sheep += 1
#                         elif field[ni][nj] == 'v':
#                             temp_wolf += 1
#                         stack.append((ni,nj))
#                         visited[ni][nj] = 1
#             if temp_sheep > temp_wolf: 
#                 sheep += temp_sheep
#             else:
#                 wolf += temp_wolf
            
# print(sheep, wolf)


# N, M = map(int, input().split())
# field = [list(input()) for _ in range(N)]
# delta = (-1,0), (0,1), (1,0), (0,-1)
# visited = [[0]* M for _ in range(N)]
# sheep, wolf = 0, 0

# for i in range(N):
#     for j in range(M):
#         if visited[i][j] == 0 and field[i][j] in '.ov':
#             temp_sheep, temp_wolf = 0, 0
#             if field[i][j] == 'o':
#                 temp_sheep += 1
#             elif field[i][j] == 'v':
#                 temp_wolf += 1
#             stack = [(i, j)]
#             visited[i][j] = 1
#             stop = False
#             while stack:
#                 i, j = stack.pop()
#                 for di, dj in delta:
#                     ni, nj = i + di, j + dj
#                     if not 0 <= ni < N and 0 <= nj < M:
#                         stop = True
#                     if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and field[ni][nj] in '.ov':
#                         if field[ni][nj] == 'o':
#                             temp_sheep += 1
#                         elif field[ni][nj] == 'v':
#                             temp_wolf += 1
#                         stack.append((ni,nj))
#                         visited[ni][nj] = 1
#             if stop:
#                 break
#             if temp_wolf >= temp_sheep:
#                 wolf += temp_wolf
#             else:
#                 sheep += temp_sheep
            
# print(sheep, wolf)







