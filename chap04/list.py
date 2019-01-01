for x in [3, 2, 1, 0]:
    print(x)

y = [number for number in range(10) if number % 2 == 0]
print(y)

squares = {x: x*x for x in range(10)}
print(squares)

odd = {number for number in range(10) if number % 2 == 1}
print(odd)

for num in ('Got %s' % number for number in range(10)):
    print(num)

def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

def get_odds():
    for num in range(1, 10, 2):
        yield num

for count, num in enumerate(get_odds(), 1):
    if count == 3:
        print("The third odd number is", num)
        break

def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print("Greeting, Earthling")

greeting()

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)
