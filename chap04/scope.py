animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('insde change_and_print_global:', animal)

print(animal)
change_and_print_global()
print(animal)
