import math
factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
a, x, n = map(int, input().split())
result = 0
for i in range(n + 1):
    result += (factorials[n] // (factorials[n - i] * factorials[i])) * (x ** i) * (a ** (n - i))
print(result)
