# Function calling 
def dictionary(): 
# Declare hash function	 
    key_value ={}	 

# Initializing value 
    key_value[2] = 56	
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18	
    key_value[3] = 323

    print ("Task 1:-\n") 
    print ("Keys are") 

    # iterkeys() returns an iterator over the 
    # dictionary’s keys. 
    for i in sorted (key_value.keys()) : 
        # print(i, end = " ") 
        print(f' i is {i}')

# def main(): 
# 	# function calling 
# 	dictionary()			 
	
# # Main function calling 
# if __name__=="__main__":	 
# 	main() 

dictionary()