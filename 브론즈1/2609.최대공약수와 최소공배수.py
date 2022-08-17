'''
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''
A, B = map(int, input().split())
gongyaksu = ""
gongbaesu = ""
baesu = 1
A_ys = []
B_ys = []
A_bs = []
B_bs = []
for i in range(1, max(A, B)+1):
    if A%i == 0:
        A_ys += [i]
    if B%i == 0:
        B_ys += [i]

for i in range(len(A_ys)):
    if A_ys[i] in B_ys:
        gongyaksu = A_ys[i]
out = 1
while out == 1:
    A_bs += [A*baesu]
    B_bs += [B*baesu]
    if A >= B:
        if B_bs[baesu-1] in A_bs:
            gongbaesu = B_bs[baesu-1]
            out = 0
    if B > A:    
        if A_bs[baesu-1] in B_bs:
            gongbaesu = A_bs[baesu-1]
            out = 0
    else:
        baesu += 1
print(gongyaksu)
print(gongbaesu)
        
        
        