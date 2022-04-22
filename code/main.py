from tkinter import *
import pandas as pd
import compare_two_cities, find_similar_cities
from functions import info_tool_tip

list_of_attributes = ["High Temperature", "Low Temperature", "Pressure", "Wind Speed", "Humidity", "Rainfall",
                      "Rainfall Days", "Snowfall", "Snowfall Days", "Daylight", "Sunshine", "Sunshine Days", "UV Index",
                      "Cloud Cover"]

df = []

root = Tk()
root.title("City Comparison Tool")
root.iconbitmap(default="cityscape_icon.ico")
root.geometry("400x680")
root.update_idletasks()
global returned
returned = False
base_weighting = {"High Temperature": 10, "Low Temperature": 10, "Pressure": 8, "Wind Speed": 8, "Humidity": 8,
                  "Rainfall": 10, "Rainfall Days": 5, "Snowfall": 8, "Snowfall Days": 4, "Daylight": 8, "Sunshine": 4,
                  "Sunshine Days": 2, "UV Index": 1, "Cloud Cover": 8}
attribute_min_max = {"high_temp": [-32.7, 48], "low_temp": [-38.3, 35], "pressure": [995, 1031.8], "wind_speed":
    [2.5, 38.2], "humidity": [9, 97], "rainfall": [0, 1350.4], "rainfall_days": [0, 31], "snowfall": [0, 1470],
                     "snowfall_days": [0, 28.4], "daylight": [4, 24], "sunshine": [0.2, 14.4], "sunshine_days": [0, 31],
                     "uv_index": [0, 12], "cloud_cover": [0, 91]}

print("initialising...")


# triggered after weightings have been selected
def start_button():
    for widget in root.winfo_children():
        widget.destroy()
    frame = Frame(root)
    frame.pack()
    initial_question_label = Label(frame, text="What would you like to do?", font=("Helvetica", 15))
    initial_question_label.grid(row=0, column=0, columnspan=2, pady=30)

    # allows users to find cities that are similar to a city they choose
    find_similar_cities_button = Button(frame, text="Find Similar Cities", command=find_similar_cities_command)
    find_similar_cities_button.grid(row=1, column=0, padx=8, pady=8)

    # allows users to compare two cities against each other
    compare_cities_button = Button(frame, text="Compare Two Cities", command=compare_two_cities_command)
    compare_cities_button.grid(row=1, column=1, padx=8, pady=8)

    # allows users to reset the weightings
    reset_weightings_button = Button(frame, text="Reset Weightings", command=create_weightings)
    reset_weightings_button.grid(row=2, column=0, columnspan=2, pady=8)

    # allows users to quit the program
    quit_button = Button(frame, text="Quit", command=root.destroy)
    quit_button.grid(row=3, column=0, columnspan=2, pady=8)


# triggered if users want to find similar cities
def find_similar_cities_command():
    for widget in root.winfo_children():
        widget.destroy()
    global similar_cities_class
    similar_cities_class = find_similar_cities.FindSimilarCities(root, df, weighting, attribute_min_max)
    root.after(200, check_if_return_home)


# triggered if users want to compare two cities
def compare_two_cities_command():
    for widget in root.winfo_children():
        widget.destroy()
    global compare_two_cities_class
    compare_two_cities_class = compare_two_cities.CompareTwoCities(root, df, weighting, attribute_min_max)
    root.after(200, check_if_return_home)


def check_if_return_home():
    global returned
    global similar_cities_class
    global compare_two_cities_class
    if returned:
        returned = False
        root.after(200, check_if_return_home)
    else:
        try:
            if similar_cities_class.return_home:
                print("returning home")
                returned = True
                similar_cities_class = None
                start_button()
            else:
                root.after(200, check_if_return_home)
        except:
            pass
        try:
            if compare_two_cities_class.return_home:
                print("returning home")
                returned = True
                compare_two_cities_class = None
                start_button()

            else:
                root.after(200, check_if_return_home)
        except:
            pass


