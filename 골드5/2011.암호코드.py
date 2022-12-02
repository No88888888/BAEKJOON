'''
문제
상근이와 선영이가 다른 사람들이 남매간의 대화를 듣는 것을 방지하기 위해서 대화를 서로 암호화 하기로 했다. 그래서 다음과 같은 대화를 했다.

상근: 그냥 간단히 암호화 하자. A를 1이라고 하고, B는 2로, 그리고 Z는 26으로 하는거야.
선영: 그럼 안돼. 만약, "BEAN"을 암호화하면 25114가 나오는데, 이걸 다시 글자로 바꾸는 방법은 여러 가지가 있어.
상근: 그렇네. 25114를 다시 영어로 바꾸면, "BEAAD", "YAAD", "YAN", "YKD", "BEKD", "BEAN" 총 6가지가 나오는데, BEAN이 맞는 단어라는건 쉽게 알수 있잖아?
선영: 예가 적절하지 않았네 ㅠㅠ 만약 내가 500자리 글자를 암호화 했다고 해봐. 그 때는 나올 수 있는 해석이 정말 많은데, 그걸 언제 다해봐?
상근: 얼마나 많은데?
선영: 구해보자!
어떤 암호가 주어졌을 때, 그 암호의 해석이 몇 가지가 나올 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 5000자리 이하의 암호가 주어진다. 암호는 숫자로 이루어져 있다.

출력
나올 수 있는 해석의 가짓수를 구하시오. 정답이 매우 클 수 있으므로, 1000000으로 나눈 나머지를 출력한다.

암호가 잘못되어 암호를 해석할 수 없는 경우에는 0을 출력한다.
'''
import sys
input = sys.stdin.readline

code = input().strip()
N = len(code)
dp = [0] * (N+1)        # 자릿수와 인덱스 맞추기 위한 패딩
dp[0], dp[1] = 1, 1     # 0번 인덱스는 i-2를 위한 값, 1번 인덱스는 한자리 수(1~9)의 경우의 수

if not int(code[0]):    # 시작이 0이면 암호 불가능
    print(0)
else:
    for i in range(2, N+1):               # 1번까진 기본값 채웠기 때문에 2번쨰 자리부터
        if int(code[i-1]):                # 해당 자리의 수 단독으로 존재 시
            dp[i] = dp[i-1]               # default로 바로 이전 자리까지의 경우의 수를 가질 수 있으므로 이전자리의 경우의 수로 채워 넣는다
        temp = int(code[i-2] + code[i-1]) # 해당 자리의 수와 그 이전 자리의 수 합해 두자리 수로 존재 시
        if 10 <= temp <= 26:              # 10에서 26 사이(암호 가능)라면
            dp[i] += dp[i-2]              # 현재 위치 보다 두칸 앞인 i-2의 경우의 수(dp)를 추가로 더한다
    print(dp[N] % 1000000)
    

# code = input()
# N = len(code)
# arr = [0] * (N+1)
# arr[1], arr[2] = 1, 2
# for i in range(3, N+1):
#     arr[i] = arr[i-2] + arr[i-1]
# num = arr[-1]
# for i in range(N-1):
#     if int(code[i:i+2]) > 26 or ('0' in code[i:i+2] and code[i] == '0'):
#         print(code[i:i+2])
#         if i == 0:
#             num -= arr[len(code[i+2:])]
#         if i == N-2:
#             num -= arr[len(code[:i])]
#         else:
#             num -= (arr[len(code[:i])] * arr[len(code[i+2:])])
#     # if code[i] == '0':
#     #     if i == 0:
#     #         num -= arr[len(code[i+1:])]
#     #     if i == N-2:
#     #         num -= arr[len(code[:i])]
#     #     else:
#     #         num -= (arr[len(code[:i])] * arr[len(code[i+2:])])
        
# if num < 0:
#     print(0)
# else:
#     print(num%1000000)




