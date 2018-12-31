guess_me = 7
start = 1
while True:
    if guess_me > start:
        print("too low")
    elif guess_me == start:
        print("found it!")
        break
    else:
        print("oops")
        break
    start = start + 1
