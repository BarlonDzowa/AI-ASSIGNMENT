# TASK 1

rooms = {"A": "clean", "B": "dirty"}


def roomA():
    print("now in Room A")
    print("Checking Room A")
    if rooms["A"] == "dirty":
        print("Room A is dirty")
        rooms["A"] = "clean"
        print("Room A is cleaned")

    else:
        print("Room A is clean")
    print("Moving to room B...............................\n\n")


def roomB():
    print("now in Room B")
    print("Checking Room B")
    if rooms["B"] == "dirty":
        print("Room B is dirty")
        rooms["B"] = "clean"
        print("Room B is cleaned")

    else:
        print("Room B is clean")
    # move_right()
    print("Moving to room A...............................\n\n")


def clean_room():
    roomA()
    roomB()


a = 2

while a >= 0:
    clean_room()
    a = a - 1