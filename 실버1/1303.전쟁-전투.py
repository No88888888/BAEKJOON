'''
문제
전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

입력
첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

출력
첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(clr, *po):                  # 해당위치에서 BFS탐색
    global visited
    delta = ((-1,0), (0,1), (1,0), (0,-1))
    visited[i][j] = 1               # 방문 표시
    q = deque()
    q.append((po[0],po[1]))                                
    cnt = 1                         # 팀원 카운트
    while q:
        x,y = q.popleft()
        for di, dj in delta:        # 4방탐색
            ni, nj = x + di, y +dj
            if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and battlefield[ni][nj] == clr: # 주변에 팀원 있으면
                visited[ni][nj] = 1 # 방문 표시
                q.append((ni,nj))   # 인큐
                cnt += 1            # 팀원 + 1
    return cnt ** 2                 # 해당 무리의 힘 리턴

N, M = map(int, input().split())
battlefield = [list(input()) for _ in range(M)]
W_power, B_power  = 0, 0
visited = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:              # 미방문이고
            if battlefield[i][j] == 'W':    # W면
                W_power += bfs('W', i, j)   # 해당 무리 힘을 W_power에 더함
            else:                           # B면
                B_power += bfs('B', i, j)   # 해당 무리 힘을 B_power에 더함
print(W_power, B_power)