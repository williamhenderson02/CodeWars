#my one liner solution
def create_phone_number(n):

    return "(" + ''.join(str(x) for x in n[0:3]) + ") " + ''.join(str(y) for y in n[3:6]) + '-' + ''.join(str(z) for z in n[6:10])

n = [1,2,3,4,5,6,7,8,9,0]

number = create_phone_number(n)

print(number)