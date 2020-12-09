str = "Apple"


def reverse_loop(str):

    rev = ''

    for ch in str:
        rev = ch + rev
        # rev += ch  # appends ch to end, will not reverse

    return rev

print(f' revers_loop returns {reverse_loop(str)} \n')   # elppA


count = 0
def reverse_rec(str):

    global count
    print(f' \t str   {str}')

    if len(str) == 0:
        return str

    else:
        print(f' count >> {count}   str {str}   \t str[1:]  {str[1:]}    \t\t str[0]  {str[0]} ')
        # print(f' >>>> reverse_rec(str[1:])  {reverse_rec(str[1:])} ')
        count += 1
        return reverse_rec(str[1:]) + str[0]


print(f' reverse_rec    {reverse_rec(str)}')    