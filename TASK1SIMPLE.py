# TASK 1 EXTENDED

import time


rooms = {"A": "", "B": ""}
# Read file and update dictionary
with open('extract.txt', 'r') as file:
    for line in file:
        status1, status2 = line.strip().split(", ")
        rooms["A"]=status1
        rooms["b"]=status2


        def roomA():
            print("now in Room A")
            print("Checking Room A")
            if rooms["A"] == "dirty":
                print("Room A is dirty")
                rooms["A"] = "clean"
                print("Room A is cleaned")

            else:
                print("Room A is clean")
            print("Moving to room B", end="", flush=True)
            start_time = time.time()
            while time.time() - start_time < 1:
                print(".", end="", flush=True)
                time.sleep(0.1)


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
            print("Moving to room A",end="",flush=True)
            start_time=time.time()
            while time.time()-start_time<1:
                print(".", end="", flush=True)
                time.sleep(0.1)


        def clean_room():
            roomA()
            roomB()
        clean_room()