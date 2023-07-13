def comp(a, b):

    new_list = [x for x in a if x**2 in b]
    
    if len(new_list) == len(a):
        return True

    else:
        return False

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

same = comp(a,b)

print(same)