'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''

def queen(i):
    global arr, cnt
    if len(arr) == N:   # 퀸을 끝줄까지 놨다면
        cnt +=1         # 경우의 수 +1
        return
        
    for j in range(N):              
        for k in range(len(arr)):
            if  abs(i - arr[k][0]) != abs(j - arr[k][1]) and j != arr[k][1]:    # 앞에 저장한 퀸들과 지금 놓을 자리를 비교
                pass    # 앞 퀸과 겹치지 않으면 일단 패스
            else:       # 하나라도 겹치면
                break   # break하고 다음 자리로 이동
        else:           # 앞 모든 퀸들과 비교해서 다 겹치지 않았다면
            arr.append((i,j))   # 해당 자리에 퀸 놓고
            queen(i+1)          # 다음 줄 확인하러 감
            arr.pop()           # 백트래킹
            
N = int(input())
arr = []
cnt = 0
queen(0)
print(cnt)

# def queen():
#     if len(arr) == N:
#         cnt +=1
#         return
#     for i in range(N):
#         if i not in arr and 
#         for j in range(N):
#             for k in range(len(arr)):
#                 if j == abs(arr[k][1]-j) or j == arr[k][1]:
#                     continue
#                 else:
#                     arr.append((i,j))
#                     break
#     if len(arr) == 8:
#         cnt += 1
# N = int(input())
# arr = []
# cnt = 0
# queen()
# print(cnt)




    # while len(arr) < N:
    #     # for k in range(N):
    #     #     arr.append((0,k))
    #     for i in range(N):
    #         for j in range(N):

    #             for k in range(len(arr)):
    #                 if  abs(i - arr[k][0]) != abs(j - arr[k][1]) and j != arr[k][1]:
    #                     arr.append((line, i))
        
        
        
    #     if i not in arr and 
    #     for j in range(N):
    #         for k in range(len(arr)):
    #             if j == abs(arr[k][1]-j) or j == arr[k][1]:
    #                 continue
    #             else:
    #                 arr.append((i,j))
    #                 break
    # if len(arr) == 8:
    #     cnt += 1