# code = input()
# N = len(code)
# arr = [0] * (N+1)
# arr[1], arr[2] = 1, 2
# for i in range(3, N+1):
#     arr[i] = arr[i-2] + arr[i-1]
# num = arr[-1]
# if N == 1:
#     if not code:
#         print(0)
#     else:
#         print(1)
# if N == 2:
#     if not '0' in code:
#         if int(code) <= 26:
#             print(2)
#         else:
#             print(1)
#     else:
#         if code[0] == '0':
#             print(0)
#         else:
#             if code[0] > 2:
#                 print(0)
#             else:
#                 print(1)
# else:
#     for i in range(N):
#         if int(code[i:i+2]) > 26 :
#             if i == 0:
#                 num -= arr[len(code[i+2:])]
#             if i == N-2:
#                 num -= arr[len(code[:i])]
#             else:
#                 num -= (arr[len(code[:i])] * arr[len(code[i+2:])])
#         if code[i] == '0':
#             if i == 0:
#                 num -= (arr[len(code[i+1:])] + arr[len(code[i+2:])])
#             if i == N-1:
#                 num -= arr[len(code[:i])]
#             else:
#                 num -= ((arr[len(code[:i])] * arr[len(code[i+1:])]) + (arr[len(code[:i])] * arr[len(code[i+2:])]))
        
#     # if code[i] == '0':
#     #     if i == 0:
#     #         num -= arr[len(code[i+1:])]
#     #     if i == N-2:
#     #         num -= arr[len(code[:i])]
#     #     else:
#     #         num -= (arr[len(code[:i])] * arr[len(code[i+2:])])
        
#     if num < 0:
#         print(0)
#     else:
#         print(num%1000000)


# code = input()
# N = len(code)
# arr = [0] * (N+2)
# arr[1], arr[2] = 1, 2
# for i in range(3, N+1):
#     arr[i] = arr[i-2] + arr[i-1]
# num = arr[-2]

# for i in range(N):
#     if ('0' in code[i:i+2] and code[i] == '0'):
#         A, B, C = arr[len(code[:i])], arr[len(code[i+1:])], arr[len(code[i+2:])]
#         if A == 0:
#             A = 1
#         if B == 0:
#             if i == N-1:
#                 B = 0
#             else:
#                 B = 1
#         if C == 0:
#             if i >= N-2:
#                 C = 0
#             else:
#                 C = 1
#         num -= (A * B) + (A * C)
                
#     elif int(code[i:i+2]) > 26:
#         L, R = arr[len(code[:i])], arr[len(code[i+2:])]
#         if L == 0:
#             L = 1
#         if R == 0:
#             R = 1
#         num -= (L * R)

        
# if num < 0:
#     print(0)
# else:
#     print(num%1000000)
    
    
# code = input()
# N = len(code)
# arr = [0] * (N+2)
# arr[1], arr[2] = 1, 2
# for i in range(3, N+1):
#     arr[i] = arr[i-2] + arr[i-1]
# num = arr[-2]
# print(num)

# for i in range(N):
#     L, R = arr[len(code[:i])], arr[len(code[i+2:])]
#     if L == 0:
#         L = 1
#     if R == 0:
#         R = 1
#     if not (10 <= int(code[i:i+2]) <=26):
#         num -= L*R    
# print(num%1000000)
        
#     if ('0' in code[i:i+2] and code[i] == '0'):
#         A, B, C = arr[len(code[:i])], arr[len(code[i+1:])], arr[len(code[i+2:])]
#         if A == 0:
#             A = 1
#         if B == 0:
#             if i == N-1:
#                 B = 0
#             else:
#                 B = 1
#         if C == 0:
#             if i >= N-2:
#                 C = 0
#             else:
#                 C = 1
#         num -= (A * B) + (A * C)
                
#     elif int(code[i:i+2]) > 26:
#         if L == 0:
#             L = 1
#         if R == 0:
#             R = 1
#         num -= (L * R)

        
# if num < 0:
#     print(0)