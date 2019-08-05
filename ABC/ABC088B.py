# coding:utf-8

_ = input()
card_list = [int(x) for x in input().split(' ')]

card_list.sort(reverse=True)

alice_score = 0
bob_score = 0

for i, card in enumerate(card_list):
    if not i % 2:
        alice_score += card
    else:
        bob_score += card

print(alice_score - bob_score)