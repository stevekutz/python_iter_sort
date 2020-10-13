from collections import Counter
from random import randint

nums = [1,3,4,2,2]
dups = set()

counts = Counter(nums)

print(counts)

# for item in counts.items():
#     if item[1] > 1:
#         print(f' we got a duplicate at {item[0]}' )
#     print(f' item is {item}  item[0] is {item[0]}   item[1] is {item[1]}')

for item in nums:
    if item not in dups:
        dups.add(item)
    else:
        print(f' dup item is {item}')   
        break 



###  generate some long lists of random nums
list_nums = []


## the _ is not important enough to define in a variable to be used inside the for loop, therefore, loop just repeats 100 times
for _ in range(100):
        list_nums.append(randint(0, 10))

counts_2 = Counter(list_nums)        
print(f' counts_2 is {counts_2}')

most_comm = Counter(list_nums).most_common(1)

print(f' most common is {most_comm[0][0]} with count of {most_comm[0][1]} ')

# print(f' elements in counts_2 : {list(counts_2.elements())}')

# #  list comprehension from counts_2
# list_counts2 = list(x for x in counts_2.elements())
# print(f' list_counts_2 {list_counts2}')

# for i in range(101):
#     print(f' list_nums[i] {list_nums[i]}     list_counts2[i] {list_counts2[i]}')
# list_nums[i] 5     list_counts2[i] 5       .elements groups similar items together
#  list_nums[i] 7     list_counts2[i] 5
#  list_nums[i] 4     list_counts2[i] 5
#  list_nums[i] 9     list_counts2[i] 5
#  list_nums[i] 3     list_counts2[i] 5
#  list_nums[i] 9     list_counts2[i] 5
#  list_nums[i] 4     list_counts2[i] 5
#  list_nums[i] 5     list_counts2[i] 5
#  list_nums[i] 8     list_counts2[i] 5
#  list_nums[i] 0     list_counts2[i] 5
#  list_nums[i] 2     list_counts2[i] 5
#  list_nums[i] 0     list_counts2[i] 7
#  list_nums[i] 1     list_counts2[i] 7
#  list_nums[i] 2     list_counts2[i] 7
#  list_nums[i] 5     list_counts2[i] 7
# ...........