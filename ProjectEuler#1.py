# Multiples of 3 & 5

def solve(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(solve(n))

# This code runs faster:
def solve(n):
    div3 = (n - 1) // 3
    div5 = (n - 1) // 5
    div15 = (n - 1) // 15

    sum3 = 3 * div3 * (div3 + 1) // 2
    sum5 = 5 * div5 * (div5 + 1) // 2
    sum15 = 15 * div15 * (div15 + 1) // 2

    return sum3 + sum5 - sum15


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(solve(n))
