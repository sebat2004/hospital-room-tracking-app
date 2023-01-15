from time import sleep

class Room():
    def __init__(self, room_number, current_status="Available"):
        self.room_number = room_number
        self.current_status= current_status
        self.patient_type = ""
        self.timer = 0
        self.timer_on = False
    
    def usage_timer(self):
        if self.patient_type == "Ambulatory":
            self.timer = 60
        elif self.patient_type == "Non-Ambulatory":
            self.timer = 30
        else:
            self.timer = 45
        return self.timer

