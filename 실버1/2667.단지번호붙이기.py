'''
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''
# bfs로 풀이
import sys
input=sys.stdin.readline
N = int(input())
village = [list(map(int, input())) for _ in range(N)]

result = []
total = 0           # 단지의 갯수
for i in range(N):
    for j in range(N):
        if village[i][j] == 1:  # 단지 시작
            total += 1          # 단지 갯수 + 1
            village[i][j] = 0   # 탐색에 안걸리기 위해 0으로 바꿔줌
            q = [(i, j)]        # bfs탐색 위한 q 이용
            house = 1           # 해당 단지의 집 갯수
            while q:
                v = q.pop(0)
                for di, dj in [[-1,0], [0,1], [1,0], [0,-1]]:   # 상우하좌 탐색
                    ni = v[0] + di
                    nj = v[1] + dj
                    if 0<=ni<N and 0<=nj<N and village[ni][nj] == 1:    # 이웃한 집 저장
                        village[ni][nj] = 0     # 마찬가질 재탐색에 안걸리게 하기 위해 0으로 바꿈
                        q.append((ni, nj))
                        house += 1              # 집 갯수 + 1
            result.append(house)                # 한 단지 탐색 끝나면 집 갯수 저장
            
print(total)                # 단지 총 갯수
for i in sorted(result):    # 단지 당 집 갯수 오름차순 정렬하여 출력
    print(i)


# N = int(input())
# village = [list(map(int, input())) for _ in range(N)]

# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
# dir = 0
# visited = []
# for i in range(N):
#     for j in range(N):
#         stack = []
#         if village[i][j] == 1:
            
#             stack.append([i, j])
#             visited.append([i, j])
#             while stack:
#                 v = stack.pop()
#                 ni = v[0] + di[dir]
#                 nj = v[1] + dj[dir]
#                 if 0<=ni<N and 0<=nj<N and village[ni][nj] == 1 and visited[ni][nj] != 0:
#                     stack.append([ni, nj])
#                     visited.append([ni, nj])
#                     break
#                 else:
#                     dir += 1
#                     if dir == 4:
#                         dir = 0
