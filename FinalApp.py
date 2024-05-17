import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pytz
from datetime import datetime
from tkinter import messagebox
import time
import threading


#This class is for the planet ages 
class PlanetPage:
    def __init__(self, app, name, info, **kwargs):
        self.frame = app.create_page(name)
        self.app = app
        self.name = name
        self.info = info
        self.additional_info = kwargs
        self.create_page()

    def create_page(self):
        label = ctk.CTkLabel(self.frame, text=f"Welcome to {self.name}", font=("Helvetica", 24, "bold"), text_color="yellow")
        label.place(relx=0.5, rely=0.1, anchor="center")

        system_label = ctk.CTkLabel(self.frame, text=f"System: {self.info['system']}", font=("Helvetica", 14), text_color="white")
        system_label.place(relx=0.5, rely=0.25, anchor="center")

        population_label = ctk.CTkLabel(self.frame, text=f"Population: {self.info['population']}", font=("Helvetica", 14), text_color="white")
        population_label.place(relx=0.5, rely=0.35, anchor="center")

        if "timezone" in self.info:
            time_label = ctk.CTkLabel(self.frame, text="", font=("Helvetica", 14), text_color="white")
            time_label.place(relx=0.5, rely=0.45, anchor="center")
            self.app.update_clock(time_label, self.info["timezone"], self.name)

        fun_fact_1_label = ctk.CTkLabel(self.frame, text=f"Fun Fact 1: {self.info['fun_facts'][0]}", font=("Helvetica", 14), text_color="white")
        fun_fact_1_label.place(relx=0.5, rely=0.55, anchor="center")

        fun_fact_2_label = ctk.CTkLabel(self.frame, text=f"Fun Fact 2: {self.info['fun_facts'][1]}", font=("Helvetica", 14), text_color="white")
        fun_fact_2_label.place(relx=0.5, rely=0.65, anchor="center")

        # Display additional information
        additional_info_y = 0.75
        for key, value in self.additional_info.items():
            additional_info_label = ctk.CTkLabel(self.frame, text=f"{key.capitalize()}: {value}", font=("Helvetica", 14), text_color="white")
            additional_info_label.place(relx=0.5, rely=additional_info_y, anchor="center")
            additional_info_y += 0.05

        back_button = ctk.CTkButton(self.frame, text="Back", command=lambda: self.app.show_frame("Main"), corner_radius=20)
        back_button.place(relx=0.5, rely=additional_info_y, anchor="center")

