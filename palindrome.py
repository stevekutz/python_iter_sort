# def is_palindrome(val):
          
#     d = 0; s = 0;  
#     temp = val; 
#     while (val > 0) :  
    
#         d = val % 10;  # find remainder
#         s = s * 10 + d;   
#         val = val // 10;  
    
#         print(f' d: {d}   s: {s}  val {val} ')
#     # If n is equal to its reverse,  
#     # it is a palindrome  
#     print(f' for {val}   result: {s == temp} ')
#     return s == temp;


# is_palindrome(2112)  # True 
# is_palindrome(100101001) # True
# is_palindrome(234532) # False
# is_palindrome(88)    # True
# is_palindrome(2)     # True


# def is_palindrome_2(string):
#     if type(string) != "str":
#         if type(string) == 'int':
#             string = str(string)
#         else:
#             return f' input mustbe string or integer'    
#     from re import sub
#     s = sub('[\W_]', '', string.lower())
#     print(f' val {string} palindrome check is {s}')
#     return s == s[::-1]

# is_palindrome_2(2112)  # True 
# is_palindrome_2(100101001) # True
# is_palindrome_2(234532) # False
# is_palindrome_2(88)    # True
# is_palindrome_2(2)     # True    

s = "sferesd"
i = 10
print(type(s))
print(type(i))

def check_type(val):
    if type(val) ==  str:
        print(f' string type')


check_type(s)