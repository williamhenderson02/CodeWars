#my attempt
"""def maskify(cc):

    appStr = ""

    if len(cc) > 4:

        length = len(cc) - 4

        for i in range(length):

            appStr = appStr + '#'

        shortened = cc[-4:]
    
        cc = appStr + shortened

    return cc

cc = 'William'

cc = maskify(cc)

print(cc)"""

#best solution
def maskify_(cc):

    #return a string of '#' multiplied by 4 less than the length of cc concatenated with the last 4 characters of cc
    return "#"*(len(cc)-4) + cc[-4:]

cc = 'William'

cc = maskify_(cc)

print(cc)