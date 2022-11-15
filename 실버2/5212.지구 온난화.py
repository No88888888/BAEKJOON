'''
문제
푸르고 아름다운 남해에는 많은 섬이 장관을 이루고 있다. 그림이 아니면 볼 수 없을 것 같은 아름다운 장관을 실제로 볼 수 있는 다도해로 상근이는 여행을 떠났다.

다도해에 도착한 상근이는 서울에서 보던 것과는 다른 풍경에 큰 충격을 받았다. 지구 온난화로 인해 해수면이 상승해 섬의 일부가 바다에 잠겨버렸다.

서울로 다시 돌아온 상근이는 이렇게 지구 온난화가 계속 될 경우 남해의 지도는 어떻게 바뀔지 궁금해졌다.

다도해의 지도는 R*C 크기의 그리드로 나타낼 수 있다. 'X'는 땅을 나타내고, '.'는 바다를 나타낸다.

50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다는 사실을 알았다.

상근이는 50년 후 지도를 그려보기로 했다. 섬의 개수가 오늘날보다 적어질 것이기 때문에, 지도의 크기도 작아져야 한다. 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다. 50년이 지난 후에도 섬은 적어도 한 개 있다. 또, 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.

입력
첫째 줄에 지도의 크기 R과 C (1 ≤ R, C ≤ 10)가 주어진다. 다음 R개 줄에는 현재 지도가 주어진다.

출력
50년 후의 지도를 출력한다.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
earth = [list(input()) for _ in range(N)]
delta = (-1,0), (0,1), (1,0), (0,-1)
Xp = []                         # 섬의 좌표
vanish = []                     # 사라질 섬의 좌표

for i in range(N):
    for j in range(M):
        if earth[i][j] == 'X':
            Xp.append((i,j))    # 섬 좌표 저장
            
for x, y in Xp:
    cnt = 0
    for di, dj in delta:
        ni, nj = x + di, y+ dj
        if not 0 <= ni < N or not 0 <= nj < M or earth[ni][nj] == '.':
            cnt += 1
    if cnt >= 3:                # 3면 이상이 바다면
        vanish.append((x,y))    # 사라질 섬에 저장
        
for x, y in vanish:
    earth[x][y] = '.'           # 섬 없애고
    Xp.remove((x,y))            # 원래 섬 좌표에서도 삭제
min_x = min(Xp, key=lambda x: x[0])[0]  # 남은 섬 좌표에서 네 귀퉁이 찾음
max_x = max(Xp, key=lambda x: x[0])[0]
min_y = min(Xp, key=lambda x: x[1])[1]
max_y = max(Xp, key=lambda x: x[1])[1]
        
for i in range(min_x, max_x+1):         # 귀퉁이를 끝으로하여 남은 지도 출력
    print(''.join(earth[i][min_y:max_y+1]))

