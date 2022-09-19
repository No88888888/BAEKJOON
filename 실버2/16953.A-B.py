'''
문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
'''

# A, B = map(int, input().split())

# arr = [0]*10**10
# arr[1] = A
# i = 1
# out= False
# res = 0
# while i < len(arr)-1:
#     if out == True:
#         break
#     for i in range(2,len(arr)):
#         if i%2 == 0:
#             arr[i] = arr[i//2]*2
#         if i%2 == 1:
#             arr[i] = arr[i//2]*10+1
#         if arr[i] == B:
#             res = i
#             out = True
#             break
# if res:
#     cnt = 1
#     while i > 1:
#         cnt += 1
#         i//=2
#     print(cnt)
# else:
#     print(-1)

# --------------------------
# A, B = map(int, input().split())

# arr = [0]*10**5
# arr[1] = A
# i = 1
# out= False
# res = 0
# while arr[i] <=B:
#     if out == True:
#         break
#     for i in range(2,len(arr)):
#         if i%2 == 0:
#             arr[i] = arr[i//2]*2
#         if i%2 == 1:
#             arr[i] = arr[i//2]*10+1
#         if arr[i] == B:
#             res = i
#             out = True
#             break
# if res:
#     cnt = 1
#     while i > 1:
#         cnt += 1
#         i//=2
#     print(cnt)
# else:
#     print(-1)
    
    
# ----------------------------
# def enq(last):
#     if tree[last] > B:
#         return
#     if tree[last] == B:
#         return last
#     last+=1
#     c = last
#     p = c//2
#     while c < len(tree):
#         if c%2==0:
#             tree[c] = tree[p]*2
#             enq(c)
            
#         elif c%2==1:
#             tree[c] = tree[p]*10+1
#             enq(c)
           
    
# A, B = map(int, input().split())
# tree = [0]*10**2
# tree[1]= A
# last= 1
# print(enq(last))

# ------------------------------
A, B = map(int, input().split())
cnt = 1
res = 0
while B>=A:             # B에서 A를 찾아가는 방식
    if B%2 == 1:        # 2배 혹은 10배 +1 밖에 없으므로 B가 홀수면
        B = (B-1)/10    # 1을 빼고 10으로 나눈다 
        cnt +=1         # 횟수 +1
    else:               # 짝수라면
        B = B/2         # 2로 나눈다
        cnt +=1         # 횟수 +1
    if B == A:          # A가 됐다면
        res = cnt       # 카운트 저장
if res:                 
    print(res)
else:                   # A가 안만들어지면 res = 0
    print(-1)