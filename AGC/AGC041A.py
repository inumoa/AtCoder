N, A, B = map(int, input().split())
if not (B - A) % 2:
    print((B - A)//2)
else:
    if B - 1 > N - A:
        b = N - A + 1
        a = N - B + 1
        A = a
        B = b

    if B-A == 1:
        print(B-1)

    else:
        print(-(-(B-A)//2) + A - 1)