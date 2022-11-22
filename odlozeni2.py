import re
hand = 'From: fsdkjfh'

if re.search('^From:', hand):
    print(hand)