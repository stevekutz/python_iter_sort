class BasicClass:
    # self points to INSTANCE of BasicClass and allows access to all attributes & methods
    # using self, the instance method can modify state on the object instance as well as the class itself
    def instance_method(self):   # self is just convention
        return f"called instance_method at {self}"


    # uses the `cls` parameter instead of self so as to refer to the class NOT the instance when called
    # can modify `class state` but not `instance state`
    @classmethod
    def class_method(cls):    # cls is just convention
        return f" class_method called at {cls}"



    # does not use `self` OR `cls` but can take any other parameters
    # CANNOT modify instance or class state, isolated
    @staticmethod
    def static_method():
        return f" static_method called"



# c = BasicClass()
# print(c.instance_method())   # called instance_method at <__main__.BasicClass object at 0x7f9cfba93b20>

# print(c.class_method())    # class_method called at <class '__main__.BasicClass'>

# print(c.static_method())   # static_method called

######  Without creating class instance
# BasicClass.class_method()     # class_method called at <class '__main__.BasicClass'>
# BasicClass.static_method()
# BasicClass.instance_method()   # TypeError: instance_method() missing 1 required positional argument: 'self'


class PizzaClass:
    def __init__(self, ingredients, size = None):
        self.ingredients = ingredients
        self.size = size

        # sizes
        self.size_init = {
                        'S' : '8 inch',
                        'M' : '12 inch',
                        'L' : '16 inch',
                        'XL' : '20 inch'
                    }

    # def __str__(self):
    #     return f' strPizza ({self.ingredients})'

        # cannot print within __str__  ONLY use return
        # for item in self.ingredients:
        #     print(f' \t {item}')   # TypeError: __str__ returned non-string (type NoneType)


    # By default, f-strings will use __str__(), 
    # but you can make sure they use __repr__() if you include the conversion flag !r
    #  AND commenting out __str__ ()
    def __repr__(self):
        return  f' reprPizza ({self.ingredients!r}, size: {self.size}  )'   

    # use class methods as FACTORY FUNCTION(function that creates another obj) EVERYTHING in Python is an obj
    @classmethod
    def margherita(cls):
        # following line will cause error  >> name 'size_init' is not defined
        # classmethod cannot see instance variable size_init
        # print(f' classmethod can size size_init  {size_init}')
        
        print(f' Our Marherita pizza has:')
        return cls(['mozerella', 'tomatoes'])     

    @classmethod
    def prosciutto(cls):
        return cls(['mozerella', 'tomatoes', 'ham']) 

    

    # This can access class variables
    # 
    def instance_size(self, size_key):
        print(f'___  in instance_size ')
        return self.size_init[size_key]

    # this should access static_size
    def get_size_diam2(self):
        print(f'  in get_size_diam2, passsing  {self.size} to static_size staticmethod')
        return self.static_size(self.size)

    def add_ingredient(self, new_ingredient):
        self.ingredients.append(new_ingredient)

        # upper_now = self.uppercase_ingredient(new_ingredient)
        # upper_now = PizzaClass.uppercase_ingredient(self, new_ingredient)
        upper_now = PizzaClass.uppercase_ingredient(PizzaClass, new_ingredient)

        self.ingredients.append(upper_now)
        print(f' ingredients now {self.ingredients}')
        return self.ingredients

    def uppercase_ingredient(self, str_val):
        return str_val.upper()

    @staticmethod
    def static_size(size_key):
        print(f' \t in static_method with passed in {size_key}')

        # sizes
        static_size =  {
                            'S' : '8 inch',
                            'M' : '12 inch',
                            'L' : '16 inch',
                            'XL' : '20 inch'
                        }



        return static_size[size_key]

        # this will cause >>  NameError: name 'init_size' is not defined  
        # static method cannot see instance variables
        # return init_size[size_key] 

# print(PizzaClass.margherita())   # reprPizza (['mozerella', 'tomatoes'], size: {'S': '8 inch', 'M': '12 inch', 'L': '16 inch', 'XL': '20 inch'}  )
# p = PizzaClass(['mushrooms, sausage'], 'L')
p = PizzaClass(['mushrooms, sausage'], 'L')
print(p.static_size('XL'))   # 20 inch    >> Will call static with param `XL` regardless of class OR instance state

print(p.instance_size('L'))    # 16 inch  >> this can access the instance variable `size_init`
print(p.get_size_diam2())      # instance method can access instance state and pass that into staticmethod
#   in get_size_diam2, passsing  L to static_size staticmethod
#          in static_method with passed in L
# 16 inch

print(PizzaClass.margherita()) # reprPizza (['mozerella', 'tomatoes'], size: None  )


print(p.add_ingredient('Octupus'))
