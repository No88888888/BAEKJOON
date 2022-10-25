'''
문제
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다. 이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다. 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다. 

입력
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.

다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.

출력
첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다. 만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.
'''

'''
1. 먼저 순회를 돌면서 고슴도치, 우물, 빈공간 찾아서 0으로 만들고
		고슴도치, 우물 좌표는 따로따로 저장 해놓는다
2. 우물 좌표를 가지고 bfs돌면서 홍수를 일으킨다. 
		빈 공간, 고슴도치 위치에 물이 차는 시간을 적어 넣는다
3. 고슴도치가 bfs로 비버 집으로 출발한다. 
		고슴도치 이동 시간보다 물이 차오르는 시간이 작다면 고슴도치가 이동 가능한 곳
4. D에 도착한다면 그 때 고슴도치 이동 시간, 아니면 KAKTUS 출력 	
'''

from collections import deque
import sys
input = sys.stdin.readline

def flood():
    while well:
        x, y = well.popleft()
        for di, dj in delta:
            ni, nj = x + di, y + dj
            if 0 <= ni < R and 0 <= nj < C and str(TDDUP[ni][nj]) not in 'DX*' and TDDUP[ni][nj] == 0:
                TDDUP[ni][nj] = TDDUP[x][y] + 1
                well.append((ni, nj))
        
def bieber():
    i,j = Hedgehog[0]
    TDDUP[i][j] = 0
    while Hedgehog:
        x, y = Hedgehog.popleft()
        for di, dj in delta:
            ni, nj = x + di, y + dj
            if 0 <= ni < R and 0 <= nj < C and str(TDDUP[ni][nj]) not in 'X*':
                if TDDUP[ni][nj] == 'D':
                    print(TDDUP[x][y] + 1)
                    return
                elif TDDUP[ni][nj] == 0 or TDDUP[ni][nj] > TDDUP[x][y] + 1:
                    TDDUP[ni][nj] = TDDUP[x][y] + 1
                    Hedgehog.append((ni,nj))
    print('KAKTUS')

R, C = map(int, input().split())
TDDUP = [list(input()) for _ in range(R)]
well, Hedgehog = deque(), deque()
for i in range(R):
    for j in range(C):
        if TDDUP[i][j] in '.*S':
            if TDDUP[i][j] == '*':
                well.append((i,j))
            elif TDDUP[i][j] == 'S':
                Hedgehog.append((i, j))
            TDDUP[i][j] = 0
delta = ((-1,0), (0,1), (1,0), (0,-1))
flood()
bieber()


# 물을 먼저 다 채운다
# 채울때 bfs로 각 칸별로 물이 차게되는 시간을 적는다
# 그 후 고슴도치 이동
# 이동하면서 시간 +1
# 이때 고슴도치의 시간이 해당 칸의 시간보다 작아야 이동
# 크면 이동 X
# 이동 중 비버의 굴 도착하면 그떄의 시간 저장
# 더이상 이동못하면 break
# from collections import deque
# import sys
# input = sys.stdin.readline

# def well():
#     while water:
#         i, j = water.pop()
#         TDDUP[i][j] = 0
#         q = deque()
#         q.append((i,j))
        
#         while q:
#             x, y = q.popleft()
#             for di, dj in delta:
#                 ni, nj = x + di, y + dj
#                 if 0 <= ni < R and 0 <= nj < C and str(TDDUP[ni][nj]) not in 'DX*' and (TDDUP[ni][nj] == 0 or TDDUP[ni][nj] > TDDUP[x][y] + 1):
#                     TDDUP[ni][nj] = TDDUP[x][y] + 1
#                     q.append((ni, nj))
#         TDDUP[i][j] = '*'
        
# def bieber():    
#     TDDUP[Hedgehog[0]][Hedgehog[1]] = 0
#     stack = deque()
#     stack.append(Hedgehog)
#     while stack:
#         x, y = stack.popleft()
#         for di, dj in delta:
#             ni, nj = x + di, y + dj
#             if 0 <= ni < R and 0 <= nj < C and TDDUP[ni][nj] != 0 and str(TDDUP[ni][nj]) not in 'X*':
#                 if TDDUP[ni][nj] == 'D':
#                     print(TDDUP[x][y] + 1)
#                     return
#                 elif TDDUP[ni][nj] > TDDUP[x][y] + 1:
#                     TDDUP[ni][nj] = TDDUP[x][y] + 1
#                     stack.append((ni,nj))
#     print('KAKTUS')


# R, C = map(int, input().split())
# TDDUP = [list(input()) for _ in range(R)]
# print(TDDUP)
# water = []
# for i in range(R):
#     for j in range(C):
#         if TDDUP[i][j] == '.':
#             TDDUP[i][j] = 0
#         elif TDDUP[i][j] == '*':
#             water.append((i,j))
#         elif TDDUP[i][j] == 'S':
#             TDDUP[i][j] = 0
#             Hedgehog = (i,j)
# print(TDDUP)
# delta = ((-1,0), (0,1), (1,0), (0,-1))
# well()
# print(TDDUP)
# bieber()
# print(TDDUP)



# from collections import deque
# import sys
# input = sys.stdin.readline

# def well():
#     while water:
#         i, j = water.pop()
#         TDDUP[i][j] = 0
#         q = deque()
#         q.append((i,j))
#         while q:
#             x, y = q.popleft()
#             for di, dj in delta:
#                 ni, nj = x + di, y + dj
#                 if 0 <= ni < R and 0 <= nj < C and str(TDDUP[ni][nj]) not in 'DX*' and (TDDUP[ni][nj] == 0 or TDDUP[ni][nj] > TDDUP[x][y] + 1):
#                     TDDUP[ni][nj] = TDDUP[x][y] + 1
#                     q.append((ni, nj))
#         TDDUP[i][j] = '*'
        
# def bieber():
#     i, j = Hedgehog    
#     TDDUP[i][j] = 0
#     q = deque()
#     q.append((i,j))
#     while q:
#         x, y = q.popleft()
#         for di, dj in delta:
#             ni, nj = x + di, y + dj
#             if 0 <= ni < R and 0 <= nj < C and str(TDDUP[ni][nj]) not in 'X*':
#                 if TDDUP[ni][nj] == 'D':
#                     print(TDDUP[x][y] + 1)
#                     return
#                 elif TDDUP[ni][nj] == 0 or TDDUP[ni][nj] > TDDUP[x][y] + 1:
#                     TDDUP[ni][nj] = TDDUP[x][y] + 1
#                     q.append((ni,nj))
#     print('KAKTUS')

# R, C = map(int, input().split())
# TDDUP = [list(input()) for _ in range(R)]
# water = []
# for i in range(R):
#     for j in range(C):
#         if TDDUP[i][j] == '.':
#             TDDUP[i][j] = 0
#         elif TDDUP[i][j] == '*':
#             water.append((i,j))
#         elif TDDUP[i][j] == 'S':
#             TDDUP[i][j] = 0
#             Hedgehog = (i,j)
# delta = ((-1,0), (0,1), (1,0), (0,-1))
# result = []
# well()
# bieber()

