1def factorial(num):
    n = 1
    for i in range(1, num + 1):
        n *= i
        n = n % 998244353
    return n


def solve():
    n = input()
    mode = "?"
    streak = 0
    operations = 0
    factor = 1

    for i in range(len(n)):
        if n[i] == mode:
            streak += 1
        else:
            operations += streak
            factor *= (streak + 1)
            streak = 0
        mode = n[i]

    operations += streak
    factor *= (streak + 1)

    ans = factor * factorial(operations) % 998244353

    return operations, ans


for _ in range(int(input())):
    print(*solve())
