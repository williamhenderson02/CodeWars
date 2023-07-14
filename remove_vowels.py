#my solution
def disemvowel(string_):
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    for i in vowels:

        string_ = string_.replace(i, "")

    return string_

string_ = 'Hello, LOL'

removed = disemvowel(string_)

print(removed)

