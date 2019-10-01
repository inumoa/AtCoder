n = int(input())
if n % 2:
    print(int((1 + n-1) * ((n-1) / 2)))
else:
    print(int((1 + n-1) * ((n-1) // 2) + -(-n // 2)))

