'''
문제
NxN 크기 체스판의 특정한 위치에 하나의 나이트가 존재한다. 이때 M개의 상대편 말들의 위치 값이 주어졌을 때, 각 상대편 말을 잡기 위한 나이트의 최소 이동 수를 계산하는 프로그램을 작성하시오.
나이트는 일반적인 체스(Chess)에서와 동일하게 이동할 수 있다. 현재 나이트의 위치를 (X,Y)라고 할 때, 나이트는 다음의 8가지의 위치 중에서 하나의 위치로 이동한다.

(X-2,Y-1), (X-2,Y+1), (X-1,Y-2), (X-1,Y+2), (X+1,Y-2), (X+1,Y+2), (X+2,Y-1), (X+2,Y+1)

N=5일 때, 나이트가 (3,3)의 위치에 존재한다면 이동 가능한 위치는 다음과 같다. 나이트가 존재하는 위치는 K, 이동 가능한 위치는 노란색으로 표현하였다.



예를 들어 N=5, M=3이고, 나이트가 (2,4)의 위치에 존재한다고 가정하자. 또한 상대편 말의 위치가 차례대로 (3,2), (3,5), (4,5)라고 하자. 이때 각 상대편 말을 잡기 위한 최소 이동 수를 계산해보자. 아래 그림에서는 상대편 말의 위치를 E로 표현하였다. 단, 본 문제에서 위치 값을 나타낼 때는 (행,열)의 형태로 표현한다.



각 상대편 말을 잡기 위한 최소 이동 수는 차례대로 1, 2, 1이 된다.

입력
첫째 줄에 N과 M이 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ N ≤ 500, 1 ≤ M ≤ 1,000) 둘째 줄에 나이트의 위치 (X, Y)를 의미하는 X와 Y가 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ X, Y ≤ N) 셋째 줄부터 M개의 줄에 걸쳐 각 상대편 말의 위치 (A, B)를 의미하는 A와 B가 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ A, B ≤ N)

단, 입력으로 주어지는 모든 말들의 위치는 중복되지 않으며, 나이트가 도달할 수 있는 위치로만 주어진다.

출력
첫째 줄에 각 상대편 말을 잡기 위한 최소 이동 수를 공백을 기준으로 구분하여 출력한다.

단, 출력할 때는 입력 시에 상대편 말 정보가 주어졌던 순서에 맞게 차례대로 출력한다.
'''
# from collections import deque
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# X, Y = map(int, input().split())
# delta = (-2, 1), (-1, 2), (1, 2), (2, 1), (2,-1), (1, -2), (-1, -2), (-2, -1)
# result = []
# for _ in range(M):
#     p, q = map(int, input().split())
#     stack = deque([(X, Y)])
#     visited = [[0] * (N+1) for _ in range(N+1)]
#     flag = False
#     while stack:
#         ki, kj = stack.popleft()
#         for di, dj in delta:
#             ni, nj = ki + di, kj + dj
#             if 0 < ni <= N and 0 < nj <= N:
#                 # print(ni, nj)
#                 if ni == p and nj == q:
#                     result.append(visited[ki][kj] + 1)
#                     flag = True
#                     break
#                 stack.append((ni,nj))
#                 if not visited[ni][nj]:
#                     visited[ni][nj] = visited[ki][kj] + 1
#                 else:
#                     visited[ni][nj] = min(visited[ki][kj] + 1, visited[ni][nj])
#         if flag:
#             break
# print(*result)

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    stack = deque([(X, Y)])
    while stack:
        ki, kj = stack.popleft()                            
        for di, dj in delta:
            ni, nj = ki + di, kj + dj
            if 0 < ni <= N and 0 < nj <= N and visited[ni][nj] == -1:   # 미방문이면
                stack.append((ni,nj))                       # 저장하고
                visited[ni][nj] = visited[ki][kj] + 1       # 이전까지의 거리 + 1
    
N, M = map(int, input().split())                            # N : 차원의 크기, M : 적 말의 수
X, Y = map(int, input().split())                            # 나이트 첫 위치
enemy = [tuple(map(int, input().split())) for _ in range(M)]# 적 위치
delta = (-2, 1), (-1, 2), (1, 2), (2, 1), (2,-1), (1, -2), (-1, -2), (-2, -1)
visited = [[-1] * (N+1) for _ in range(N+1)]                # 방문 위치까지의 최소 횟수 담을 배열
visited[X][Y] = 0                                           # 첫 위치 = 0
BFS()
for i, j in enemy:                                          # visited에서
    print(visited[i][j], end=' ')                           # 적 좌표의 값을 출력한다