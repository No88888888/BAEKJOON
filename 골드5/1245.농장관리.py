'''
문제
농부 민식이가 관리하는 농장은 N×M 격자로 이루어져 있다. 민식이는 농장을 관리하기 위해 산봉우리마다 경비원를 배치하려 한다. 이를 위해 농장에 산봉우리가 총 몇 개 있는지를 세는 것이 문제다.

산봉우리의 정의는 다음과 같다. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다. (여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이 모두 1 이하일 경우로 정의된다.) 또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.

문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.

입력
첫째 줄에 정수 N(1 < N ≤ 100), M(1 < M ≤ 70)이 주어진다. 둘째 줄부터 N+1번째 줄까지 각 줄마다 격자의 높이를 의미하는 M개의 정수가 입력된다. 격자의 높이는 500보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 산봉우리의 개수를 출력한다.
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
mt = [list(map(int, input().split())) for _ in range(N)]
delta = (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)
visited = [[0] * M for _ in range(N)]
cnt = 0

def bfs(i, j):
    global cnt
    stack = [(i, j)]
    flag = True
    
    while stack:            
        i, j = stack.pop()
        visited[i][j] = 1
        for di, dj in delta:        # 8방면 탐색
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M: # 범위내면서
                if mt[ni][nj] > mt[i][j]:   # 봉우리가 아니라면(주변이 나보다 높다면)
                    flag = False            # 일단 봉우리 불가
                if mt[ni][nj] == mt[i][j] and not visited[ni][nj]:  # 나랑 높이 같고 미방문이라면
                    stack.append((ni, nj))  # stack 추가
    if flag:        # 전체탐색 결과 봉우리라면
        cnt += 1    # 봉우리 추가
        
for i in range(N):
    for j in range(M):
        if not visited[i][j]:   # 미방문이라면
            bfs(i,j)            # bfs돌려라라
print(cnt)