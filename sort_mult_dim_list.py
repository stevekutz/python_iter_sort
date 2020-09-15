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
