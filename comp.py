#my solution
"""def comp(a, b):

    if a is None or b is None or len(a) != len(b):
        return False
        
    count_a = {}
    count_b = {}

    for num in a:
        count_a[num] = count_a.get(num, 0) + 1

    for num in b:
        count_b[num] = count_b.get(num, 0) + 1

    for num in count_a:
        if num ** 2 not in count_b or count_a[num] != count_b[num ** 2]:
            return False

    return True

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

same = comp(a,b)

print(same)"""