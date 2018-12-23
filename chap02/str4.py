todos = 'get gloves,get mask,give cat vitamins, call ambulance'
print(todos.split(','))
print(todos.split())
print()

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid whitch is moist and wet
Fire that property can never get.
Then 'tis no cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))
word = 'the'
print(poem.find(word))
print(poem.rfind(word))
print(poem.count(word))
print(poem.isalnum())

setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(39))
print(setup.replace('duck', 'marmoset'))
print(setup.replace('a ', 'a famous ', 100))
print(setup.replace('a', 'a famous', 100))
