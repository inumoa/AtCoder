import math

n = int(input())
word_list = []
for _ in range(n):
    word_list.append(str(input()))
for i, word in enumerate(word_list):
    # 各文字列をソート
    word_list[i] = ''.join(sorted(word))
# 全体をソート
word_list = sorted(word_list)+['']
temp_str = ''
temp_count = 1
result_count = 0
for word in word_list:
    if temp_str == word:
        temp_count += 1
    else:
        if temp_count > 1:
            # 組み合わせの計算
            result_count += math.factorial(temp_count) // (math.factorial(temp_count - 2) * 2)
        temp_count = 1
    temp_str = word
print(result_count)