# I made the whole main application a class named StarWarsApp
class StarWarsApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Star Wars App")

        # URL of the image
        image_url = "https://wallpapers.com/images/high/star-wars-space-background-1595-x-1162-e178irn8bim5vake.webp"

        # Download the image
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
        else:
            raise Exception(f"Failed to download image from {image_url}")

        # Use PIL to open the image
        background_image = Image.open(BytesIO(image_data))
        background_image = ImageTk.PhotoImage(background_image)
        background_label = ctk.CTkLabel(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        self.frames = {}
        self.messages = []
        self.create_main_frame()
        self.create_planet_pages()
        self.create_transmissions_page()
        self.create_login_page()
        self.create_messages_page()
        self.create_nav_frame()

        # Show the main frame
        root.after(100, lambda: self.show_frame("Main"))

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
  #To creaate the main page with the buttons 
    def create_page(self, name, visible=False):
        frame = ctk.CTkFrame(self.root, corner_radius=10, fg_color="transparent")
        frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.5)
        self.frames[name] = frame
        if visible:
            frame.tkraise()
        return frame

    def create_main_frame(self):
        main_frame = self.create_page("Main", visible=True)
        
        title_label = ctk.CTkLabel(main_frame, text="Welcome to the Star Wars App", font=("Helvetica", 24, "bold"), text_color="yellow")
        title_label.pack(pady=10)

        for planet in planet_info.keys():
            button = ctk.CTkButton(main_frame, text=planet, command=lambda p=planet: self.open_planet_page(p), corner_radius=25)
            button.pack(pady=10, padx=20)
    #Function to open whatever planet we choose
    def open_planet_page(self, planet):
        print(f"Opening {planet} page...")
        self.show_frame(planet)

    def create_planet_pages(self):
        # Adding additional information using kwargs
        PlanetPage(self, "Tatooine", planet_info["Tatooine"], planet_age="5 billion years", climate="Arid")
        PlanetPage(self, "Hoth", planet_info["Hoth"], planet_age="Unknown", climate="Frozen")
        PlanetPage(self, "Endor", planet_info["Endor"], planet_age="Unknown", climate="Forested")
        PlanetPage(self, "Naboo", planet_info["Naboo"], planet_age="Unknown", climate="Temperate")
        PlanetPage(self, "Kamino", planet_info["Kamino"], planet_age="Unknown", climate="Oceanic")
        PlanetPage(self, "Coruscant", planet_info["Coruscant"], planet_age="Unknown", climate="Urban")
        PlanetPage(self, "Alderaan", planet_info["Alderaan"], planet_age="Unknown", climate="Temperate")
    #to show the current time on planetv
    def update_clock(self, label, timezone, planet):
        if timezone:  # Check if timezone is provided
            tz = pytz.timezone(timezone)
            now = datetime.now(tz)
            current_time = now.strftime("%H:%M:%S")
            label.configure(text=f"Current Time on {planet}: {current_time}")
            label.after(1000, self.update_clock, label, timezone, planet)

    def create_transmissions_page(self):
        transmissions_frame = self.create_page("Transmissions")
        transmissions_label = ctk.CTkLabel(transmissions_frame, text="Send a Transmission", font=("Helvetica", 24, "bold"), text_color="yellow")
        transmissions_label.place(relx=0.5, rely=0.1, anchor="center")

        self.transmissions_entry = ctk.CTkEntry(transmissions_frame, width=300)
        self.transmissions_entry.place(relx=0.5, rely=0.3, anchor="center")

        base_names = ["Echo Base", "Yavin Base", "Dantooine Base", "Hoth Base"]
        self.base_var = tk.StringVar()
        base_dropdown = ttk.Combobox(transmissions_frame, textvariable=self.base_var, values=base_names, state="readonly")
        base_dropdown.place(relx=0.5, rely=0.4, anchor="center")
        base_dropdown.set("Select Base")

        send_button = ctk.CTkButton(transmissions_frame, text="Send", command=self.send_transmission, corner_radius=20)
        send_button.place(relx=0.5, rely=0.7, anchor="center")

        transmissions_back_button = ctk.CTkButton(transmissions_frame, text="Back", command=lambda: self.show_frame("Main"), corner_radius=20)
        transmissions_back_button.place(relx=0.5, rely=0.8, anchor="center")

    def send_transmission(self, **kwargs):
        transmission_text = self.transmissions_entry.get()
        selected_base = self.base_var.get()

        if not transmission_text:
            messagebox.showwarning("Empty Transmission", "Please enter a message to send.")
            return
        if selected_base == "Select Base":
            messagebox.showwarning("No Base Selected", "Please select a base to send the transmission to.")
            return

        progress_bar = ttk.Progressbar(self.frames["Transmissions"], orient="horizontal", mode="determinate", length=300)
        progress_bar.place(relx=0.5, rely=0.6, anchor="center")
        progress_bar["value"] = 0

        def progress():
            for i in range(101):
                time.sleep(0.05)
                progress_bar["value"] = i
            progress_bar.place_forget()
            messagebox.showinfo("Transmission Sent", f"Your transmission was successfully sent to {selected_base}.")
            self.save_message(base=selected_base, message=transmission_text, **kwargs)

        threading.Thread(target=progress).start()
    #Save the trasmitted message to the database 
    def save_message(self, **kwargs):
        base = kwargs.get('base')
        message = kwargs.get('message')
        self.messages.append(f"{base}: {message}")

    def create_login_page(self):
        login_frame = self.create_page("Login")
        login_label = ctk.CTkLabel(login_frame, text="Login", font=("Helvetica", 24, "bold"), text_color="yellow")
        login_label.place(relx=0.5, rely=0.2, anchor="center")

        self.username_entry = ctk.CTkEntry(login_frame, width=200, placeholder_text="Username")
        self.username_entry.place(relx=0.5, rely=0.4, anchor="center")

        self.password_entry = ctk.CTkEntry(login_frame, width=200, placeholder_text="Password", show="*")
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center")

        login_button = ctk.CTkButton(login_frame, text="Login", command=self.check_login, corner_radius=20)
        login_button.place(relx=0.5, rely=0.6, anchor="center")

        login_back_button = ctk.CTkButton(login_frame, text="Back", command=lambda: self.show_frame("Main"), corner_radius=20)
        login_back_button.place(relx=0.5, rely=0.7, anchor="center")

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "luke" and password == "maythe4":
            self.show_frame("Messages")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    #Create messages page to display transmitted messages
    def create_messages_page(self):
        messages_frame = self.create_page("Messages")
        messages_label = ctk.CTkLabel(messages_frame, text="Transmitted Messages", font=("Helvetica", 24, "bold"), text_color="yellow")
        messages_label.place(relx=0.5, rely=0.1, anchor="center")

        self.messages_listbox = tk.Listbox(messages_frame, width=50, height=10)
        self.messages_listbox.place(relx=0.5, rely=0.5, anchor="center")

        update_messages_button = ctk.CTkButton(messages_frame, text="Refresh Messages", command=self.update_messages, corner_radius=20)
        update_messages_button.place(relx=0.5, rely=0.8, anchor="center")

        messages_back_button = ctk.CTkButton(messages_frame, text="Back", command=lambda: self.show_frame("Main"), corner_radius=20)
        messages_back_button.place(relx=0.5, rely=0.9, anchor="center")

    def update_messages(self):
        self.messages_listbox.delete(0, tk.END)
        for message in self.messages:
            self.messages_listbox.insert(tk.END, message)

    def create_nav_frame(self):
        nav_frame = ctk.CTkFrame(self.root, width=200, corner_radius=10)
        nav_frame.place(relx=0, rely=0.5, anchor="w")

        transmissions_button = ctk.CTkButton(nav_frame, text="Transmissions", command=self.open_transmissions_page, corner_radius=25)
        transmissions_button.pack(pady=10, padx=20)

        login_button = ctk.CTkButton(nav_frame, text="Login", command=self.open_login_page, corner_radius=25)
        login_button.pack(pady=10, padx=20)

    def open_transmissions_page(self):
        print("Opening transmissions page...")
        self.show_frame("Transmissions")

    def open_login_page(self):
        print("Opening login page...")
        self.show_frame("Login")

