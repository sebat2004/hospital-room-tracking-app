import tkinter
import tkinter.messagebox
import customtkinter

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

        def home_page(self):
            home_frame = customtkinter.CTkFrame(self)

            # create navbar
            nav_bar("home_button")

            # contents of home page
            label = customtkinter.CTkLabel(home_frame, text="Home Page")
            label.grid(row=0, column=1, padx=20, pady=20)

            home_frame.grid(row=0, column=1, padx=20, pady=20)

        # Navigation bar (left side of screen)
        def nav_bar(gray_button):
            self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
            self.sidebar_frame.grid_rowconfigure(4, weight=1)
            
            self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="RoomTracker", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 15))

            self.home_button = customtkinter.CTkButton(self.sidebar_frame, text="Home", command=lambda: home_page)
            self.home_button.grid(row=1, column=0, padx=20, pady=10)

            self.patient_button = customtkinter.CTkButton(self.sidebar_frame, text="Add Patient")
            self.patient_button.grid(row=2, column=0, padx=20, pady=10)

            self.status_button = customtkinter.CTkButton(self.sidebar_frame, text="Room Status View")
            self.status_button.grid(row=3, column=0, padx=20, pady=10)

            self.gray_button.configure(fg_color="7F8590")

        def patient_page(self):
            home_frame = customtkinter.CTkFrame(self)

            # create tabview
            self.tabview = customtkinter.CTkTabview(self, width=250)
            self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(15, 20), sticky="nsew")
            self.tabview.add("Add Patient")
            self.tabview.add("View Rooms")
            self.tabview.tab("Add Patient").grid_columnconfigure(0, weight=1)
            self.tabview.tab("View Rooms").grid_columnconfigure(0, weight=1)

            self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Add Patient"),
                                                        values=["Ambulatory Patient", "Unknown Type", "Etc..."], width=170)
            self.combobox_1.grid(row=0, column=0, padx=20, pady=(100, 10))
            
            self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Add Patient"), text="Create Room",
                                                            command=self.create_room_event)
            self.string_input_button.grid(row=1, column=0, padx=20, pady=(15, 10))

            self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("View Rooms"))
            self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # set default values
        self.combobox_1.set("Select Patient Type")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def create_room_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()