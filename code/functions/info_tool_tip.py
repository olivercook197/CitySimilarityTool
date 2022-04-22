from tkinter import *


def attribute_info(command):
    tip_window = Tk()
    command_dict = {0: "The average high temperature is the average of the highest daily temperature, measured in "
                       "Celsius.",
                    1: "The average low temperature is the average of the lowest daily temperature, measured in "
                       "Celsius.",
                    2: "The average monthly pressure, measured in mbar.",
                    3: "The average wind speed, measured in km/h.",
                    4: "Relative humidity indicates a present state of absolute humidity relative to a maximum "
                       "humidity given the same temperature, measured as a percentage.",
                    5: "Rainfall is the amount of rain fallen in a month, measured in mm.",
                    6: "Rainfall days is the number of days in a month at least 1mm of rain will fall, measured in "
                       "days.",
                    7: "Snowfall is the amount of snow fallen in a month, measured in mm.",
                    8: "Snowfall days is the number of days in a month at least 1mm of snow will fall, "
                       "measured in days.",
                    9: "Daylight is the amount of time the sun is up a day, measured in hours.",
                    10: "Sunshine is the amount of time the sun is visible a day, measured in hours.",
                    11: "Sunshine days is how many days a month it will be sunny, measured in days.",
                    12: "UV Index is a forecast of the amount of skin damaging UV radiation expected to reach the "
                        "earth's surface at the time when the sun is highest in the sky, measured on the UV Index "
                        "Scale.",
                    13: "Cloud cover is how much of the sky is obscured by clouds, measured as a percentage."}
    Label(tip_window, text=command_dict[command]).pack()