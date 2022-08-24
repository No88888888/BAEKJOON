'''
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
'''
# 백트래킹 이용풀이
# 양수만 더하면 구하려는 합보다 커질 시 가지치기가 가능한데
# 음수 포함이라 모든 부분집합을 구하게 돼서 백트래킹의 의미가 희석됨
# 456ms
def back(i, N, h, t):
    global answer
    if i == N:                  # 모든 원소가 고려된 경우
        if h == t:              #부분집합의 합이 t면
            answer += 1
        return
    else:
        back(i+1, N, h+num[i], t)    # A[i]가 포함되는 경우
        back(i+1, N, h, t)         # A[i]가 포함되지 않은 경우
        
N, S = map(int, input().split())
num = list(map(int, input().split()))
answer = 0
back(0, N, 0, S)

if S == 0:       # 구하려는 합이 0일 경우 공집합인 경우도 answer에 포함되기 때문에
    answer -= 1  # 공집합 경우를 -1
print(answer)

#----------------------------------------------------------

# 부분집합 이용 풀이
# 1440ms
N, S = map(int, input().split())
num = list(map(int, input().split()))
subset = [[]]                   # 부분집합을 담을 녀셕

def sum(arr):                   # sum 함수
    s = 0
    for i in arr:
        s += i
    return s
      
def d_sup():                    # 부분집합 합 함수
    global cnt
    for sub in subset:
        if sum(sub) == S:       # 부분집합 합이 S먄
            cnt +=1             # cnt + 1
    return cnt

for n in num:                   # 부분집합 구하는 for문
    for i in range(len(subset)):
        subset.append(subset[i] +[n])
cnt = 0        
d_sup()

if S == 0:                      # 구하려는 합이 0일경우
    cnt -= 1                    # 공집합 경우를 빼준다
print(cnt)