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

        # sizes
        self.size = {
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

    # use class methods as FACTORY FUNCTIONS(function that creates another obj) EVERYTHING in Python is an obj
    @classmethod
    def margherita(cls):
        return cls(['mozerella', 'tomatoes'])     

    @classmethod
    def prosciutto(cls):
        return cls(['mozerella', 'tomatoes', 'ham']) 


    def get_size_diam(self):
        return self.static_size('size')

    # Will cause error when run with print(p.static_size('L'))
    # NameError: name 'size' is not defined    
    # @staticmethod
    # def static_size(size_key):
    #     return size[size_key]

    # This can access class variables
    # 
    def instance_size(self, size_key):
        return self.size[size_key]



# print(PizzaClass.margherita())
# print(PizzaClass.prosciutto())           

print(PizzaClass.margherita())   # reprPizza (['mozerella', 'tomatoes'], size: {'S': '8 inch', 'M': '12 inch', 'L': '16 inch', 'XL': '20 inch'}  )
# p = PizzaClass(['mushrooms, sausage', 'L'])
# print(p.static_size('L'))

print(p.instance_size('L'))    # 16 inch