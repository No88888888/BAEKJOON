'''
문제
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

출력
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.
'''

L, C = map(int, input().split())
password = list(input().split())
A= []
B= []
for i in password:
    if i in 'aeiou':
        A.append(i)                     # 모음 
    else:
        B.append(i)                     # 자음
subset = [[]]
result = []
ans = []
for char in password:                   # 모든 부분집합 구하기
    for i in range(len(subset)):
        subset.append(subset[i]+[char])
        
for i in range(len(subset)):            # 조건맞는 부분집합만 result 저장
    for j in range(len(subset[i])):
        if len(subset[i]) == L and subset[i][j] in A:   # 길이 L이고 모음이 포함되고
            cnt = 0
            for k in range(len(B)):
                for h in range(len(subset[i])):
                    if subset[i][h] == B[k]:
                        cnt +=1
                    if cnt >= 2:                        # 자음 개수가 2개 이상이면
                        result.append(subset[i])        # result에 추가
                        break

for i in result:                    # 글자 순서 sort
    i.sort()

for i in range(len(result)):        # 문자 형태로 list 벗기기
    ans.append(''.join(result[i]))

res = sorted(set(ans))              # 중복 제거, 사전 순서로 정렬

for i in res:                       # 하나씩 출력
    print(i)
    


    



# for i in range(L):                  # 순서대로 정렬(실패)
#     for j in range(len(result)):
    
#         for k in range(len(result)-j-1):
#             if ord(result[k][i]) > ord(result[k+1][i]):
#                 result[k], result[k+1] = result[k+1], result[k]
# for i in range(len(result)):
#     print(''.join(result[i]))
            # print(''.join(subset[i]))
            # break
        
        
# def back(i, N, h, t):           # i: 시작 원소 N:마지막원소 h: 부분집합의 합 t: 구하는 부분집합 합
#     global answer
#     if i == N:                  # 모든 원소가 고려된 경우
#         if h == t:              #부분집합의 합이 t면
#             answer += 1
#         return
#     else:
#         back(i+1, N, h+num[i], t)    # A[i]가 포함되는 경우
#         back(i+1, N, h, t)         # A[i]가 포함되지 않은 경우
        
# N, S = map(int, input().split())
# num = list(map(int, input().split()))
# answer = 0
# back(0, N, 0, S)

# if S == 0:       # 구하려는 합이 0일 경우 공집합인 경우도 answer에 포함되기 때문에
#     answer -= 1  # 공집합 경우를 -1
# print(answer)


