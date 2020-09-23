def is_palindrome(val):
          
    d = 0; s = 0;  
    temp = val; 
    while (val > 0) :  
    
        d = val % 10;  # find remainder
        s = s * 10 + d;   
        val = val // 10;  
    
        print(f' d: {d}   s: {s}  val {val} ')
    # If n is equal to its reverse,  
    # it is a palindrome  
    print(f' result: {s == temp} ')
    return s == temp;


is_palindrome(2112)
# is_palindrome(100101001)