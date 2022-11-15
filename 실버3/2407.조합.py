'''
문제
nCm을 출력한다.

입력
n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

출력
nCm을 출력한다.
'''
# / 를 쓰면 실수오차가 발생, // 를 써야 함
n, m = map(int, input().split())
res = 1
for i in range(m):
    res *= (n-i)
for i in range(1, m+1):
    res //= i
print(res)


# import math
# n, m = map(int, input().split())
# res = math.factorial(n)/(math.factorial(m)*math.factorial(n-m))
# print(int(res))
