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
    @staticmethod
    def static_method():
        return f" static_method called"



c = BasicClass()
print(c.instance_method())   # called instance_method at <__main__.BasicClass object at 0x7f9cfba93b20>

print(c.class_method())    # class_method called at <class '__main__.BasicClass'>

print(c.static_method())   # static_method called

######  Without creating class instance
BasicClass.class_method()     # class_method called at <class '__main__.BasicClass'>
BasicClass.static_method()
BasicClass.instance_method()   # TypeError: instance_method() missing 1 required positional argument: 'self'