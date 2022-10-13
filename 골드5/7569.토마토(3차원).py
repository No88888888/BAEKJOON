'''
문제
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.



창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    delta = [(0,-1,0),(0,0,1),(0,1,0),(0,0,-1),(1,0,0),(-1,0,0)] # 앞뒤좌우 위아래
    global day, tomato
    while tomato:                       
        new_tomato = deque()            # 날마다 새로 익은 토마토 좌표를 저장할 변수
        for _ in range(len(tomato)):    # 익은 토마토 자리에서 탐색
            h, i, j = tomato.popleft()
            for dh, di, dj in delta:    # 높이, 가로, 세로
                nh, ni,nj = h + dh, i + di, j + dj
                if 0 <= nh < H and 0<= ni < N and 0 <= nj < M and box[nh][ni][nj] == 0: # 범위 내고 안익은 토마토라면
                    box[nh][ni][nj] = 1             # 익히고
                    new_tomato.append((nh,ni,nj))   # 해당 좌표 저장
        tomato = new_tomato     # 새로익은 토마토 자리에서만 탐색하기 위해
        day += 1                # 날짜 +1
    if i in sum(sum(box,[]),[]):    # 익을 수 있는 토마토가 다 익은 후 아직 안익은 토마토가 있다면
        if i == 0:
            day = -1                        # -1

M,N,H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
day = -1    # 토마토가 다 익고 나서도 한번 더 확인한 후 day + 1하기 때문에 -1로 초기값 설정 
tomato = deque()
for k in range(H):
    for i in range(N):  
        for j in range(M):
            if box[k][i][j] == 1:
                tomato.append((k,i,j))  # 익은 토마토의 좌표를 저장

bfs()
print(day)


# from collections import deque
# import copy
# import sys
# input = sys.stdin.readline
# def bfs():
#     delta = [[0,-1,0],[0,0,1],[0,1,0],[0,0,-1],[1,0,0],[-1,0,0]]

#     global day, apple
#     while apple:
#         new_apple = []
#         for _ in range(len(apple)):
#             Q = apple.pop(0)
#             h, i, j = Q[0], Q[1], Q[2]
#             for dh, di, dj in delta:
#                 nh, ni,nj = h + dh, i + di, j + dj
#                 if 0 <= nh < H and 0<= ni < N and 0 <= nj < M and tmt[nh][ni][nj] == 0:
#                     tmt[nh][ni][nj] = 1
#                     new_apple.append((nh,ni,nj))
#         apple = new_apple
#         day += 1
#     if sum(sum(tmt,[]),[]).count(0):
#         day = -1

# M,N,H = map(int, input().split())
# tmt = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# apple = []
# for k in range(H):
#     for i in range(N):  
#         for j in range(M):
#             if tmt[k][i][j] == 1:
#                 apple.append((k,i,j))
                
# day = 0
# bfs()
# print(day)




# import sys
# input = sys.stdin.readline
# def bfs():
#     delta = [[0,-1,0],[0,0,1],[0,1,0],[0,0,-1],[1,0,0],[-1,0,0]]
#     flag= True
#     global day, visited
#     while flag:
#         for k in range(H):
#             for i in range(N):
#                 for j in range(M):
#                     if visited[k][i][j] == day + 1 and tmt[k][i][j] == 1:
#                         # visited[i][j] = 1
#                         for dh, di, dj in delta:
#                             nh, ni,nj = k + dh, i + di, j + dj
#                             if 0 <= nh < H and 0<= ni < N and 0 <= nj < M and visited[nh][ni][nj] == 0 and tmt[nh][ni][nj] == 0:
#                                 tmt[nh][ni][nj] = 1
#                                 visited[nh][ni][nj] = visited[k][i][j] + 1
#                                 flag = False
#         if flag == False:
#             flag = True
#         else:
#             if sum(tmt,[]).count(0):
#                 day = -1
#                 break
#         day += 1
# M,N,H = map(int, input().split())
# tmt = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# visited = [[[0]*M for _ in range(N)] for _ in range(H)]
# for k in range(H):
#     for i in range(N):  
#         for j in range(M):
#             if tmt[k][i][j] == 1:
#                 visited[k][i][j] = 1
# day = 0
# bfs()
# print(day)

# def bfs():
#     delta = [[-1,0],[0,1],[1,0],[0,-1],[N,0],[-1*N,0]]
#     flag= True
#     global day
#     while flag:
#         visited = [[0]*M for _ in range(N*H)]
#         for i in range(N*H):
#             for j in range(M):
#                 if visited[i][j] == 0 and tmt[i][j] == 1:
#                     visited[i][j] = 1
#                     for di, dj in delta:
#                         ni,nj = i + di, j + dj
#                         if 0<= ni < N*H and 0 <= nj < M and visited[ni][nj] == 0 and tmt[ni][nj] == 0:
#                             tmt[ni][nj] = 1
#                             visited[ni][nj] = 1
#                             flag = False
#         if flag == False:
#             flag = True
#         else:
#             if sum(tmt,[]).count(0):
#                 day = -1
#                 break
#         day += 1
    


# M,N,H = map(int, input().split())
# tmt = [list(map(int, input().split())) for _ in range(N*H)]
# day = 0
# bfs()
# print(day)