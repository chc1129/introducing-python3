def do_nothing():
    pass

do_nothing()

def make_a_sound():
    print('quack')

make_a_sound()

def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected,')

def echo(anything):
    return anything + ' ' + anything

echo('Rumplestiltskin')

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only beess can see it."
    else:
        return "I've never heard of the color " + color + "."

comment = commentary('blue')
print(comment)
print(do_nothing())

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
print(menu('beef', 'bagel', 'bordeaux'))
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print(menu('frontenac', dessert='flan', entree='fish'))

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'doughnut'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

print(buggy('a'))
print(buggy('b'))

def works(arg):
    result = []
    result.append(arg)
    return result

print(works('a'))
print(works('b'))

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

print(nonbuggy('a'))
print(nonbuggy('b'))

def print_args(*args):
    print('Positional argument tuple:', args)

print_args()

print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

#def echo(anything):
#    'echoは,与えられた入力引数引数を返す'
#    return anything
#
#help(echo)
#print(echo.__doc__)

def answer():
    print(42)

answer()

def run_something(func):
    func()

run_something(answer)
type(run_something)

def add_args(arg1, arg2):
    print(arg1 + arg2)

type(add_args)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_args, 1, 2, 3, 4)

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(4, 7)

