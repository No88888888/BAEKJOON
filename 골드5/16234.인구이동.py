'''
문제
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

출력
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.
'''

# 이중 for문을 순서대로 순회하면서
# bfs를 통해 연합의 정보(연합국가의 수, 연합국가 총 인구수, 연합국가 각 좌표)를 저장하고
# 탐색이 끝난 후 저장된 정보를 이용해 인구이동을 시킨다
# 더 이상 연합이 이뤄지지 않을때까지 반복
from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    delta = [(-1,0),(0,1),(1,0),(0,-1)]
    day = 0
    flag = True     # 연합이 일어나는지 확인하는 flag값
    while flag:
        visited = [[0]*N for _ in range(N)]
        stack = {}
        cnt = -1
        for i in range(N):
            for j in range(N):
                if visited[i][j] != 1:  # 미방문한 곳이라면
                    visited[i][j] = 1   # 방문처리
                    q = deque()
                    q.append((i,j))     
                    cnt +=1
                    stack[cnt] = [1, nation[i][j], (i,j)]   # 연합정보 0번 인덱스: 연합국가 수 / 1번 인덱스: 연합국가 인구 합 / 2번 인덱스: 국가 좌표
                    while q:                                # bfs 탐색
                        x, y = q.popleft()
                        for di, dj in delta:       
                            ni, nj = x + di, y + dj
                            if 0<= ni < N and 0 <= nj < N and (L <= abs(nation[x][y] - nation[ni][nj]) <= R) and visited[ni][nj] == 0:
                                visited[ni][nj] = 1             # 방문 처리
                                q.append((ni,nj))
                                stack[cnt][0] += 1              # 연합국가 수 + 1
                                stack[cnt][1] += nation[ni][nj] # 인구수 합 +
                                stack[cnt].append((ni,nj))      # 국가 좌표 +
                                flag = False                    # 연합이 일어났다는것 표시
        if flag == False:                       # 연합 일어났으면
            for k in range(len(stack)):
                for t in range(2,len(stack[k])):
                        nation[stack[k][t][0]][stack[k][t][1]] = stack[k][1]//stack[k][0]   # stack 순회 돌면서 nation 에서 인구이동
            day +=1     # 날짜 +1
            flag = True # 다시 flag True로
        else:           # 더이상 연합 안일어났으면
            return day  # 날짜 리턴
N, L, R = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(N)]
print(bfs())

# def find_set(x,y):
#     while key[x][y] != (x,y):
#         (x,y) = key[x][y]
#     return (x,y)

# def union(x,y,p,q):
#     key[p][q] = find_set(x,y)
    
    
# N, L, R = map(int, input().split())
# nation = [list(map(int, input().split())) for _ in range(N)]
# delta = [(-1,0),(0,1),(1,0),(0,-1)]
# key = [[0]*N for _ in range(N)]
# day = 0
# for i in range(N):
#     for j in range(N):
#         key[i][j] = (i,j)

# while len(set(sum(key, []))) > 1:
#     day += 1
#     for i in range(N):
#         for j in range(N):
#             for di, dj in delta:
#                 ni, nj = i + di, j + dj
#                 if 0<= ni < N and 0 <= nj < N and L <= abs(nation[i][j] - nation[ni][nj]) <= R:
#                     if find_set(i,j) != find_set(ni,nj):
#                         union(i,j,ni,nj)
#     arr = 
#     for i in list(set(sum(key, []))):
#         sum(key, []).count(i)
        
    
#     break
#     print(key)
    
