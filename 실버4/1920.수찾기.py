'''
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''

def binary(R, key):
    S = 0                   # 시작 - A 첫 인덱스
    E = R                   # 끝 - A 마지막 인덱스
    while S <= E:           # 처음과 끝도 탐색해야하기 때문에 '<='
        C = (S + E)//2      # 이진 탐색 위한 중간 C
        if A[C] == key:     # 같다면
            return 1        
        else:           
            if A[C] < key:  # 다른데 key가 더 크다면
               C += 1       # C +=1 후 이를 Start로 치환
               S = C
            elif A[C] > key: # 다른데 key가 더 작다면
                C -= 1       # C -=1 후 이를 end로 치환
                E = C        
    return 0                # 없다면 0

N = int(input())                                # 정수 갯수
A = sorted(list(map(int, input().split())))     # 오름차순 정렬한 정수
M = int(input())                                
B = list(map(int, input().split()))             # 찾을 정수

for i in range(len(B)):
    print(binary(len(A)-1, B[i]))               
    