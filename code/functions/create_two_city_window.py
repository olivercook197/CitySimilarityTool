from tkinter import *
from functions import info_tool_tip


class create_window:
    def __init__(self, cities, similarity, attributes):
        self.cities = cities
        self.similarity = similarity
        self.attribues = attributes
        self.table_number = 0

        self.dict_headings_key = {"High Temperature": ["high_temperature", 0], "Low Temperature": ["low_temperature", 1],
                                  "Pressure": ["pressure", 2], "Wind Speed": ["wind_speed", 3], "Humidity": ["humidity", 4],
                                  "Rainfall": ["rainfall", 5], "Rainfall Days": ["rainfall_days", 6], "Snowfall": ["snowfall", 7],
                                  "Snowfall Days": ["snowfall_days", 8], "Daylight": ["daylight", 9], "Sunshine": ["sunshine", 10],
                                  "Sunshine Days": ["sunshine_days", 11], "UV Index": ["uv_index", 12],
                                  "Cloud Cover": ["cloud_cover", 13]}

        self.window = Tk()
        self.window.geometry("300x300")
        self.window.update_idletasks()
        similarity_label = Label(self.window,
                                 text=f"Similarity between {cities[0][3]}, {cities[0][4]} and {cities[1][3]},"
                                      f" {cities[1][4]} is {round(similarity, 3)}.",
                                 wraplengt=self.window.winfo_width(), font=("Helvetica", 16)).grid(row=0, column=0,
                                                                                              columnspan=2)

        self.show_other_info()
        open_table_button = Button(self.window, text="Open Tables", command=self.create_tables).grid(row=2, column=0,
                                                                                                     pady=5, columnspan=2)

        self.window.mainloop()

    def create_tables(self):
        self.table_window = Tk()

        self.show_tables()

        self.table_window.mainloop()

    def show_tables(self):
        for widget in self.table_window.winfo_children():
            widget.destroy()
        longest_city_length = len(max(self.cities[0]['city_localisation'], self.cities[1]['city_localisation']))
        Label(self.table_window, text=f"{self.attribues[self.table_number]} similarity", font=("Helvetica", 16)).grid(
            row=0, column=0, columnspan=2)
        Button(self.table_window, text="Info", relief=FLAT, fg="dark blue", font=("Helvetica", 11, "underline"),
               cursor="hand2", command=lambda attribute=self.attribues[self.table_number]: info_tool_tip.attribute_info(
                   self.dict_headings_key[self.attribues[self.table_number]][1])).grid(row=1, column=0, columnspan=2)
        Label(self.table_window,
              text=f"{'  ' * longest_city_length}  J      F      M      A      M      J        J      A      S      O  "
                   f"    N      D").grid(row=2, column=0, columnspan=2)
        Label(self.table_window, text=f"{' ' * (longest_city_length - len(self.cities[0]['city_localisation']))}"
                                      f"{self.cities[0]['city_localisation']}: "
                                      f"{self.cities[0][self.dict_headings_key[self.attribues[self.table_number]][0]]}"
                                      f"").grid(row=3, column=0, columnspan=2)
        Label(self.table_window, text=f"{' ' * (longest_city_length - len(self.cities[1]['city_localisation']))}"
                                      f"{self.cities[1]['city_localisation']}: "
                                      f"{self.cities[1][self.dict_headings_key[self.attribues[self.table_number]][0]]}"
                                      f"").grid(row=4, column=0, columnspan=2)
        Button(self.table_window, text="< Previous Table", command=self.previous_table).grid(row=5, column=0, pady=5)
        Button(self.table_window, text="Next Table >", command=self.next_table).grid(row=5, column=1, pady=5)

    def previous_table(self):
        self.table_number -= 1
        if self.table_number == -1:
            self.table_number = len(self.attribues) - 1
        self.show_tables()

    def next_table(self):
        self.table_number += 1
        if self.table_number == len(self.attribues):
            self.table_number = 0
        self.show_tables()

    def show_other_info(self):
        frame = Frame(self.window)
        frame.grid(row=1, column=0, columnspan=2)
        city1label = Label(frame, text=self.cities[0]["city_localisation"]).grid(row=0, column=1)
        city2label = Label(frame, text=self.cities[1]["city_localisation"]).grid(row=0, column=2)
        latitude_label = Label(frame, text="Latitude:").grid(row=1, column=0)
        longitude_label = Label(frame, text="Longitude:").grid(row=2, column=0)
        hemisphere_label = Label(frame, text="Hemisphere:").grid(row=3, column=0)
        altitude_label = Label(frame, text="Altitude:").grid(row=4, column=0)
        population_label = Label(frame, text="Population:").grid(row=5, column=0)
        co2_label = Label(frame, text="CO2 production:").grid(row=6, column=0)
        for i in range(0, 6):
            if i == 0 or i == 1:
                Label(frame, text=round(self.cities[0][i+19], 3)).grid(row=i+1, column=1)
                Label(frame, text=round(self.cities[1][i+19], 3)).grid(row=i+1, column=2)
            else:
                Label(frame, text=self.cities[0][i+19]).grid(row=i+1, column=1)
                Label(frame, text=self.cities[1][i+19]).grid(row=i+1, column=2)

