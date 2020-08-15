# sort flatten list of list  
# using sorted + list comprehension 
  
# initializing list of list  
test_list = [[3, 5], [7, 3, 9], [1, 12]] 
  
# printing original list of list  
print("The original list : " + str(test_list)) 
  
# using sorted + list comprehension 
# sort flatten list of list 
res = sorted([j for i in test_list for j in i]) 
  
# print result 
print("The sorted and flattened list : " + str(res))