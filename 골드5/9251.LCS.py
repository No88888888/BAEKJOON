'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''

string_a = [0] + list(input())  # a 문자열을 패딩해서 받는다
string_b = [0] + list(input())  # b 문자열을 패딩해서 받는다
N = len(string_a)               
M = len(string_b)
LCS = [[0]*M for _ in range(N)] # LCS구하기 위한 2차원 배열 생성
max_length = 0                  # 최대 부분 수열 길이 값
for i in range(N):              
    for j in range(M):
        if i == 0 or j == 0:    # 패딩 부분이면
            LCS[i][j] = 0       # 0으로 냅둠
        elif string_a[i] != string_b[j]:                # 두 문자열 비교해서 다르다면
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])   # 그 전까지의 부분수열의 길이를 저장
        else:                                           # 두 문자열 비교해서 같다면
            LCS[i][j] = LCS[i-1][j-1] + 1               # 지금까지의 최대 부분 수열 + 1
            max_length = max(max_length, LCS[i][j])     
print(max_length)
