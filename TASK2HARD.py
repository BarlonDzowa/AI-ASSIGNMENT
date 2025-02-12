import time
import random

# Defining the building structure (floors and rooms along a corridor)
MUBAS_Building = {
    "First Floor": {30: "dirty", 31: "clean", 32: "dirty", 33: "dirty", 34: "clean"},
    "Second Floor": {40: "clean", 41: "dirty", 42: "dirty", 43: "clean", 44: "dirty"},
    "Third Floor": {45: "dirty", 46: "clean", 47: "clean", 48: "dirty", 49: "clean"}
}

# Timetable of room usage (1 means class in progress, 0 means available)
room_timetable = {
    30: 0, 31: 1, 32: 0, 33: 1, 34: 0,
    40: 1, 41: 0, 42: 1, 43: 0, 44: 0,
    45: 0, 46: 1, 47: 0, 48: 1, 49: 0
}


class VacuumCleaner:
    def __init__(self, building, difficulty="Easy"):
        self.building = building
        self.difficulty = difficulty
        self.cleaned_rooms = 0
        self.total_rooms = sum(len(rooms) for rooms in building.values())

    def delay(self, duration=1):

        time.sleep(duration)

    def randomize_dirt(self):

        for floor, rooms in self.building.items():
            for room in rooms:
                # 50% chance of getting dirty again
                if random.choice([True, False]):
                    rooms[room] = "dirty"

    def is_room_available(self, room):
        """ Check if the room is available for cleaning """
        return room_timetable.get(room, 0) == 0

    def clean_room(self):
        while True:
            for floor, rooms in self.building.items():
                print(f"Now at {floor}")
                for room, status in rooms.items():
                    print(f"Moving to Room {room}", end="")
                    self.delay(1)

                    if not self.is_room_available(room):
                        print(f"\nRoom {room} is currently in use. Skipping...")
                        continue

                    print(f"\nChecking Room {room}...")

                    if status == "dirty":
                        print(f"Room {room} is dirty. Cleaning now...", end="")
                        self.delay(2)
                        rooms[room] = "clean"
                        self.cleaned_rooms += 1
                        print(f"\nRoom {room} is now clean!")
                    else:
                        print(f"Room {room} is already clean.")

                    print(f"Moving out of Room {room} back to corridor...\n")
                print("=" * 50)

                # For Medium and Hard levels, introduce random dirt
                if self.difficulty in ["Medium", "Hard"]:
                    self.randomize_dirt()
                    print("SOME ROOMS MAY HAVE BECOME DIRTY AGAIN !!!!!!!")
                    print("-" * 50)

            print(f"!!!!!!!!!!!!!! CLEANING COMPLETE!!!!!!!!!! {self.cleaned_rooms}/{self.total_rooms} ROOMS CLEANED. MOVING BACK TO THE FIRST ROOM...")
            # Pause before restarting the cycle
            time.sleep(10)

difficulty_level = "Medium"

vacuum_robot = VacuumCleaner(MUBAS_Building, difficulty_level)
vacuum_robot.clean_room()
