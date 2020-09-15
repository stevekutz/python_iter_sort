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

#  math_op(2,4)



class My_Math:
    def __init__(self):
        self.ops = ops = {  '+': operator.add,
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

    def math_calc(self, x, y, op = None):
        if type(x) != int or type(y) != int:
            print(f' Invalid Input type: Must be integer ')
            raise Exception(" ERROR: inputs must be integer")
        
        
        if op != None:
            return f' {x} {op} {y} = {self.ops[op](x, y)}'

        print(f' \n  Do all ops in class')
        for k in ops.keys():
            if k == '~':
                print(f'\t{str(ops[k]).split()[-1][:-1]} : {k} {x} = {self.ops[k](x)}')
            elif k == '&' or k == '|':
                print(f'\t{str(ops[k]).split()[-1][:-2]} :  {x} {k} {y} =  {self.ops[k](x, y)}')    
            else:    
                print(f'\t{str(ops[k]).split()[-1][:-1]} :  {x} {k} {y} =  {self.ops[k](x, y)}')


c = My_Math()
#   returns after specified operation
print(c.math_calc(2,4,'+'))
print(c.math_calc(2,4,'*'))

# rusn through all operations on given inputs
c.math_calc(2,4)

# will raise error
# c.math_calc(2.1, 4)
# c.math_calc(2, 4.1)
c.math_calc('a', 'b')