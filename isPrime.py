#my solution
def is_prime(num):

    try:

        return (len([x for x in range(2, int(num**0.5) + 1) if num % x == 0]) == 0) and num > 1

    except:

        return False

num = 8

valid = is_prime(num)

print(valid)