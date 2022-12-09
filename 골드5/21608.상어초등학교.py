'''
문제
상어 초등학교에는 교실이 하나 있고, 교실은 N×N 크기의 격자로 나타낼 수 있다. 학교에 다니는 학생의 수는 N2명이다. 오늘은 모든 학생의 자리를 정하는 날이다. 학생은 1번부터 N2번까지 번호가 매겨져 있고, (r, c)는 r행 c열을 의미한다. 교실의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다.

선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사했다. 이제 다음과 같은 규칙을 이용해 정해진 순서대로 학생의 자리를 정하려고 한다. 한 칸에는 학생 한 명의 자리만 있을 수 있고, |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.

비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
예를 들어, N = 3이고, 학생 N2명의 순서와 각 학생이 좋아하는 학생이 다음과 같은 경우를 생각해보자.

학생의 번호	좋아하는 학생의 번호
4	2, 5, 1, 7
3	1, 9, 4, 5
9	8, 1, 2, 3
8	1, 9, 3, 4
7	2, 3, 4, 8
1	9, 2, 5, 7
6	5, 2, 3, 4
5	1, 9, 2, 8
2	9, 3, 1, 4
가장 먼저, 4번 학생의 자리를 정해야 한다. 현재 교실의 모든 칸은 빈 칸이다. 2번 조건에 의해 인접한 칸 중에서 비어있는 칸이 가장 많은 칸인 (2, 2)이 4번 학생의 자리가 된다.

 	 	 
 	4	 
 	 	 
다음 학생은 3번이다. 1번 조건을 만족하는 칸은 (1, 2), (2, 1), (2, 3), (3, 2) 이다. 이 칸은 모두 비어있는 인접한 칸이 2개이다. 따라서, 3번 조건에 의해 (1, 2)가 3번 학생의 자리가 된다.

 	3	 
 	4	 
 	 	 
다음은 9번 학생이다. 9번 학생이 좋아하는 학생의 번호는 8, 1, 2, 3이고, 이 중에 3은 자리에 앉아있다. 좋아하는 학생이 가장 많이 인접한 칸은 (1, 1), (1, 3)이다. 두 칸 모두 비어있는 인접한 칸이 1개이고, 행의 번호도 1이다. 따라서, 3번 조건에 의해 (1, 1)이 9번 학생의 자리가 된다.

9	3	 
 	4	 
 	 	 
이번에 자리를 정할 학생은 8번 학생이다. (2, 1)이 8번 학생이 좋아하는 학생과 가장 많이 인접한 칸이기 때문에, 여기가 그 학생의 자리이다.

9	3	 
8	4	 
 	 	 
7번 학생의 자리를 정해보자. 1번 조건을 만족하는 칸은 (1, 3), (2, 3), (3, 1), (3, 2)로 총 4개가 있고, 비어있는 칸과 가장 많이 인접한 칸은 (2, 3), (3, 2)이다. 행의 번호가 작은 (2, 3)이 7번 학생의 자리가 된다.

9	3	 
8	4	7
 	 	 
이런식으로 학생의 자리를 모두 정하면 다음과 같다.

9	3	2
8	4	7
5	6	1
이제 학생의 만족도를 구해야 한다. 학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다. 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다. 그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.

학생의 만족도의 총 합을 구해보자.

입력
첫째 줄에 N이 주어진다. 둘째 줄부터 N2개의 줄에 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호가 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다.

학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생으로 이루어져 있다. 입력으로 주어지는 학생의 번호, 좋아하는 학생의 번호는 N2보다 작거나 같은 자연수이다. 어떤 학생이 자기 자신을 좋아하는 경우는 없다.

출력
첫째 줄에 학생의 만족도의 총 합을 출력한다.
'''
# 깔끔하게 정리된 식
import sys
input = sys.stdin.readline

N = int(input())
student = [list(map(int, input().split())) for _ in range(N**2)]
classroom = [[0]*N for _ in range(N)]
delta = (-1,0), (0,1), (1,0), (0,-1)    # 상 우 하 좌

for st in range(N**2):
    possible_list = []
    maxV = 0
    for i in range(N):
        for j in range(N):
            if not classroom[i][j]:
                like, empty, cnt = 0, 0, 0
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if classroom[ni][nj] in student[st][1:]:
                            like += 1
                        if not classroom[ni][nj]:
                            empty += 1
                        if 4-cnt + like < maxV:
                            break
                maxV = max(like, maxV)
                possible_list.append([like, empty, i, j])
    arr = sorted(possible_list, key=lambda x : (-x[0], -x[1], x[2], x[3]))
    classroom[arr[0][2]][arr[0][3]] = student[st][0]

res = 0
student.sort()
for i in range(N):
    for j in range(N):
        satisfy = 0
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if classroom[ni][nj] in student[classroom[i][j]-1]:
                    satisfy += 1
        if satisfy != 0:
            res += 10 ** (satisfy-1)
print(res)

'''
내 식
좋아하는 친구 비교 시 str으로 변환 후 거기에 있는지 비교하면 
한자리 수에서 문제 없으나 두자리 수일 때 오류가 난다
'''
import sys
input = sys.stdin.readline

N = int(input())
student = [list(map(int, input().split())) for _ in range(N**2)]
classroom = [[0]*N for _ in range(N)]
delta = (-1,0), (0,1), (1,0), (0,-1)    # 상 우 하 좌


for st in range(N**2):
    possible_list = []
    maxV = 0
    for i in range(N):
        for j in range(N):
            if not classroom[i][j]:
                like, empty, cnt = 0, 0, 0
                # like, empty = 0, 0
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += 1
                        # if str(classroom[ni][nj]) in ''.join(map(str, student[st][1:])):  # str으로 묶고 비교하면 두자리 수가 나올때 오류가 나버린다
                        if classroom[ni][nj] in student[st][1:]:
                            like += 1
                        if not classroom[ni][nj]:
                            empty += 1
                        if 4-cnt + like < maxV:
                            break
                maxV = max(like, maxV)
                possible_list.append([(i,j), like, empty])
    arr = sorted(possible_list, key=lambda x : (-x[1], -x[2], x[0][0], x[0][1]))
    classroom[arr[0][0][0]][arr[0][0][1]] = student[st][0]

res = 0
student.sort()
for i in range(N):
    for j in range(N):
        # for st in student:
        #     if classroom[i][j] == st[0]:
        satisfy = 0
        for di, dj in delta:
            ni, nj = i + di, j + dj
            # if 0 <= ni < N and 0 <= nj < N and (str(classroom[ni][nj]) in ''.join(map(str, st[1:]))):
            if 0 <= ni < N and 0 <= nj < N:
                if classroom[ni][nj] in student[classroom[i][j]-1]:
                    satisfy += 1
        if satisfy == 1:            
            res += 1
        elif satisfy == 2:
            res += 10
        elif satisfy == 3:
            res += 100
        elif satisfy == 4:
            res += 1000
print(res)
