import tkinter
import tkinter.messagebox
import customtkinter
from objects import Hospital, Room, HouseKeeper
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RoomTracker.py")
        self.geometry(f"{1100}x{580}")

        # initialize hospital class
        self.hospital = Hospital()

        # Grid layout
        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1), weight=0)

        # text entry vars
        self.err_msg = customtkinter.StringVar(value="Errors: None")
        self.status_err = customtkinter.StringVar(value="Errors: None")
        self.hk_err = customtkinter.StringVar(value="Errors: None")
        self.def_id = customtkinter.StringVar(value="Enter ID")
        self.def_name = customtkinter.StringVar(value="Enter Name")
        self.def_room_num = customtkinter.StringVar(value="Enter Room Number")

    # page creation functions
    def home_page(self):
        # create navbar
        self.nav_bar("home")

        # create add patient tab
        self.patient_tab = customtkinter.CTkTabview(self, width=250)
        self.patient_tab.grid(row=0, column=1, padx=20, pady=(15, 20), sticky="nsew")
        self.patient_tab.add("Home")
        self.patient_tab.tab("Home").grid_columnconfigure(0, weight=1)

        self.desclabel = customtkinter.CTkLabel(self.patient_tab.tab("Home"), text="Welcome to the Hospital Room Tracking Application!", font=("Arial", 22))
        self.desclabel.grid(row=1, column=0, padx=20, pady=(30,5), sticky="S")

        self.desclabel2 = customtkinter.CTkLabel(self.patient_tab.tab("Home"), text="Please click on a panel on the side to navigate throughout the application", font=("Arial", 22))
        self.desclabel2.grid(row=2, column=0, padx=20, pady=(5, 20), sticky="S")

    def patient_page(self):
        # create navbar
        self.nav_bar("patient")

        # create patient tab
        self.patient_tab = customtkinter.CTkTabview(self, width=250)
        self.patient_tab.grid(row=0, column=1, padx=(20, 20), pady=(15, 20), sticky="nsew")
        self.patient_tab.add("Add Patient")
        self.patient_tab.tab("Add Patient").grid_columnconfigure(0, weight=1)

        self.dropdown_menu = customtkinter.CTkComboBox(self.patient_tab.tab("Add Patient"),
                                                    values=["Ambulatory", "Non-Ambulatory"], width=170)
        self.dropdown_menu.grid(row=0, column=0, padx=20, pady=(100, 5))
        
        self.assign_room_entry = customtkinter.CTkEntry(self.patient_tab.tab("Add Patient"), textvariable=self.def_room_num)
        self.assign_room_entry.grid(row=1, column=0, padx=20, pady=5)
        
        self.add_patient_button = customtkinter.CTkButton(self.patient_tab.tab("Add Patient"), text="Add Patient",
                                                        command= lambda: [self.add_patient(self.dropdown_menu.get())])
        self.add_patient_button.grid(row=2, column=0, padx=20, pady=(40, 5))
        self.create_room_button = customtkinter.CTkButton(self.patient_tab.tab("Add Patient"), text="Create Room",
                                                        command= lambda: [self.create_room()])
        self.create_room_button.grid(row=3, column=0, padx=20, pady=(5, 5))
        
        self.error_display = customtkinter.CTkEntry(self.patient_tab.tab("Add Patient"), textvariable=self.err_msg, state="readonly", width=200)
        self.error_display.grid(row=4, column=0, padx=20, pady=(5, 10))

        # default text
        self.dropdown_menu.set("Select Patient Type")
        self.err_msg.set("Errors: None")
    
    def housekeeper_page(self):
        # create navbar
        self.nav_bar("housekeep")

        housekeep_frame = customtkinter.CTkFrame(self, width=300)
        housekeep_frame.grid(row=0, column=1, padx=20, pady=20)

        # create housekeeping tab
        self.housekeep_tab = customtkinter.CTkTabview(self, width=250)
        self.housekeep_tab.grid(row=0, column=1, padx=(20, 20), pady=(15, 20), sticky="nsew")
        self.housekeep_tab.add("Add Housekeeper")
        self.housekeep_tab.tab("Add Housekeeper").grid_columnconfigure(0, weight=1)

        self.hk_id_entry = customtkinter.CTkEntry(self.housekeep_tab.tab("Add Housekeeper"), textvariable=self.def_id)
        self.hk_id_entry.grid(row=0, column=0, padx=20, pady=(100,5))

        self.hk_name_entry = customtkinter.CTkEntry(self.housekeep_tab.tab("Add Housekeeper"), textvariable=self.def_name)
        self.hk_name_entry.grid(row=1, column=0, padx=20, pady=(5,5))

        self.hk_add_button = customtkinter.CTkButton(self.housekeep_tab.tab("Add Housekeeper"), text="Add Housekeeper", command= self.add_housekeeper)
        self.hk_add_button.grid(row=2, column=0, padx=20, pady=(40,5))

        self.err_entry = customtkinter.CTkEntry(self.housekeep_tab.tab("Add Housekeeper"), textvariable=self.hk_err, state="readonly")
        self.err_entry.grid(row=3, column=0, padx=20, pady=(5,5))

        # default text entry values
        self.def_name.set("Enter name")
        self.def_id.set("Enter ID")
        self.hk_err.set("Errors: None")


    def status_page(self):
        status_frame = customtkinter.CTkFrame(self, width=500)
        status_frame.grid(row=0, column=1, padx=20, pady=20, sticky=customtkinter.N)

        self.nav_bar("status")

        # create visual progress bar for each room 
        if len(self.hospital._rooms) == 0:
            self.empty_label = customtkinter.CTkLabel(status_frame, text="There are currently no rooms created.\n To create a new room, go to the Add Patient tab")
            self.empty_label.grid(row=0, column=0, padx=20,  pady=20)
            return
        displayed_rooms = 0
        for room in self.hospital._rooms:
            self.room_label = customtkinter.CTkLabel(status_frame, text=f"Room # {room.room_number} |", font=("Arial", 20))
            self.room_label.grid(row=displayed_rooms, column=0, padx=10, pady=10)
            if room.room_availability == "AVAILABLE":
                self.new_label = customtkinter.CTkLabel(status_frame, text="Room is available for patients", font=("Arial", 20))
                self.new_label.grid(row=displayed_rooms, column=1, padx=(2,10), pady=10)
            elif room.room_availability == "CLEANING":
                self.timer_label = customtkinter.CTkLabel(status_frame, text=f"{room.timer} seconds until room is finished cleaning", font=("Arial", 20))
                self.timer_label.grid(row=displayed_rooms, column=1, padx=(2,10), pady=10)
                self.after(1000, lambda : [self.delete_pages, self.status_page()])
            elif room.room_availability == "RF-CLEANING":
                self.new_label = customtkinter.CTkLabel(status_frame, text="Room is ready for cleaning", font=("Arial", 20))
                self.new_label.grid(row=displayed_rooms, column=1, padx=(2,10), pady=10)
                
                self.new_button = customtkinter.CTkButton(status_frame, text="Request Housekeeper", font=("Arial", 20), command= lambda: self.clean_room(room))
                self.new_button.grid(row=displayed_rooms, column=2, padx=(2,10), pady=10)
            else:
                self.timer_label = customtkinter.CTkLabel(status_frame, text=f"{room.timer} seconds until room is available for cleaning", font=("Arial", 20))
                self.timer_label.grid(row=displayed_rooms, column=1, padx=(2,10), pady=10)

            displayed_rooms += 1
        
        self.refresh_button = customtkinter.CTkButton(status_frame, text="Refresh List", command=lambda : [self.delete_pages(), self.status_page()])
        self.refresh_button.grid(row=displayed_rooms+1, column=0, padx=10, pady=10)
        self.status_entry = customtkinter.CTkEntry(status_frame, textvariable=self.status_err, state="readonly")
        self.status_entry.grid(row=displayed_rooms+1, column=1, padx=10, pady=10, sticky="nsew")

    # Navigation bar (left side of screen)
    def nav_bar(self, gray_button):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=125, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="RoomTracker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 15))

        self.home_button = customtkinter.CTkButton(self.sidebar_frame, text="Home", command= lambda:[self.delete_pages(), self.home_page()])
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        self.patient_button = customtkinter.CTkButton(self.sidebar_frame, text="Add Patient", command= lambda:[self.delete_pages(), self.patient_page()])
        self.patient_button.grid(row=2, column=0, padx=20, pady=10)

        self.housekeep_button = customtkinter.CTkButton(self.sidebar_frame, text="Add Housekeeper", command= lambda: [self.delete_pages(),  self.housekeeper_page()])
        self.housekeep_button.grid(row=3, column=0, padx=20, pady=10)

        self.status_button = customtkinter.CTkButton(self.sidebar_frame, text="Room Status View", command= lambda:[self.delete_pages(), self.status_page()])
        self.status_button.grid(row=4, column=0, padx=20, pady=10)

        if gray_button == "home":
            self.home_button.configure(fg_color="#7F8590")
        elif gray_button == "patient":
            self.patient_button.configure(fg_color="#7F8590")
        elif gray_button == "housekeep":
            self.housekeep_button.configure(fg_color="#7F8590")
        else:
            self.status_button.configure(fg_color="#7F8590")

    def delete_pages(self):
        for frame in self.winfo_children():
            frame.destroy()
    
    def countdown(self, room):
        if room.timer > 0:
            room.timer -= 1
            self.after(1000, lambda: [self.countdown(room)])

            if room.timer == 0 and room.room_availability == "OCCUPIED":
                room.room_availability = "RF-CLEANING"
            if room.timer == 0 and room.room_availability == "CLEANING":
                room.room_availability = "AVAILABLE"

    def add_housekeeper(self):
        id = self.hk_id_entry.get()
        name = self.hk_name_entry.get()
        output = self.hospital.add_house_keeper(HouseKeeper(id, name))
        self.hk_err.set(output)

    def clean_room(self, room):
        err = self.hospital.request_room_cleaning(room)
        if err == "There are no available house keepers":
            return self.status_err.set(err)
        err2 = self.hospital.cleaning_beginning(room.room_number)
        self.status_err.set(err2)
        self.countdown(room)
        if room.timer == 0:
            self.hospital.cleaning_complete(room)

    def create_room(self):
        next_room = len(self.hospital._rooms)+1
        new_room = Room(next_room)
        self.err_msg.set(f"Created room {next_room}")
        return self.hospital.add_room(new_room)

    def add_patient(self, patient_entry):
        # adds a patient to a room
        try:
            requested_room = int(self.assign_room_entry.get())
        except ValueError:
            return self.err_msg.set("Enter a valid integer")
        if requested_room > len(self.hospital._rooms):
            return self.err_msg.set("Enter a valid room #")
        elif patient_entry == "Ambulatory" or patient_entry == "Non-Ambulatory":
            for room in self.hospital._rooms:
                if requested_room == room.room_number and room.room_availability == "AVAILABLE":
                    # set patient type before running usage_timer()
                    if patient_entry == "Ambulatory":
                        room.room_status = "FILTHY"
                    else:
                        room.room_status = "DIRTY"

                    room.room_availability = "OCCUPIED"
                    room.usage_timer()
                    self.countdown(room)
                    self.err_msg.set(f"Added Patient to room {room.room_number}")
                    return
            return self.err_msg.set(f"Room {room.room_number} is occupied")
        else:
            return self.err_msg.set("Enter a valid patient type")

if __name__ == "__main__":
    app = App()
    app.home_page()
    app.mainloop()
