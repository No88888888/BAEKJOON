'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''
import math
N = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    if i <= 2:          # 2이하 자연수 중
        if i == 1:      # 1이면
            N -= 1      # 소수 아니니까 -1
        continue
            
    for j in range(2, int(math.sqrt(i))+1): # 2 초과 수 중 해당 수의 제곱근까지만큼 나눠본다
        if not i % j:                       # 나눈 나머지가 0이라면 약수라는 뜻
            N -= 1                          # 소수 아니다
            break
print(N)