'''
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

출력
S에 PN이 몇 군데 포함되어 있는지 출력한다.

제한
1 ≤ N ≤ 1,000,000
2N+1 ≤ M ≤ 1,000,000
S는 I와 O로만 이루어져 있다.
'''

N = int(input())
M = int(input())
S = list(input())       # 타겟
P = ['I']               
for i in range(N):
    P.extend(['O','I']) # 패턴
i = 0
j = 0
cnt = 0
while i < len(S):
    if P[j] == S[i]:    # 같으면 다음으로 이동
        i += 1
        j += 1
    else:               # 값은 다른데 j != 0라면, i자리는 유지, j = 0
        if j != 0:
            j = 0
        else:           #값은 다른데 j == 0라면 , i 값 한칸만 이동하고 처음부터 다시 진행
            i += 1
    if j == len(P):     # j가 패턴 길이면
        cnt += 1        # cnt + 1
        j = j - 2       # 어차피 앞부분은 다 맞기 때문에 해당 i와 j-2부터 맞는지 확인
        
print(cnt)

