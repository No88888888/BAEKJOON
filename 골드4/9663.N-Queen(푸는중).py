'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''
def queen():
    if len(arr) == N:
        cnt +=1
        return
    for i in range(N):
        if i not in arr and 
        for j in range(N):
            for k in range(len(arr)):
                if j == abs(arr[k][1]-j) or j == arr[k][1]:
                    continue
                else:
                    arr.append((i,j))
                    break
    if len(arr) == 8:
        cnt += 1
N = int(input())
arr = []
cnt = 0
queen()
print(cnt)