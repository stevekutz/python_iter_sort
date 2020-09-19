def split_and_join(line):
    # write your code here
    line = line.split(' ')
    line = '-'.join(line)
    print(line)

#  split_and_join("this is a string")    

s = 'hello world'
def solve(s):
    S = ''
    for item in s:
        s += item.title()
    return S    
print(solve(s))    