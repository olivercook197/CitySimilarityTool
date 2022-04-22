from tkinter import *


class AttributeSelector:
    def __init__(self, inherited_root, city):
        global root
        root = inherited_root
        self.root = inherited_root
        self.city = []
        if len(city) == 2:
            self.city.append(city[0])
            self.city.append(city[1])
        else:
            self.city.append(city)
        self.list_of_checkboxes = []
        self.list_of_attributes = []
        self.potential_attributes = []
        self.similarity = 0

        # initialise checkbox variables
        self.high_temp_var = BooleanVar()
        self.low_temp_var = BooleanVar()
        self.pressure_var = BooleanVar()
        self.wind_speed_var = BooleanVar()
        self.humidity_var = BooleanVar()
        self.rainfall_var = BooleanVar()
        self.rainfall_days_var = BooleanVar()
        self.snowfall_var = BooleanVar()
        self.snowfall_days_var = BooleanVar()
        self.daylight_var = BooleanVar()
        self.sunshine_var = BooleanVar()
        self.sunshine_days_var = BooleanVar()
        self.uv_index_var = BooleanVar()
        self.cloud_cover = BooleanVar()
        self.include_all_var = BooleanVar()
        #print(len(self.city))
        if len(self.city) == 1:
            chosen_city_label = Label(root, text=f"Chosen city: {city.iloc[3]}, {city.iloc[4]}",
                                      wraplengt=root.winfo_width(), font=("Helvetica", 16)).pack()
        else:
            chosen_cities_label = Label(root,
                                        text=f"Chosen cities: {city[0].iloc[3]}, {city[0].iloc[4]} and {city[1].iloc[3]}"
                                             f", {city[1].iloc[4]}", wraplengt=root.winfo_width(),
                                        font=("Helvetica", 16)).pack()
        choose_attributes_label = Label(root, text="Choose the attributes you want to compare.",
                                        font=("Helvetica", 14)).pack()
        na_attr = "['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']"

        self.list_of_checkboxes.append(Checkbutton(root, text="Include all", font=12, variable=self.include_all_var))

        if len(self.city) == 1:
            if city.iloc[5] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="High Temperature", font=12,
                                                           variable=self.high_temp_var))
                self.potential_attributes.append("High Temperature")
            if city.iloc[6] != na_attr:
                self.list_of_checkboxes.append(
                    Checkbutton(root, text="Low Temperature", font=12, variable=self.low_temp_var))
                self.potential_attributes.append("Low Temperature")
            if city.iloc[7] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Pressure", font=12, variable=self.pressure_var))
                self.potential_attributes.append("Pressure")
            if city.iloc[8] != na_attr:
                self.list_of_checkboxes.append(
                    Checkbutton(root, text="Wind Speed", font=12, variable=self.wind_speed_var))
                self.potential_attributes.append("Wind Speed")
            if city.iloc[9] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Humidity", font=12, variable=self.humidity_var))
                self.potential_attributes.append("Humidity")
            if city.iloc[10] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Rainfall", font=12, variable=self.rainfall_var))
                self.potential_attributes.append("Rainfall")
            if city.iloc[11] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Rainfall Days", font=12,
                                                           variable=self.rainfall_days_var))
                self.potential_attributes.append("Rainfall Days")
            if city.iloc[12] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Snowfall", font=12, variable=self.snowfall_var))
                self.potential_attributes.append("Snowfall")
            if city.iloc[13] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Snowfall Days", font=12, variable=self.snowfall_days_var))
                self.potential_attributes.append("Snowfall Days")
            if city.iloc[14] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Daylight", font=12, variable=self.daylight_var))
                self.potential_attributes.append("Daylight")
            if city.iloc[15] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Sunshine", font=12, variable=self.sunshine_var))
                self.potential_attributes.append("Sunshine")
            if city.iloc[16] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Sunshine Days", font=12, variable=self.sunshine_days_var))
                self.potential_attributes.append("Sunshine Days")
            if city.iloc[17] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="UV Index", font=12, variable=self.uv_index_var))
                self.potential_attributes.append("UV Index")
            if city.iloc[18] != na_attr:
                self.list_of_checkboxes.append(
                    Checkbutton(root, text="Cloud Cover", font=12, variable=self.cloud_cover))
                self.potential_attributes.append("Cloud Cover")
        else:
            if city[0].iloc[5] != na_attr and city[1].iloc[5] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="High Temperature", font=12,
                                                           variable=self.high_temp_var))
                self.potential_attributes.append("High Temperature")
            if city[0].iloc[6] != na_attr and city[1].iloc[6] != na_attr:
                self.list_of_checkboxes.append(
                    Checkbutton(root, text="Low Temperature", font=12, variable=self.low_temp_var))
                self.potential_attributes.append("Low Temperature")
            if city[0].iloc[7] != na_attr and city[1].iloc[7] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Pressure", font=12, variable=self.pressure_var))
                self.potential_attributes.append("Pressure")
            if city[0].iloc[8] != na_attr and city[1].iloc[8] != na_attr:
                self.list_of_checkboxes.append(
                    Checkbutton(root, text="Wind Speed", font=12, variable=self.wind_speed_var))
                self.potential_attributes.append("Wind Speed")
            if city[0].iloc[9] != na_attr and city[1].iloc[9] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Humidity", font=12, variable=self.humidity_var))
                self.potential_attributes.append("Humidity")
            if city[0].iloc[10] != na_attr and city[1].iloc[10] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Rainfall", font=12, variable=self.rainfall_var))
                self.potential_attributes.append("Rainfall")
            if city[0].iloc[11] != na_attr and city[1].iloc[11] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Rainfall Days", font=12,
                                                           variable=self.rainfall_days_var))
                self.potential_attributes.append("Rainfall Days")
            if city[0].iloc[12] != na_attr and city[1].iloc[12] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Snowfall", font=12, variable=self.snowfall_var))
                self.potential_attributes.append("Snowfall")
            if city[0].iloc[13] != na_attr and city[1].iloc[13] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Snowfall Days", font=12,
                                                           variable=self.snowfall_days_var))
                self.potential_attributes.append("Snowfall Days")
            if city[0].iloc[14] != na_attr and city[1].iloc[14] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Daylight", font=12, variable=self.daylight_var))
                self.potential_attributes.append("Daylight")
            if city[0].iloc[15] != na_attr and city[1].iloc[15] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Sunshine", font=12, variable=self.sunshine_var))
                self.potential_attributes.append("Sunshine")
            if city[0].iloc[16] != na_attr and city[1].iloc[16] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Sunshine Days", font=12,
                                                           variable=self.sunshine_days_var))
                self.potential_attributes.append("Sunshine Days")
            if city[0].iloc[17] != na_attr and city[1].iloc[17] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="UV Index", font=12, variable=self.uv_index_var))
                self.potential_attributes.append("UV Index")
            if city[0].iloc[18] != na_attr and city[1].iloc[18] != na_attr:
                self.list_of_checkboxes.append(Checkbutton(root, text="Cloud Cover", font=12, variable=self.cloud_cover))
                self.potential_attributes.append("Cloud Cover")

        for i in self.list_of_checkboxes:
            i.pack()

        global similarity_entry_box
        if len(self.city) == 1:
            similarity_label = Label(root, text="Choose similarity (0.01-1.00)", font=("Helvetica", 14), fg="grey")
            similarity_label.pack(pady=16)
            similarity_entry_box = Entry(root, font=("Helvetica", 20))
            similarity_entry_box.pack()

        ok_button_attribute = Button(root, text="OK", command=self.ok_button_pressed_attribute).pack(pady=10)

    def ok_button_pressed_attribute(self):
        global similarity_entry_box
        if self.include_all_var.get():
            for i in self.potential_attributes:
                self.list_of_attributes.append(i)
        else:
            if self.high_temp_var.get():
                self.list_of_attributes.append("High Temperature")
            if self.low_temp_var.get():
                self.list_of_attributes.append("Low Temperature")
            if self.pressure_var.get():
                self.list_of_attributes.append("Pressure")
            if self.wind_speed_var.get():
                self.list_of_attributes.append("Wind Speed")
            if self.humidity_var.get():
                self.list_of_attributes.append("Humidity")
            if self.rainfall_var.get():
                self.list_of_attributes.append("Rainfall")
            if self.rainfall_days_var.get():
                self.list_of_attributes.append("Rainfall Days")
            if self.snowfall_var.get():
                self.list_of_attributes.append("Snowfall")
            if self.snowfall_days_var.get():
                self.list_of_attributes.append("Snowfall Days")
            if self.daylight_var.get():
                self.list_of_attributes.append("Daylight")
            if self.sunshine_var.get():
                self.list_of_attributes.append("Sunshine")
            if self.sunshine_days_var.get():
                self.list_of_attributes.append("Sunshine Days")
            if self.uv_index_var.get():
                self.list_of_attributes.append("UV Index")
            if self.cloud_cover.get():
                self.list_of_attributes.append("Cloud Cover")
        if not self.list_of_attributes:
            error_window = Tk()
            error_window.title("Error")
            error_label = Label(error_window, text="Must make at least one selection.").pack()
            ok_error_button = Button(error_window, text="OK", command=error_window.destroy).pack()
            self.reset_passed_on_variables()
        else:
            try:
                if len(self.city) != 2:
                    if float(similarity_entry_box.get()) > 1 or float(similarity_entry_box.get()) <= 0:
                        error_window = Tk()
                        error_window.title("Error")
                        error_label = Label(error_window, text="Similarity must be between 0 and 1.").pack()
                        ok_error_button = Button(error_window, text="OK", command=error_window.destroy).pack()
                        self.reset_passed_on_variables()
                    else:
                        self.similarity = float(similarity_entry_box.get())
                        for widget in self.root.winfo_children():
                            widget.destroy()
                else:
                    for widget in self.root.winfo_children():
                        widget.destroy()
            except:
                error_window = Tk()
                error_window.title("Error")
                error_label = Label(error_window, text="Please enter how similar you want the cities to be.").pack()
                ok_error_button = Button(error_window, text="OK", command=error_window.destroy).pack()
                self.reset_passed_on_variables()

    def reset_passed_on_variables(self):
        self.similarity = 0
        self.list_of_attributes = []
