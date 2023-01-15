class HouseKeeper:
    def __init__(self, employee_id, name, status="AVAILABLE"):
        self._employee_id = employee_id
        self._name = name
        self._status = status  # Can be marked: 'AVAILABLE', 'BUSY', 'ON_BREAK'
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
        room._house_keeper_assigned = self._employee_id


class Room:
    def __init__(self, room_number, room_status="CLEAN", room_availability="AVAILABLE"):
        self.room_number = room_number 
        self.room_status = room_status # Can be marked 'CLEAN', 'DIRTY', 'FILTHY'
        self.room_availability = room_availability # Either 'AVAILABLE', 'RF-CLEANING', 'CLEANING', or 'OCCUPIED'
        self.timer = 0
        self._house_keeper_assigned = None
        
    def usage_timer(self):
        if self.room_status == "FILTHY":
            self.timer = 20
        elif self.room_status == "DIRTY":
            self.timer = 10
        return self.timer

    def get_room_number(self):
        return self.room_number

    def set_house_keeper_assigned(self, house_keeper):
        """Sets the house_keeper assigned to clean the room"""
        self._house_keeper_assigned = house_keeper

    def get_update(self):
        """Returns ETA and Housekeeper who will be cleaning the room."""
        return f"Room {self.room_number} is being cleaned by {self._house_keeper_assigned} and will be done in {self.timer} seconds."

    def get_assigned_house_keeper(self):
        return self._house_keeper_assigned

    def get_room_status(self):
        return self.room_status

    def set_timer(self, time):
        self.timer = time


class Hospital:
    def __init__(self):
        self._house_keepers = []
        self._rooms = []

    def add_house_keeper(self, house_keeper):
        """Adds a HouseKeeper object to the Hospital's house_keepers list."""
        if len(self._house_keepers) == 0:
            return self._house_keepers.append(house_keeper)     
        for keeper in self._house_keepers:
            if house_keeper._employee_id == keeper._employee_id:
                return "ID in use"
        self._house_keepers.append(house_keeper)  
        print("worked")
        return f"Housekeeper {house_keeper._employee_id} added"     
        

    def remove_house_keeper(self, house_keeper):
        """Removes a HouseKeeper object from the Hospital's house_keepers list."""
        return self._house_keepers.remove(house_keeper)

    def add_room(self, room):
        """Adds a Room object to the hospital."""
        self._rooms.append(room)

    def remove_room(self, room):
        """Removes a Room object from the Hospital's rooms list."""
        self._rooms.remove(room)

    def request_room_cleaning(self, room):
        """Finds an available house_keeper and sets their room assignment"""
        for house_keeper in self._house_keepers:
            if house_keeper._status == 'AVAILABLE':
                room.set_house_keeper_assigned(house_keeper)
                room.room_availability == "RF-CLEANING"
                house_keeper.set_room_assigned = room
                house_keeper.set_employee_status = 'BUSY'
                return "Room Assignment Successful!"
        return "There are no available house keepers"  # Figure out a queue system for if all keepers are busy that gives time frame of arrival of next HK

    def cleaning_beginning(self, room_number, time=0):
        """Gives estimated time of completion, time chosen based on room condition if time is not entered."""
        for room in self._rooms:
            if room.room_number == room_number and room.room_availability == "RF-CLEANING":
                if time == 0:
                    room.room_availability = 'CLEANING'
                    if room.get_room_status() == 'DIRTY':
                        room.timer = 10
                        return
                    elif room.get_room_status() == 'FILTHY':
                        room.timer = 10
                        return
                elif time != 0:
                    room.timer = time
        return "Room is being cleaned"

    def cleaning_complete(self, room):
        """Sets room as 'CLEAN' and house keeper as 'AVAILABLE', removes house keeper assignment """
        room.room_status = 'CLEAN'
        room.room_availability = 'AVAILABLE'
        house_keeper = room.get_assigned_house_keeper()
        room.set_house_keeper_assigned(None)
        house_keeper._room_assigned = None
        house_keeper._status = 'AVAILABLE'
        room.set_timer(0

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
