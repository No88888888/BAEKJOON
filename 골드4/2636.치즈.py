'''
문제
아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다. 판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다. <그림 1>의 경우, 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어져서 <그림 2>와 같이 된다.



<그림 1> 원래 치즈 모양

다시 한 시간 후에는 <그림 2>에서 ‘c’로 표시된 부분이 녹아 없어져서 <그림 3>과 같이 된다.



<그림 2> 한 시간 후의 치즈 모양



<그림 3> 두 시간 후의 치즈 모양

<그림 3>은 원래 치즈의 두 시간 후 모양을 나타내고 있으며, 남은 조각들은 한 시간이 더 지나면 모두 녹아 없어진다. 그러므로 처음 치즈가 모두 녹아 없어지는 데는 세 시간이 걸린다. <그림 3>과 같이 치즈가 녹는 과정에서 여러 조각으로 나누어 질 수도 있다.

입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.
'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global cheeze, result, hour
    delta = [(-1,0), (0,1), (1,0), (0,-1)]
    while cheeze:                           # 치즈가 다 녹을동안
        visited = [[0]*M for _ in range(N)]
        visited[0][0] = 1
        q = deque()
        q.append((0,0))                     # (0,0)은 무조건 외부 공기이기 때문에
        del_cheeze = []                     # 해당 시간에 없어질 치즈
        while q:                            # bfs로 외부 공기 탐색
            i, j = q.popleft()
            for di, dj in delta:            # 상하좌우 탐색해서
                ni, nj = i + di, j + dj     
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0: # 범위 내, no방문 시 
                    visited[ni][nj] = 1     # 일단 방문 처리
                    if arr[ni][nj] == 0:    # 0이라면 외부공기
                        q.append((ni,nj))   # 인큐
                    else:                   # 1이라면 외부공기와 맞닿아있는 치즈
                        del_cheeze.append((ni,nj))  # 녹아 없어질 치즈 리스트에 넣어줌
                    
        for x, y in del_cheeze:             
            arr[x][y] = 0           # arr에서 이번 타임 녹을 치즈 녹여주고
            cheeze.remove((x,y))    # 최초 치즈 리스트에서 없애줌
        hour += 1                   # 시간 + 1
        result.append(len(cheeze))  # 없어진 후 남은 치즈의 양을 result에 저장
            

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheeze = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheeze.append((i,j))    # 치즈위치만 cheeze에 저장
result = [len(cheeze)]              # 시간당 남은 치즈 리스트
hour = 0
bfs()
print(hour)
print(result[-2])

# import time
# def dfs():
#     delta = [(-1,0), (0,1), (1,0), (0,-1)]
#     global cheeze, cheeze2, rest_cheeze
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if cheeze[i][j] == 1:
#                 cnt += 1
#                 for di, dj in delta:
#                     ni, nj = i + di, j + dj
#                     if cheeze2[ni][nj] == -1:
#                         cheeze[i][j] = 0
            
#     rest_cheeze.append(cnt)
#     return cheeze
                


# def bfs():
#     delta = [(-1,0), (0,1), (1,0), (0,-1)]
#     global hour, cheeze, cheeze2
#     while set(sum(cheeze, [])) != {0}:
#         # if hour == 2:
#         #     print(cheeze2)
#         #     return
#         for i in range(N):
#             for j in range(M):
#                 q= []
#                 if cheeze[i][j] == 0:
#                     q.append((i,j))
#                     while q:
#                         i, j = q.pop(0)
#                     for di, dj in delta:
#                         ni, nj = i + di, j + dj
#                         if ni < 0 or ni > N-1 or nj < 0 or nj > M-1:
#                             cheeze2[i][j] = -1
                            
#                         elif cheeze[ni][nj] == 0:
#                             q.append((ni,nj))
#                             if cheeze2[i][j] == -1:
#                                 cheeze2[ni][nj] == -1
                                
#                             while cheeze[ni][nj] == 0:
#                                 q.append((ni,nj))
#                                 ni += di
#                                 nj += dj
#                                 if ni < 0 or ni > N-1 or nj < 0 or nj > M-1:
#                                     cheeze2[i][j] = -1
#                                     break
#         dfs()                        
#         hour += 1
# N, M = map(int, input().split())

# cheeze = [list(map(int, input().split())) for _ in range(N)]
# cheeze2 = [[0]*M for _ in range(N)]
# hour = 0
# rest_cheeze = []
# bfs()
# print(hour)
# print(rest_cheeze)


# def bfs():
#     global cheeze, cheeze2, hour, result, arr
#     delta = [(-1,0), (0,1), (1,0), (0,-1)]
#     while cheeze:
#         # print(cheeze)
#         for i,j in cheeze:
#             print((i,j))
#             for di, dj in delta:
#                 ni, nj = i + di, j + dj
#                 if arr[ni][nj] == 0:
#                     while arr[ni][nj] == 0:
#                         ni += di
#                         nj += dj
#                         if ni < 0 or ni > N-1 or nj < 0 or nj > M-1:
#                             print(cheeze2)
#                             cheeze2.append((i,j))
#                             break
#         for x, y in cheeze2:
#             arr[x][y] = 0
#             cheeze.remove((x,y))
#         hour += 1
#         result.append(len(cheeze))

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# cheeze, cheeze2 = [], []
# result = []
# hour = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             cheeze.append((i,j))
# bfs()
# print(hour)
# print(result)


# def bfs():
#     global cheeze, cheeze2, hour, result, arr
#     delta = [(-1,0), (0,1), (1,0), (0,-1)]
    
#     visited = [[0]*M for _ in range(N)]
#     visited[0][0] = 1
#     while cheeze:
#         q = [(0,0)]
#         top = -1
#         while top < len(q):
#             top += 1
#             i, j = q[top]
#             for di, dj in delta:
#                 ni, nj = i + di, j + dj
#                 if 0 <= ni < N
#                 and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
#                     visited[ni][nj] = 1
#                     arr[ni][nj] = -1
#                     q.append((ni,nj))

#         for x, y in cheeze:
#             for di, dj in delta:
#                 ni, nj = x + di, y + dj
#                 if arr[ni][nj] == -1:
#                     arr[x][y] = -1
            
            

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# cheeze, cheeze2 = [], []
# result = []
# hour = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             cheeze.append((i,j))
# bfs()
# print(hour)
# print(result)