# A dictionary that contains information about every planet. 
planet_info = {
    "Tatooine": {"system": "Tatoo system", "timezone": "Asia/Riyadh", "population": "200,000", "fun_facts": ["Home to Anakin Skywalker", "Known for its twin suns"]},
    "Hoth": {"system": "Anoat system", "timezone": "Antarctica/Troll", "population": "Unknown", "fun_facts": ["Site of the Rebel Alliance's Echo Base", "Known for its icy terrain"]},
    "Endor": {"system": "Endor system", "timezone": "Pacific/Midway", "population": "30,000 Ewoks", "fun_facts": ["Location of the Battle of Endor", "Home to the Ewoks"]},
    "Naboo": {"system": "Chommell sector", "timezone": "Pacific/Auckland", "population": "4.5 million", "fun_facts": ["Home to Padmé Amidala", "Known for its beautiful landscapes"]},
    "Kamino": {"system": "Wild Space", "timezone": "Etc/GMT+12", "population": "1 million", "fun_facts": ["Home to the Clone Army production", "Known for its ocean-covered surface"]},
    "Coruscant": {"system": "Coruscant system", "timezone": "Etc/GMT-3", "population": "1 trillion", "fun_facts": ["Capital of the Galactic Empire", "Known as the city-covered planet"]},
    "Alderaan": {"system": "Alderaan system", "population": "2 billion", "fun_facts": ["Home to Princess Leia", "Destroyed by the Death Star"]},
}

if __name__ == "__main__":
    root = ctk.CTk()
    app = StarWarsApp(root)
    root.mainloop()
