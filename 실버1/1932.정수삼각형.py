'''
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
'''

# 삼각형 위에서부터 더해가며 값을 재정의하는 형태
N = int(input())
tri = []
for _ in range(N):
    tri.append(list(map(int, input().split())))

for i in range(1,N):
    for j in range(i+1):
        if j == 0:                              # 0이면(왼쪽끝) 
            tri[i][j] = tri[i-1][j] + tri[i][j] # 자신과 윗줄0번과 더함
        elif j == i:                            # i면(오른쪽끝)
            tri[i][j] = tri[i-1][j-1] + tri[i][j] # 자신과 윗줄 마지막 더함
        else:                                   # 중간이면
            tri[i][j] = max(tri[i-1][j], tri[i-1][j-1]) + tri[i][j] # 자신과 윗줄 부모 두개 중 최댓값을 더해줌
print(max(tri[N-1])) # 위에서부터 더해서 완성된 삼각형 마지막 줄 값에서 최댓값 출력
