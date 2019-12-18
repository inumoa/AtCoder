N = int(input())
if N/1.08 == -(-N//1.08):
    print(int(N/1.08))
# もとの数の商より大きく，+1の商より小さい整数
else:
    if not -(-N//1.08) == -(-(N+1)//1.08):
        print(int((N+1)//1.08))
    else:
        print(':(')