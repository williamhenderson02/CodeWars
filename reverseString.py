#my solution and best solution
def solution(string):

    #this annotation means start at the end of the string and end at the front moving left
    return string[::-1]

string = "hello"

newString = solution(string)

print(newString)