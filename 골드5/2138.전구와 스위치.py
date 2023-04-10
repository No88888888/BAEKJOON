'''
문제
N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(2 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 0은 켜져 있는 상태, 1은 꺼져 있는 상태를 의미한다.

출력
첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.
'''
'''
첫번째 전구를 누르거나 누르지 않는 경우 두 가지 시도한 후
그 중 목표와 같은 것 중 최소 횟수를 출력하는 방식
'''
N = int(input())
now = list(input())                                     # 현재 상태
want = list(input())                                    # 원하는 상태

# 첫 전구 누르는 케이스
cnt1 = 0                                                # 스위치 누르는 횟수 
temp1 = now[:]                                          # 복사
for i in range(N):
    if i == 0:                                          # 첫 전구 시 스위치 누름
        temp1[i] = str(abs(int(temp1[i]) - 1))          # 첫 전구 누르고
        temp1[i+1] = str(abs(int(temp1[i+1]) - 1))      # 그 다음 전구 누름
        cnt1 += 1
    elif i == N-1:                                      # 끝 전구 시
        if temp1[i-1] != want[i-1]:                     # 이전 전구가 목표와 다르다면
            temp1[i-1] = str(abs(int(temp1[i-1]) - 1))  # 끝에서 두 전구 누름
            temp1[i] = str(abs(int(temp1[i]) - 1))
            cnt1 += 1
    else:
        if temp1[i-1] != want[i-1]:                     # 중간 전구고 이전 전구가 목표와 다르다면
            temp1[i-1] = str(abs(int(temp1[i-1]) - 1))  # 셋 전구 누름
            temp1[i] = str(abs(int(temp1[i]) - 1))
            temp1[i+1] = str(abs(int(temp1[i+1]) - 1))
            cnt1 += 1

# 첫 전구 스위치 누르지 않는 케이스
temp2 = now[:]
cnt2 = 0
for i in range(N):
    if i == 0:                                          # 첫 전구 통과
        continue
    elif i == N-1:                                      # 나머지는 상동
        if temp2[i-1] != want[i-1]:
            temp2[i-1] = str(abs(int(temp2[i-1]) - 1))
            temp2[i] = str(abs(int(temp2[i]) - 1))
            cnt2 += 1
    else:
        if temp2[i-1] != want[i-1]:
            temp2[i-1] = str(abs(int(temp2[i-1]) - 1))
            temp2[i] = str(abs(int(temp2[i]) - 1))
            temp2[i+1] = str(abs(int(temp2[i+1]) - 1))
            cnt2 += 1
if temp1 == want and temp2 != want:                     # 두 케이스 중 목표와 같은게 하나 있다면
    print(cnt1)                                         # 해당 케이스의 스위치 클릭 횟수 출력
elif temp1 != want and temp2 == want:
    print(cnt2)
elif temp1 == want and temp2 == want:                   # 두 케이스 모두 목표와 같다면
    print(min(cnt1, cnt2))                              # 두 개 중 최소 스위치 클릭 값 출력
else:                                                   # 목표와 맞출 수 없다면
    print(-1)                                           # -1 출력