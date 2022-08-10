'''
문제
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

입력
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

출력
첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

예제 입력 1 
1 2 3 4 5 6 7 8
예제 출력 1 
ascending
예제 입력 2 
8 7 6 5 4 3 2 1
예제 출력 2 
descending
예제 입력 3 
8 1 7 2 6 3 5 4
예제 출력 3 
mixed
'''
# 내장함수 X, 얕은복사 이용
def down(arr):    # 내림차순
    for _ in range(llen(arr)):
        for j in range(llen(arr)-1):
            if arr[j+1] > arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def up(arr):    # 오름차순
    for _ in range(llen(arr)):
        for j in range(llen(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def llen(arr):  # len함수
    count = 0
    for _ in arr:
        count += 1
    return count



note = list(map(int, input().split()))
note_copy = note[:]     # 얕은복사
if note == down(note_copy):     # 복사없이 함수 돌리면 note 자체가 변경 됨
    print('descending')
elif note == up(note_copy):
    print('ascending')
else:
    print('mixed')

# 쉬운 풀이
note = list(map(int, input().split()))
if note == [1,2,3,4,5,6,7,8]:
    print('ascending')
elif note == [8,7,6,5,4,3,2,1]:
    print('descending')
else:
    print('mixed')