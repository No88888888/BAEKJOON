'''
문제
빙고 게임은 다음과 같은 방식으로 이루어진다.

먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다



다음은 사회자가 부르는 수를 차례로 지워나간다. 예를 들어 5, 10, 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다.




차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.



이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.



철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.
'''
chulsu = [list(map(int, input().split())) for _ in range(5)]    # 철수가 쓴 빙고 종이
chulsu90 = [[0]*5 for _ in range(5)]                            # 90도 반전
chulsu_slash = [0]*26                                           # 대각선 숫자들의 리스트 인덱스 = 숫자
chulsu_rev_slash = [0]*26                                       # 역대각선 숫자들의 리스트 인덱스 = 숫자
for i in range(5):
    for j in range(5):
        chulsu90[i][j] = chulsu[j][i]
        if i == j:
            chulsu_slash[chulsu[i][j]] =chulsu[i][j]
        if 4-i == j:
            chulsu_rev_slash[chulsu[i][j]] = chulsu[i][j]
MC = [list(map(int, input().split())) for _ in range(5)]        # 사회자 숫자

def find_bingo(MC, chulsu, chulsu90, chulsu_slash, chulsu_rev_slash):
    cnt = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                bingo = 0                                   # 빙고 초기화
                for h in range(5):
                    if MC[i][j] == chulsu[k][h]:            # 사회자 부른 숫자와 철수 숫자 같으면
                        chulsu[k][h] = 0                    # 해당 부분 0
                        chulsu90[h][k] = 0                  #    "
                        if k == h:                          # 대각선 부분이라면
                            chulsu_slash[MC[i][j]] = 0      # 대각선 리스트에서 해당 숫자 0
                        if 4-k == h:                        # 역대각선 부분이라면
                            chulsu_rev_slash[MC[i][j]] = 0  # 역대각선 리스트에서 해당 숫자 0
                        cnt += 1                            # 숫자 하나 지울 때마다 cnt + 1
                        for t in range(5):                  # bingo 유무 체크
                            if sum(chulsu[t]) == 0:
                                bingo += 1
                            if sum(chulsu90[t]) == 0:
                                bingo += 1
                        if sum(chulsu_slash) == 0:
                            bingo += 1
                        if sum(chulsu_rev_slash) == 0:
                            bingo += 1
                        if bingo >= 3:                      # 사회자 한번 부를때마다 빙고 체크하여 3개 이상이면
                            return cnt                      # cnt 반환

print(find_bingo(MC, chulsu, chulsu90, chulsu_slash, chulsu_rev_slash))
