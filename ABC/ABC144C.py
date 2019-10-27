import math
n = int(input())
result = [0,0]
for i in range(1, int(math.sqrt(n))+1):
    if not n%i:
        result = [n/i,i]
print(int(sum(result)-2))