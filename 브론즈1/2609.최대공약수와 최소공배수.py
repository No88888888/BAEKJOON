'''
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

for i in range(min(A,B), 0, -1): # 더 빨리 찾기 위해 range -1
    if A%i == 0 and B%i == 0:
        YS = i                   # 최대공약수
        break
    
BS = YS * (A//YS) * (B//YS)      # 최소공배수

print(YS)
print(BS)

# 밑 3 풀이는 답은 맞으나 백준에서 시간초과
# ----------------------------------------
# import sys
# input = sys.stdin.readline
# 
# A, B = map(int, input().split())
# gongyaksu = ""
# gongbaesu = ""
# baesu = 1
# 
# A_bs = []
# B_bs = []
# for i in range(1, max(A, B)+1):
    # if A%i == 0 and B%i == 0:
        # gongyaksu = i
# out = 1
# while out == 1:
    # A_bs += [A*baesu]
    # B_bs += [B*baesu]
    # if A >= B:
        # if B_bs[baesu-1] in A_bs:
            # gongbaesu = B_bs[baesu-1]
            # out = 0
    # if B > A:    
        # if A_bs[baesu-1] in B_bs:
            # gongbaesu = A_bs[baesu-1]
            # out = 0
    # else:
        # baesu += 1
# print(gongyaksu)
# print(gongbaesu)
# --------------------------------------
# import sys
# input = sys.stdin.readline

# gongyaksu = ""
# gongbaesu = ""
# A, B = map(int, input().split())
# C = A*B
# list = []
# for i in range(1,C+1):
#     if C%i == 0:
#         list += [i]
        
# for i in list:
#     if A%i == 0 and B%i == 0:
#         gongyaksu = i
# for i in list:
#     if i%A == 0 and i%B == 0:
#         gongbaesu = i
#         break
# print(gongyaksu)
# print(gongbaesu)

# ----------------------------------------------
# import sys
# input = sys.stdin.readline

# A, B = map(int, input().split())
# C = A*B                             # 두 수의 곱
# YS = ""
# BS = ""
# for i in range(1,C+1):
#     if C%i == 0:
#         if A%i == 0 and B%i == 0:   # C의 약수 중 A,B를 나눈 나머지가 0인 수 중 최대값
#             YS = i
#         elif i%A == 0 and i%B == 0: # C의 약수 중 A,B로 나눈 나머지가 0인 수 중 최소값 
#             BS = i
#             break
# print(YS)
# print(BS)
        
        