import math

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


N, M = map(int, input().split())
a_list = list(map(int, input().split()))

lcm = lcm_list(a_list)

if M < (lcm/2):
    print(0)
else:
    print(M-(lcm/2))