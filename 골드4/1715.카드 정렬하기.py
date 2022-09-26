import heapq, sys

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    heapq.heappush(nums, int(input()))
total = 0
while len(nums) > 1:
    min1 = heapq.heappop(nums)
    min2 = heapq.heappop(nums)
    total += min1 + min2
    heapq.heappush(nums, min1 + min2)
print(total)