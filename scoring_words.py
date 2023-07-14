#my solution 
"""def high(x):

    highest = ''

    text = x.split()

    maxi = 0

    for word in text:
        total = 0
        for char in word:
            num = ord(char) - 96
            total = total + num
            if total > maxi:
                highest = word
                maxi = total

    return highest

x = 'what time are we climbing up the volcano'

highest = high(x)

print(highest)"""

#best solution
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


x = 'what time are we climbing up the volcano'

highest = high(x)

print(highest)