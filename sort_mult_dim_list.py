# mlist = [[1, 2], [4, 5], [3, 6]]
mlist = [[1, 2, 5], [4, 5, 0], [3, 6, 8]]



##############  use itemgetter
from operator import itemgetter

mdict = {}
sort_list = []

# for i in range(len(mlist)):

#     mdict[i] = mlist[i] , mlist[i][0]



#####   sort by smallest value from each list within list
def sort_multdim_list(list, sort_index):

    for i in range(len(mlist)):
        mdict[i] = sorted(mlist[i]) , mlist[i][0]

    print(f' mdict  {mdict}  ')

    # temp_sort = sorted(mdict.items(), key = lambda x: x[sort_index])
    temp_sort = sorted(mdict.items(), key = itemgetter(sort_index))

    print(f'temp_sort {temp_sort}')

    for item in temp_sort:
        print(item[sort_index][0])
        sort_list.append(item[sort_index][0])


sort_multdim_list(mlist, 1)

print(f' sort_list   {sort_list} ')


def sort_mult_dim_list_2(list, sort_index):
    return sorted(list, key = itemgetter(sort_index))


mlist = [[1, 2, 5], [4, 5, 0], [3, 6, 8]]
print(sort_mult_dim_list_2(mlist, 0))
# [[1, 2, 5], [3, 6, 8], [4, 5, 0]]

print(sort_mult_dim_list_2(mlist, 1))
# [[1, 2, 5], [4, 5, 0], [3, 6, 8]]

print(sort_mult_dim_list_2(mlist, 2))
# [[4, 5, 0], [1, 2, 5], [3, 6, 8]]



# sort by lowest val in each list within list
def sort_mult_dim_list_3(list):
    
    temp_list = []
    for item in list:
        temp_list.append(sorted(item))

    print(temp_list)    

    return sorted(temp_list, key = itemgetter(0))

print(f' ver3 {sort_mult_dim_list_3(mlist)}\n')



print(f' mlist is {mlist}')
sort4 = list(item for item in sorted(mlist, key = lambda index: index[0]))
# sort4 = list( item for item in sorted(mlist, key = itemgetter(0)) )
print(f' by index 0 {sort4}') # ver 4 [[1, 2, 5], [3, 6, 8], [4, 5, 0]]

sort4 = list(item for item in sorted(mlist, key = lambda index: index[1]))
#sort4 = list( item for item in sorted(mlist, key = itemgetter(1)) )
print(f' by index 1 {sort4}') # ver 4 [[1, 2, 5], [4, 5, 0], [3, 6, 8]

sort4 = list(item for item in sorted(mlist, key = lambda index: index[2]))
# sort4 = list( item for item in sorted(mlist, key = itemgetter(2)) )
print(f' by index 2 {sort4}') # ver 4 [[4, 5, 0], [1, 2, 5], [3, 6, 8]]


mlist = [[3, 2, 9], [2, 1, 0], [4, 1, 2, 0]]
print(f' \n\nsort each list within {[sorted(item) for item in mlist]}')
# sort by lowest list val in a list of lists
sort_5 = sorted([sorted(item) for item in mlist])
print(f' sort by lowest within each list {sort_5}' )
# [0, 1, 2], [0, 1, 2, 4], [2, 3, 9]]

# Sorted will sort by first value in sublist
new_list = sorted(mlist)
print(f' new_list  {new_list} ')  # [[2, 1, 0], [3, 2, 9], [4, 1, 2, 0]]