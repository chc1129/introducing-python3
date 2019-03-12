import threading

def do_this(waht):
    whoami(waht)

def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this,
            args=("I'm function %s" %n,))
        p.start()
