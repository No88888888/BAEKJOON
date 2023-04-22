'''
문제
한별이는 출근하던 도중 이세계 대환장 버스에 치였다.



그림 B.1: 이세계 대환장 버스



그림 B.2: 출근하는 한별이

올해 휴가를 전부 써 버려 당장 판교로 돌아가야 하는 한별이는 돌아가기 위한 방법을 어떻게든 찾아보기 위해 이세계를 돌아다녀 보려고 한다.

이세계는 
$R\times C$의 격자로 되어 있다. 지금은 밤이어서 한별이는 자신이 위치한 칸 및 그 칸에서 위, 아래, 왼쪽 또는 오른쪽으로 인접한 칸만을 볼 수 있지만, 와드를 설치하면 조금 더 넓은 영역의 시야를 확보할 수 있다. 구체적으로는, 격자의 모든 칸은 각각 어떤 영역 하나에 속해 있는데, 와드를 놓으면 와드가 놓인 칸이 속한 영역에 있는 모든 칸을 볼 수 있게 된다.

한별이의 여행 기록이 주어질 때 한별이가 얼마나 넓은 시야를 확보했을지 계산해 보자.

입력
첫 번째 줄에는 격자의 크기를 나타내는 두 정수 
$R$과 
$C$가 주어진다. (
$1 \le R,C \le 1\,000$)

다음 줄부터 
$R$개의 줄에 걸쳐 격자의 정보가 주어진다. 각 줄은 
$C$개의 알파벳 소문자로 이루어져 있으며, 위, 아래, 왼쪽 또는 오른쪽으로 인접해 있는 칸이 같은 문자라는 것은 두 칸이 같은 영역에 속해 있음을 의미한다.

다음 줄에는 한별이가 이세계에 떨어진 위치를 나타내는 두 정수 
$H_R$, 
$H_C$가 주어진다. 이는 한별이가 위에서 
$H_R$번째 줄, 왼쪽에서 
$H_C$번째 칸에 떨어졌음을 의미한다. (
$1 \le H_R \le R$, 
$1 \le H_C \le C$)

마지막 줄에는 한별이의 여행 기록을 나타내는 
$200\,000$글자 이하의 문자열이 주어진다. 여행 기록의 각 문자는 U, D, L, R, W 중 하나로 이루어져 있으며, U, D, L, R은 각각 위, 아래, 왼쪽, 오른쪽으로 한 칸 이동했다는 뜻이고, W는 지금 있는 칸에 와드를 설치했다는 뜻이다. 한별이가 격자를 벗어나는 경우는 주어지지 않는다.

출력
 
$R$개의 줄에 걸쳐 한별이의 시야를 출력한다. 각 줄은 
$C$개의 문자로 되어 있어야 하며, 
$R$번째 줄 
$C$번째 문자가 .이라면 한별이의 시야에 해당 칸이 들어와 있다는 뜻이고 #이라면 그렇지 않다는 뜻이다.
'''

import sys
input = sys.stdin.readline

def gkatn(X, Y):
    visited = [[0]*M for _ in range(N)]
    for m in range(len(movement)):
        if movement[m] == 'R':                          # 이동따라 이동시키기
            X, Y = X + delta[1][0], Y + delta[1][1]
        elif movement[m] == 'L':
            X, Y = X + delta[3][0], Y + delta[3][1]
        elif movement[m] == 'D':
            X, Y = X + delta[2][0], Y + delta[2][1]
        elif movement[m] == 'U':
            X, Y = X + delta[0][0], Y + delta[0][1]
        elif movement[m] == 'W' and not visited[X][Y]:  # 와드 박는거면서 해당 위치 미방문이면
            arr = [(X,Y)]                               # 주변 같은 영역 탐색위한 배열
            visited[X][Y] = 1                           # 방문 처리
            ans[X][Y] = '.'                             # 시야 확보
            while arr:
                x, y = arr.pop()
                for di, dj in delta:                    # 4방 탐색하며 동일 영역 시야 확보
                    ni, nj = x + di, y + dj
                    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and isekai[ni][nj] == isekai[x][y]:
                        visited[ni][nj] = 1
                        ans[ni][nj] = '.'
                        arr.append((ni,nj))
        if m == len(movement)-1:                        # 마지막 이동이면
            ans[X][Y] = '.'                             # 해당 위치 + 사방 시야 확보
            for di, dj in delta:
                ni, nj = X + di, Y + dj
                if 0 <= ni < N and 0 <= nj < M:
                    ans[ni][nj] = '.'
                    
N, M = map(int, input().split())
isekai = [list(input()) for _ in range(N)]  # 이세계 영역 정보
X, Y = map(int, input().split())            # 시작위치
X -= 1                                      # 인덱스 맞추기
Y -= 1
movement = list(input())                    # 이동 정보
ans = [['#'] * M for _ in range(N)]         # 정답 배열

delta = (-1, 0), (0, 1), (1, 0), (0, -1)
gkatn(X, Y)

for r in ans:
    print(''.join(r))