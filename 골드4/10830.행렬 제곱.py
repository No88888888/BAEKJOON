'''
문제
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
'''

# 구글 답
N, B = map(int, input().split())                            # 행렬의 크기, 거듭제곱 수
arr = [list(map(int, input().split())) for _ in range(N)]   # 시작 행렬

def calmatrix(X,Y):                                         # X행렬 * Y행렬
    start = [[0 for _ in range(N)] for _ in range(N)]       # 곱한 행렬을 담은 배열
    for i in range(N):      
        for j in range(N):
            temp = 0                                        # 행렬 요소 하나의 값
            for k in range(N):
                temp += X[i][k] * Y[k][j]                   # 행렬 곱하기
            start[i][j] = temp % 1000                       # 1000으로 나눈 값
    return start

def square(arr, B):                                         # B를 2진수로 표현해서 1인 자릿수 찾기
    if B == 1:                                              # 1제곱이면
        for i in range(N):
            for j in range(N):
                arr[i][j] %= 1000                           # 1000으로 나눈 후
        return arr                                          # 그대로 반환
    
    tmp = square(arr, B//2)                                 # 2로 나눈다
    if B % 2:                                               # B를 2로 나눈 나머지가 1이라면
        return calmatrix(calmatrix(tmp,tmp), arr)           # B-1 제곱만큼 곱한 행렬에 arr 다시 곱하기
    else:                                                   # B를 나눈 나머지가 0이라면
        return calmatrix(tmp, tmp)                          # B/2제곱한 행렬을 제곱한다
    
    
result = square(arr, B)                                     # result는 arr를 B만큼 제곱
for r in result:                                            # 출력
    print(*r)
    
# chatGPT 답
n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def matrix_mul(A, B):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000
    return result

def matrix_pow(matrix, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        return matrix
    elif b % 2 == 0:
        temp = matrix_pow(matrix, b // 2)
        return matrix_mul(temp, temp)
    else:
        temp = matrix_pow(matrix, b - 1)
        return matrix_mul(temp, matrix)

result = matrix_pow(matrix, b)

for row in result:
    print(' '.join(map(str, row)))