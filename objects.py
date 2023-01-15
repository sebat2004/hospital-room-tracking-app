from time import sleep


class HouseKeeper:
    def __init__(self, employee_id, name):
        self._employee_id = employee_id
        self._name = name
        self._status = 'AVAILABLE'  # Can be marked: 'AVAILABLE', 'BUSY', 'ON_BREAK'
        self._room_assigned = None

    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._employee_id

    def get_employee_status(self):
        return self._status

    def set_employee_status(self, status):
        """Allows employee to be marked as 'AVAILABLE', 'BUSY', 'ON_BREAK'"""
        self._status = status

    def set_room_assigned(self, room):
        self._room_assigned = room



class Room:
    def __init__(self, room_number, room_status="CLEAN"):
        self.room_number = room_number
        self.room_status = room_status   # Can be marked 'CLEAN', 'DIRTY', 'FILTHY'
        # self.patient_type = ""
        self.timer = 0
        self.timer_on = False
        self._house_keeper_assigned = None
    
    # def usage_timer(self):
    #     if self.patient_type == "Ambulatory":
    #         self.timer = 60
    #     elif self.patient_type == "Non-Ambulatory":
    #         self.timer = 30
    #     else:
    #         self.timer = 45
    #     return self.timer

    def get_room_number(self):
        return self.room_number

    def set_house_keeper_assigned(self, house_keeper):
        """Sets the house_keeper assigned to clean the room"""
        self._house_keeper_assigned = house_keeper

    def get_update(self):
        """Returns ETA and Housekeeper who will be cleaning the room."""
        if self._house_keeper_assigned:
            return f"Room {self.room_number} will be cleaned by {self._house_keeper_assigned.get_name()} " \
                   f"and be done in {self.timer} minutes."
        else:
            return "Room is cleaned and ready for the next patient."

    def get_assigned_house_keeper(self):
        return self._house_keeper_assigned

    def get_room_status(self):
        return self.room_status

    def set_room_status(self, status):   # Can be marked 'CLEAN', 'DIRTY', 'FILTHY'
        self.room_status = status

    def set_timer(self, time):
        self.timer = time


class Hospital:
    def __init__(self):
        self._house_keepers = []
        self._rooms = []

    def add_house_keeper(self, house_keeper):
        """Adds a HouseKeeper object to the Hospital's house_keepers list."""
        self._house_keepers.append(house_keeper)

    def remove_house_keeper(self, house_keeper):
        """Removes a HouseKeeper object from the Hospital's house_keepers list."""
        self._house_keepers.remove(house_keeper)

    def add_room(self, room):
        """Adds a Room object to the hospital."""
        self._rooms.append(room)

    def remove_room(self, room):
        """Removes a Room object from the Hospital's rooms list."""
        self._rooms.remove(room)

    def request_room_cleaning(self, room):
        """Finds an available house_keeper and sets their room assignment"""
        if room.get_room_status() == "CLEAN":
            return "Room has already been cleaned!"
        for house_keeper in self._house_keepers:
            if house_keeper.get_employee_status() == 'AVAILABLE':
                room.set_house_keeper_assigned(house_keeper)
                house_keeper.set_room_assigned(room)
                house_keeper.set_employee_status('BUSY')
                return "Room Assignment Successful!"
        else:
            return "There are no available house keepers at this time"  # Figure out a queue system for if all keepers are busy that gives time frame of arrival of next HK

    def cleaning_beginning(self, room_number, time=0):
        """Gives estimated time of completion, time chosen based on room condition if time is not entered."""
        for room in self._rooms:
            if room.get_room_number() == room_number:
                if time == 0:
                    if room.get_room_status() == 'CLEAN':
                        return "Room is already cleaned!"
                    elif room.get_room_status() == 'DIRTY':
                        room.set_timer(30)
                    elif room.get_room_status() == 'FILTHY':
                        room.set_timer(60)
                elif time != 0:
                    room.set_timer(time)

    def cleaning_complete(self, room_number):
        """Sets room as 'CLEAN' and house keeper as 'AVAILABLE', removes housekeeper assignment """
        for room in self._rooms:
            if room.get_room_number() == room_number:
                room.set_room_status('CLEAN')
                house_keeper = room.get_assigned_house_keeper()
                room.set_house_keeper_assigned(None)
                house_keeper.set_room_assigned(None)
                house_keeper.set_employee_status('AVAILABLE')
                room.set_timer(0)






if __name__ == '__main__':


    # hospital = Hospital()
    # r1 = Room(1)
    # r2 = Room(2)
    # r3 = Room(3)
    # hospital.add_room(r1)
    # hospital.add_room(r2)
    # hospital.add_room(r3)
    #
    # hk1 = HouseKeeper(123, 'Eric')
    # hk2 = HouseKeeper(456, 'Sebastian')
    # hk3 = HouseKeeper(789, 'Hannah')
    # hospital.add_house_keeper(hk1)
    # hospital.add_house_keeper(hk2)
    # hospital.add_house_keeper(hk3)
    #
    # r1.set_room_status('FILTHY')
    # print(hospital.request_room_cleaning(r1))
    #
    # hospital.cleaning_beginning(1)
    # print(r1.get_update())
    #
    # hospital.cleaning_complete(1)
    # print(r1.get_update())
    #
    # print(hospital.request_room_cleaning(r1))