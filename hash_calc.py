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
       '~' : operator.inv, 
        }


def math_op(val_a, val_b, op = None):
    if op != None:      
        result =  ops[op](val_a, val_b)
        # return f' {val_a} {ops[op]} {val_b}'
        return result

    print(f'\n Do all ops')
    for k in ops.keys():
        if k == '~':
            print(f'{str(ops[k]).split()[-1][:-1]} : {k} {val_a} = {ops[k](val_a)}')
        else:    
            print(f'{str(ops[k]).split()[-1][:-1]} :  {val_a} {k} {val_b} =  {ops[k](val_a, val_b)}')


# print(math_op(2, 4, '+'))    # 6  
# print(math_op(2, 4, '-'))    # -2
# print(math_op(2, 4, '*'))    # 8   

math_op(2,4)