# if a user wants custom weightings their selections are read to memory
def get_weightings(entries):
    selected_weightings = []
    for entry_box in entries:
        cw = entry_box.get()
        selected_weightings.append(cw)
    for attribute in range(0, len(weighting)):
        try:
            if selected_weightings[attribute] != "":
                if int(selected_weightings[attribute]) > 0 and round(int(selected_weightings[attribute]), 0) == int(
                        selected_weightings[attribute]):
                    weighting[list_of_attributes[attribute]] = int(selected_weightings[attribute])
                else:
                    raise Exception
        except:
            error_window = Tk()
            error_label = Label(error_window, text="Input was incorrect, using recommended settings.").pack()
            ok_button = Button(error_window, text="OK", command=error_window.destroy).pack()
    print(weighting)
    start_button()


# triggered when users have decided which dataset they want and appropriate csv file has been read, this allows users
# to select the weightings they would like
def create_weightings():
    global weighting
    global base_weighting
    weighting = {}
    for i in base_weighting:
        weighting.update({i: base_weighting[i]})
    for widget in root.winfo_children():
        widget.destroy()
    weightings_label = Label(text="Enter the weightings you would like to use (only accepts integers) otherwise press "
                                  "Use Recommended Settings. Any attributes left blank will automatically use their "
                                  "recommended value. Recommended values are shown in brackets.",
                             wraplengt=400, font=("Helvetica", 11)).grid(row=0, column=0, columnspan=2)
    use_recommended_settings = Button(text="Use Recommended Settings", command=start_button).grid(row=1, columnspan=2,
                                                                                                  pady=8)
    entries = []
    list_of_buttons = []
    for attribute in range(0, len(list_of_attributes)):
        Label(text=f"{list_of_attributes[attribute]}: ({weighting[list_of_attributes[attribute]]})",
              font=("Helvetica", 11)).grid(
            row=attribute + 2, column=0, sticky="W")
        # info button allows the info of any attribute to be seen
        info_button = Button(text="Info", relief=FLAT, fg="dark blue", font=("Helvetica", 11, "underline"),
                             cursor="hand2",
                             command=lambda attribute=attribute: info_tool_tip.attribute_info(attribute)).grid(
            row=attribute + 2, column=0, columnspan=2)
        list_of_buttons.append(info_button)
        en = Entry(root)
        en.grid(row=attribute + 2, column=1)
        entries.append(en)
    c = []
    get_weight_button = Button(text="OK", command=lambda: c == get_weightings(entries)).grid(row=16, columnspan=2,
                                                                                             pady=8)


def set_weighting():
    global weighting
    global base_weighting
    weighting = base_weighting
    start_button()


# triggered if users want to use dataset with all cities
def all_cities_chosen():
    global df
    df = pd.read_csv("city_data_csv_updated.csv")
    create_weightings()


# triggered if users want to use dataset with only the cities with CO2 data
def CO2_cities_chosen():
    global df
    df = pd.read_csv("CO2_city_data.csv")
    create_weightings()


# when users have read through intro text they are asked which dataset they want to use
def choose_data_set():
    global df
    for widget in root.winfo_children():
        widget.destroy()
    all_or_CO2_label = Label(root, text="Would you like to use the full dataset of 2632 cities or the dataset of 373 "
                                        "cities that contain CO2 data?", font=("Helvetica", 11),
                             wraplengt=root.winfo_width() - 10, padx=10).grid(row=0, columnspan=2)
    all_cities_button = Button(root, text="All cities", command=all_cities_chosen).grid(row=1, column=0, pady=5)
    CO2_cities = Button(root, text="Only cities with CO2 data", command=CO2_cities_chosen).grid(row=1, column=1, pady=5)


# create opening screen
intro_text_label = Label(root, text="Welcome to this tool, it has been created as part of my undergraduate dissertation"
                                    " project at Newcastle University. It uses publicly available data, with a special "
                                    "mention to https://www.citycarbonfootprints.info/ and "
                                    "https://www.codeminders.com/weather_similarity/ which served as the initial "
                                    "inspiration. I hope you find this tool useful and educational.",
                         font=("Helvetica", 11), wraplengt=root.winfo_width() - 10,
                         padx=10)
intro_text_label.grid(row=0, column=0, columnspan=2)

intro_start_button = Button(root, text="Start", command=choose_data_set)
intro_start_button.grid(row=1, column=0, columnspan=2)

root.mainloop()
