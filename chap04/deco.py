def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional argsuments:', args)
        print('Keyword argument:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

@document_it
def add_ints(a, b):
    return a + b
print(add_ints(3, 5))

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, *kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)

@square_it
@document_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)

