#my solution 
"""def find_it(seq):

    result = 0

    for num in seq:
        result ^= num

    return result

seq = [1,1,2,3,3]

odd = find_it(seq)

print(odd)"""

#best solution
def find_it(seq):

    for i in seq:

        if seq.count(i)%2!=0:

            return i
            
seq = [1,1,2,3,3]

odd = find_it(seq)

print(odd)