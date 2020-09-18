###############################
# # Simple method, not efficient

# Python code to demonstrate 
# return the sum of values of dictionary 
# with same keys in list of dictionary 

from operator import itemgetter 

# Initialising list of dictionary 
ini_dict = [{'a':5, 'b':10, 'c':90}, 
			{'a':45, 'b':78}, 
			{'a':90, 'c':10}] 

# printing initial dictionary 
print ("initial dictionary", str(ini_dict)) 


# sum the values with same keys 
result = {} 
for d in ini_dict: 
	for k in d.keys(): 
		result[k] = result.get(k, 0) + d[k] 


print("resultant dictionary : ", str(result)) 


###################################
# Counter method using collections
# Python code to demonstrate 
# return the sum of values of dictionary 
# with same keys in list of dictionary 

import collections 

# Initialising list of dictionary 
ini_dict = [{'a':5, 'b':10, 'c':90}, 
			{'a':45, 'b':78}, 
			{'a':90, 'c':10}] 

# printing initial dictionary 
print ("initial dictionary", str(ini_dict)) 



# sum the values with same keys 
counter = collections.Counter() 
for d in ini_dict: 
	counter.update(d) 
	
result = dict(counter) 


print("resultant dictionary : ", str(counter)) 


#############################################
# using reduce, Counter, 
# Python code to demonstrate 
# return the sum of values of dictionary 
# with same keys in list of dictionary 

import collections, functools, operator 

# Initialising list of dictionary 
ini_dict = [{'a':5, 'b':10, 'c':90}, 
			{'a':45, 'b':78}, 
			{'a':90, 'c':10}] 


# printing initial dictionary 
print ("initial dictionary", str(ini_dict)) 

# sum the values with same keys 
result = dict(functools.reduce(operator.add, 
		map(collections.Counter, ini_dict))) 

print("resultant dictionary : ", str(result)) 

