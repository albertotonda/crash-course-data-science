from import_this import multiply_strings, MyAwesomeClass

if __name__ == "__main__" :
    my_int = 3
    my_string = "ciao"
    
    print(multiply_strings(my_int, my_string))
    
    person = MyAwesomeClass("Alberto", "Tonda", 43)
    print(person.greet())