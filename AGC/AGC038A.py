def main():
    h, w, a, b = list(map(int, input().split()))
    result_list = []
    for _ in range(b):
        result_list.append([0] * a + [1] * (w-a))
        if not min_count(result_list[-1]) == a:
            print('No')
            exit()
    for _ in range(h-b):
        result_list.append([1] * a + [0] * (w-a))
        if not min_count(result_list[-1]) == a:
            print('No')
            exit()
    for i in range(w):
        temp_list = []
        for j in range(h):
            temp_list.append(result_list[j][i])
        if not min_count(temp_list) == b:
            print('No')
            exit()
    result_str = ''
    for content in result_list:
        result_str += str(''.join(list(map(str, content)))) + '\n'
    print(result_str)


def min_count(input_list):
    zero = 0
    one = 0
    for v in input_list:
        if v == 0:
            zero += 1
        else:
            one += 1
    return min(zero, one)


if __name__ == '__main__':
    main()