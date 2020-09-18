"""
Merging Two Packages

Given a package with a weight limit `limit` and a list `weights` of item
weights, implement a function `get_indices_of_item_weights` that finds
two items whose sum of weights equals the weight limit `limit`. Your
function will return a tuple of integers that has the following form:


(zero, one)


where each element represents the item weights of the two packages.
_**The higher valued index should be placed in the `zeroth` index and
the smaller index should be placed in the `first` index.**_ If such a
pair doesn’t exist for the given inputs, your function should return
`None`.

Your solution should run in linear time.

Example:

input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""






def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Fixing PR

    index_dict = {}
    result = []
    tup_1 = ()

    # build hashtable with weights
    for i in range(length):
        index_dict[weights[i]] = i

    # print(index_dict)

    # iterate through to find max & min from complement
    for i in range(length):
        current = weights[i]
        complement = limit - current  # could also optimize as >> limit - weights[i]

        if complement in index_dict:
            #print(complement)  
            #result.append(complement)
            # print(i)   
            result.append(i)

    if result:
        # result = sorted(result, reverse = True)
        # return result
        # return sorted(result, reverse = True)

        #  !!!!!!!!    to return a tuple
        tup_1 = tuple(sorted(result, reverse = True))
        return tup_1
    return None   # if nothing found

weights = [9]
print(get_indices_of_item_weights(weights, 1, 9))  # None


weights= [4, 4]
print(get_indices_of_item_weights(weights, 2, 8))   # [1,0]


weights = [ 4, 6, 10, 15, 16 ]  # length = 5, limit = 21
print(get_indices_of_item_weights(weights, len(weights), 21))   # [3,1]