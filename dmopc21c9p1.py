n = int(input())
arr = map(int, input().split())

nums = [1]

for i in arr:
    nums.append(i - nums[-1])

n1 = [nums[i] for i in range(n) if i % 2 == 0]
n2 = [nums[i] for i in range(n) if i % 2 == 1]

ans = min(n2) - max(0, 1 - min(n1))

print(max(ans, 0))
