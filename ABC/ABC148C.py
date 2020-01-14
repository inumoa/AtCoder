import collections

def prime_factorize(n):
    # 1に注意
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


a, b = map(int, input().split())

if a == 1 or b == 1:
    print(a*b)
    exit()

a_dic = collections.Counter(prime_factorize(a))
b_dic = collections.Counter(prime_factorize(b))

target_list = list(set(list(a_dic.keys()) + list(b_dic.keys())))

result = 1

for i in target_list:
    if i in a_dic and i in b_dic:
        value = max(a_dic[i], b_dic[i])
    elif i not in b_dic:
        value = a_dic[i]
    else:
        value = b_dic[i]
    result *= i ** value

print(result)