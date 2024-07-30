'''
문제
이민희와 민희진을 연결하면 이민희진

김서인과 서인국을 연결하면 김서인국

박건과 건빵을 연결하면 박건빵

민희는 한 사람의 이름 뒷부분이 다른 사람의 이름 앞부분과 같을 때, 이 둘을 연결하는 것을 재밌어한다.

 
$N$명의 사람이 주어질 때, 연결할 수 있는 서로 다른 사람 쌍의 개수를 구해보자.

각각 
$S, T$라는 이름을 가진 두 사람을 연결할 수 있으려면 다음과 같은 조건을 충족해야 한다.

 
$S, T$의 길이보다 작거나 같은 양의 정수 
$k$가 존재하여, 
$S$의 앞 
$k$글자와 
$T$의 뒤 
$k$글자가 일치하거나, 
$S$의 뒤 
$k$글자와 
$T$의 앞 
$k$글자가 일치해야 한다.

입력
첫 줄에는 사람 수 
$N$이 주어진다. 
$\left(1 \leq N \leq 100\right)$

두 번째 줄부터 
$N$개 줄에 걸쳐 각 사람의 이름이 주어진다.

이름은 영어 소문자로만 구성되어 있으며, 길이는 최소 1자, 최대 20자이다.

단, 동명이인이 있을 수 있다.

출력
첫 줄에 연결할 수 있는 서로 다른 사람 쌍의 개수를 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input().strip())
names = [input().strip() for _ in range(N)]
cnt = 0
def check(name1, name2):
    global cnt
    S, T = len(name1), len(name2)
    if S <= T:
        for k in range(S):
            if name1[k:] == name2[:S-k] or name2[T-S+k:] == name1[:S-k]:
                cnt += 1
                return
    else:
        for r in range(T):
            if name2[r:] == name1[:T-r] or name1[S-T+r:] == name2[:T-r]:
                cnt += 1
                return

for i in range(N-1):
    for j in range(i+1, N):
        if names[i] == names[j]:
            cnt += 1
            continue
        check(names[i], names[j])
print(cnt)