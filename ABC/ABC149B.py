A, B, K = map(int, input().split())
a = max(A-K, 0)
b = max(min(A-K, 0) + B, 0)
print(a, b)