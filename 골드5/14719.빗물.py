'''
문제
2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.



비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

입력
첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)

두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.

따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

출력
2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.

빗물이 전혀 고이지 않을 경우 0을 출력하여라.
'''
'''
1. 전체구간(왼쪽끝~오른쪽끝)에서 빈 공간을 센다
2. 왼쪽 끝, 오른쪽 끝 확인하여 0 이하이면 재탐색하여 전체구간을 바꿔준다
3. 최대높이 기둥까지 반복하며 빈공간(빗물 차는 부분)을 세준다
'''
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))
L, R = 0, W-1                       # 왼쪽끝 좌표, 오른쪽 끝 좌표
M = max(block)                      # 최대높이
res = 0

for i in range(M):                  # 최대높이까지만 순회
    if block[L] == 0:               # 왼쪽끝 0 이하일 시
        for i in range(L, R+1):
            if block[i] > 0:
                L = i
                break
    if block[R] == 0:
        for i in range(R , L-1 , -1):
            if block[i] > 0:
                R = i
                break
    W = R - L + 1                   # 전체구간 재정의
    cnt = 0
    for k in range(L, R+1):         # 전체구간에서 기둥갯수 세기
        if block[k] > 0:
            cnt += 1
    
    res += W - cnt                  # 전체구간에서 기둥갯수 빼기(빗물차는 공간)
    for t in range(L, R+1):         # 기둥 1씩 빼주기
        block[t] -= 1
    
print(res)



#--------------------------------------------
'''
2차원배열 이용 풀이

'''
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))
M = max(block)                      # 위에 남는 공간은 필요 없으므로 제일 높은 기둥 높이까지만 2차원 배열을 만든다
arr = [[0] * M for _ in range(W)]
cnt = 0                             # 1 혹은 -1로 바꾸는 횟수를 셀 cnt
#양쪽 맨끝을 기둥은 1, 빈 공간은 -1로 채움
for i in range(M):
    if i < block[0]:                # 왼쪽끝 기둥
        arr[0][i] = 1        
    else:
        arr[0][i] = -1
    cnt += 1
    if i < block[-1]:               # 오른쪽 끝 기둥
        arr[-1][i] = 1
    else:
        arr[-1][i] = -1
    cnt += 1
# 중간 기둥들 / 자기보다 앞 기둥을 보면서 1이거나 0이면 냅두고 -1이면 -1로 채움
for i in range(1, W-1):
    for j in range(M):
        if j < block[i]:
            arr[i][j] = 1
            cnt += 1
        else:
            if arr[i-1][j] == -1:
                arr[i][j] = -1
                cnt += 1
# 오른쪽 끝기둥부터 역으로 보면서 -1 채워져야 했던 곳 -1로 채움
stack = []
for j in range(len(arr[-1])):
    if arr[W-1][j] == -1:
        stack.append((W-1,j))
        while stack:
            x, y = stack.pop()
            if arr[x-1][y] == 0:
                arr[x-1][y] = -1
                stack.append((x-1, y))
                cnt += 1
print(W*M-cnt)  # 전체 2차원 공간에서 기둥(1)이나 빗물이 안차는 공간(-1)을 채우면서 셋던 횟 수를 뺀다 = 빗물 찬 공간

    
    