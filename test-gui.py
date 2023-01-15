import tkinter
import tkinter.messagebox
import customtkinter

# below is not yet functional, meant to import room class
# import functions as hospital

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RoomTracker.py")
        self.geometry(f"{1100}x{580}")

        # Grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.grid_rowconfigure((0), weight=1)

        # text entry vars
        self.create_room_num = customtkinter.StringVar()
        
        # list of all room classes
        self.rooms = []

    # page creation functions
    def home_page(self):
        home_frame = customtkinter.CTkFrame(self)

        # create navbar
        self.nav_bar("home")

        # contents of home page
        label = customtkinter.CTkLabel(home_frame, text="Home Page")
        label.grid(row=0, column=1, padx=20, pady=20)

        home_frame.grid(row=0, column=1, padx=20, pady=20)

    def patient_page(self):
        patient_frame = customtkinter.CTkFrame(self)

        # create navbar
        self.nav_bar("patient")

        # create add patient tab
        self.patient_tab = customtkinter.CTkTabview(self, width=250)
        self.patient_tab.grid(row=0, column=1, padx=(20, 20), pady=(15, 20), sticky="nsew")
        self.patient_tab.add("Add Patient")
        self.patient_tab.tab("Add Patient").grid_columnconfigure(0, weight=1)

        self.dropdown_menu = customtkinter.CTkComboBox(self.patient_tab.tab("Add Patient"),
                                                    values=["Ambulatory Patient", "Unknown Type", "Etc..."], width=170)
        self.dropdown_menu.grid(row=0, column=0, padx=20, pady=(100, 10))

        self.assign_room_entry = customtkinter.CTkEntry(self.patient_tab.tab("Add Patient"), textvariable=self.create_room_num)
        self.assign_room_entry.grid(row=1, column=0, padx=20, pady=20)
        
        self.create_room_button = customtkinter.CTkButton(self.patient_tab.tab("Add Patient"), text="Create Room",
                                                        command=self.create_room)
        self.create_room_button.grid(row=2, column=0, padx=20, pady=(15, 10))

        # dropdown default text
        self.dropdown_menu.set("Select Patient Type")
    
    def status_page(self):
        status_frame = customtkinter.CTkFrame(self)

        self.nav_bar("status")

        # create visual progress bar for each room


    # Navigation bar (left side of screen)
    def nav_bar(self, gray_button):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="RoomTracker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 15))

        self.home_button = customtkinter.CTkButton(self.sidebar_frame, text="Home", command= lambda:[self.delete_pages(), self.home_page()])
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        self.patient_button = customtkinter.CTkButton(self.sidebar_frame, text="Add Patient", command= lambda:[self.delete_pages(), self.patient_page()])
        self.patient_button.grid(row=2, column=0, padx=20, pady=10)

        self.status_button = customtkinter.CTkButton(self.sidebar_frame, text="Room Status View", command= lambda:[self.delete_pages(), self.status_page()])
        self.status_button.grid(row=3, column=0, padx=20, pady=10)
        if gray_button == "home":
            self.home_button.configure(fg_color="#7F8590")
        elif gray_button == "patient":
            self.patient_button.configure(fg_color="#7F8590")
        else:
            self.status_button.configure(fg_color="#7F8590")

    def delete_pages(self):
        for frame in self.winfo_children():
            frame.destroy()

    def open_input_dialog_event(self):
        # dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        # print("CTkInputDialog:", dialog.get_input())
        pass

    def create_room(self):
        # creates a room object when called
        pass


if __name__ == "__main__":
    app = App()
    app.home_page()
    app.mainloop()