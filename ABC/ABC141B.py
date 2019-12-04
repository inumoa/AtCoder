s = input()
for i, c in enumerate(s):
    if (i % 2 and c == 'R') or (not i % 2 and c == 'L'):
        print('No')
        exit()
print('Yes')