def multiply_strings(an_integer : int, a_string : str) :
    
    output_string = ""
    for i in range(0, an_integer) :
        output_string += a_string
    
    return output_string

class MyAwesomeClass :
    def __init__(self, name : str, surname : str, age : int) :
        self.name = name
        self.surname = surname
        self.age = age
        
    def greet(self) :
        my_string = "Hello! My name is %s %s, and I am %d years old!" % (self.name, self.surname, self.age)
        return my_string
    
    #def __str__(self) : # try implementing this!