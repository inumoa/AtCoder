C = input()

all_list = 'abcdefghijklmnopqrstuvwxyz'

for i, content in enumerate(all_list):
    if content == C:
        print(all_list[i+1])
        exit()