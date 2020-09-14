import operator


ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul, 
       '&': operator.and_,
       '<<' : operator.lshift,
       '>>' : operator.rshift,
       '%' : operator.mod,
       '|' : operator.or_,
       '^' : operator.xor,

        }


def math_op(val_a, val_b, op = None):
    # if op in ops:
        
        result =  ops[op](val_a, val_b)
        # return f' {val_a} {ops[op]} {val_b}'
        return result

    # for k in ops.keys():
    #     return f' {val_a} {op} {val_b} =  {ops[k](val_a, val_b)}  '


print(math_op(2, 4, '+'))    # 6  
print(math_op(2, 4, '-'))    # -2
print(math_op(2, 4, '*'))    # 8   

# print(math_op(2,4))

