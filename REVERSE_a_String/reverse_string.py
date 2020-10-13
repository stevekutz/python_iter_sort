str_val = "Hello"

####################################################
# # Basic for loop to append ch to start of new string
# def reverse(x):
#     sol = ''
#     for ch in str_val:
#         # sol += ch     >> same as sol = sol + ch  >> just copies string
#         sol = ch + sol  # appends like sol = e + H >>> sol = eH  
#     return sol

# # print(reverse(str_val))    # olleH

# ####################################################
# # Using recursion
# def reverse_r(x):

#     # end condition
#     if len(x) == 0:
#         return x

#     else:
#         print(f' x[1:]>> {x[1:]}  +  x[0] {x[0]}')
#         return reverse_r( x[1:]) + x[0]

# print(reverse_r(str_val))        
# #  x[1:]>> ello  +  x[0]>> H = Hello
# #  x[1:]>> llo  +  x[0]>> e = ello
# #  x[1:]>> lo  +  x[0]>> l = llo
# #  x[1:]>> o  +  x[0]>> l = lo
# #  x[1:]>>   +  x[0]>> o = o
# # olleH








####################################################
# reverse a string using a stack 

# # Function to create an empty stack. It 
# # initializes size of stack as 0 
# def createStack(): 
# 	stack=[] 
# 	return stack 

# # Function to determine the size of the stack 
# def size(stack): 
# 	return len(stack) 

# # Stack is empty if the size is 0 
# def isEmpty(stack): 
# 	if size(stack) == 0: 
# 		return True 

# # Function to add an item to stack . It 
# # increases size by 1	 
# def push(stack,item): 
# 	stack.append(item) 

# # Function to remove an item from stack. 
# # It decreases size by 1 
# def pop(stack): 
# 	if isEmpty(stack): return
# 	return stack.pop() 

# # A stack based function to reverse a string 
# def reverse_s(string): 
# 	n = len(string) 
	
# 	# Create a empty stack 
# 	stack = createStack() 

# 	# Push all characters of string to stack 
# 	for i in range(0,n,1): 
# 		push(stack,string[i]) 

# 	# Making the string empty since all 
# 	# characters are saved in stack	 
# 	string = "" 

# 	# Pop all characters of string and put 
# 	# them back to string 
# 	for i in range(0,n,1): 
# 		string += pop(stack) 
# 		print(f' {i} {string}' )
# 	return string 

# print(reverse_s(str_val))



####################################################
## reverse string using extended slice syntax 

## Function to reverse a string 
# def reverse_sl(string): 
# 	return string[::-1] 
# 	# return string 

# print(reverse_sl(str_val))   # olleH



# ###################################################
# reverse a string using reversed()  as iterator

# Function to reverse a string 
# ### SEPARATOR.join(LIST_NAME) merges contents of a list into a string
# ### reversed()
# reversed() doesn't actually reverse anything, it merely returns the reversed iterator object  
# that can be used to iterate over the container's elements in reverse order.

def reverse_f(string):
    print(f' not joined    {list(reversed(s))}')
    string = "".join(reversed(string)) 
    return string 

    # just returns function obj
    # sol =  reversed(string)
    # return sol


s = "Hello"
print(reverse_f(s))   # olleH

print(f' reversed iterator object returned    {reversed(s)}') 

####################################################
# # reverse a string using a list comprehension
# str_val = "".join(list(x for x in reversed(str_val)))
# print(str_val)    # olleH