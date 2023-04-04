'''
문제
뿌요뿌요의 룰은 다음과 같다.

필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.

뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.

아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다. 하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

입력
총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.

이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.

R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.

입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

출력
현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.
'''
import sys
input = sys.stdin.readline

def blow():
    flag = True                             # 더 터질 뿌요가 있는지 확인하는 flag
    chain = 0                               # 연쇄 횟수 셀 변수
    while flag:
        bomb = []                           # 한 연쇄에서 함께 터지는 뿌요들 담을 배열
        visited = [[0]*12 for _ in range(6)]
        
        for i in range(6):
            for j in range(12):
                if puyopuyo[i][j] != '.' and not visited[i][j]: # 빈칸이 아니고 미방문이라면
                    stack = []                                  
                    stack.append((i,j))                         # 탐색을 위해 in stack
                    visited[i][j] = 1                           # 방문처리
                    cnt = 1                                     # 4개 뿌요가 모여있는지 세기위한 cnt
                    temp = [(i,j)]                              # 4개 이상일 시 bomb에 담기위한 temp
                    while stack:
                        x, y = stack.pop()
                        for di, dj in delta:
                            ni,nj = x + di, y +dj
                            if 0 <= ni < 6 and 0 <= nj < 12 and puyopuyo[x][y] == puyopuyo[ni][nj] and not visited[ni][nj]: # 범위 내고 같은 뿌요면서 미방문이면
                                stack.append((ni,nj))           # 스택에 담고
                                temp.append((ni,nj))            # temp에도 담는다
                                visited[ni][nj] = 1             # 방문처리
                                cnt += 1                        # 뿌요 개수 + 1
                    if cnt >= 4:                                # 해당 뿌요가 4개 이상 모여있으면
                        bomb.extend(temp)                       # 이번 연쇄에 터질 bomb에 저장                   
        if bomb:                                                # 끝까지 순회 후 터질 bomb이 있다면
            for k in range(len(bomb)):                  
                puyopuyo[bomb[k][0]][bomb[k][1]] = '.'          # 터트리고
            for li in puyopuyo:                                 # 빈자리를 없앤다음
                while '.' in li:
                    li.remove('.')
            for li in puyopuyo:                                 # 뒷자리를 빈칸으로 다시 채운다
                while len(li) < 12:
                    li.append('.')
            chain += 1                                          # 연쇄 + 1
        
        else:
            flag = False                                        # 필드 전체 순회 후 터질 뿌요가 없었다면 그만 탐색위해 flag를 False로 변환
                        
    return chain
puyo = [list(input()) for _ in range(12)]
puyopuyo = [[0]*12 for _ in range(6)]
delta = (-1,0) , (0,1), (1,0), (0,-1)

for i in range(6):
    for j in range(12):
        puyopuyo[i][j] = puyo[11-j][i]      # 배열을 시계방향으로 90도 회전
print(blow())