import math


def value(x_list, kaijo):

    num_list = list(range(len(x_list)+1))

    result = 1
    count = len(x_list)
    for x in x_list:
        kaijo /= count
        count -= 1
        target_value = num_list[x] - 1
        result += target_value * kaijo

        new_list = [0]*(len(x_list)+1)

        for i, num in enumerate(num_list):
            if num > target_value:
                new_list[i] = num-1
            else:
                new_list[i] = num

        num_list = new_list

    return int(result)


N = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

kaijo = math.factorial(N)

p_value = value(p_list, kaijo)
q_value = value(q_list, kaijo)
print(abs(p_value-q_value))