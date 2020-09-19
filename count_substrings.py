S = 'ABCDCACDFCDCECDCDCAAAAB'
sub = 'CDC'


def count_sub(string, sub_string):
    indices = []
    index = 0
    count = 0

    # for i in range(len(string) - 1):
    #     print(f' at {i}  ch is string[i]')

    while index < len(string):
        ind = string.find(sub_string, index)
        if ind == -1:
            break
        indices.append(ind)
        index = ind + 1    
        count += 1
        
    print(f' length of indices {len(indices)} ')
    print(f' indices are are  {indices}')
    print(f' count is {count}')

    return indices

print(count_sub(S, sub))