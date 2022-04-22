import pandas as pd
from tkinter import *
from functions import two_city_comparison, create_similarity_external_window


def determine_similar_cities_main(main_city, attributes, similarity_chosen, df, weighting, attribute_min_max, root):
    similarities = []
    na_attr = "['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']"
    progress = 0
    loading_label = Label(root, text="Loading...", fg="grey").grid(row=0, sticky=NSEW)
    root.update_idletasks()
    frame = Frame(root, relief=GROOVE, width=100, height=30, bd=2, padx=4)
    frame.grid(row=1, pady=20, sticky=W)
    total_number_of_cities = len(df)
    for secondary_city in range(0, total_number_of_cities):
        available_attributes = []
        if "High Temperature" in attributes:
            if df.iloc[secondary_city][5] != na_attr:
                available_attributes.append("High Temperature")
        if "Low Temperature" in attributes:
            if df.iloc[secondary_city][6] != na_attr:
                available_attributes.append("Low Temperature")
        if "Pressure" in attributes:
            if df.iloc[secondary_city][7] != na_attr:
                available_attributes.append("Pressure")
        if "Wind Speed" in attributes:
            if df.iloc[secondary_city][8] != na_attr:
                available_attributes.append("Wind Speed")
        if "Humidity" in attributes:
            if df.iloc[secondary_city][9] != na_attr:
                available_attributes.append("Humidity")
        if "Rainfall" in attributes:
            if df.iloc[secondary_city][10] != na_attr:
                available_attributes.append("Rainfall")
        if "Rainfall Days" in attributes:
            if df.iloc[secondary_city][11] != na_attr:
                available_attributes.append("Rainfall Days")
        if "Snowfall" in attributes:
            if df.iloc[secondary_city][12] != na_attr:
                available_attributes.append("Snowfall")
        if "Snowfall Days" in attributes:
            if df.iloc[secondary_city][13] != na_attr:
                available_attributes.append("Snowfall Days")
        if "Daylight" in attributes:
            if df.iloc[secondary_city][14] != na_attr:
                available_attributes.append("Daylight")
        if "Sunshine" in attributes:
            if df.iloc[secondary_city][15] != na_attr:
                available_attributes.append("Sunshine")
        if "Sunshine Days" in attributes:
            if df.iloc[secondary_city][16] != na_attr:
                available_attributes.append("Sunshine Days")
        if "UV Index" in attributes:
            if df.iloc[secondary_city][17] != na_attr:
                available_attributes.append("UV Index")
        if "Cloud Cover" in attributes:
            if df.iloc[secondary_city][18] != na_attr:
                available_attributes.append("Cloud Cover")
        similarity_between_main_and_secondary = two_city_comparison.TwoCityComparison([main_city,
                                                                                       df.iloc[secondary_city]],
                                                                                      available_attributes,
                                                                                      similarity_chosen, df, weighting,
                                                                                      attribute_min_max)
        progress += 1
        if progress >= total_number_of_cities / 22:
            mylabel = Label(frame, text="| ", bg="dark blue").pack(side=LEFT)
            mylabel = Label(frame, text="", bg="light gray").pack(side=LEFT)
            root.update()
            progress = 0
        #print(
            #f"Similarity between {main_city['city_localisation']} and {df.iloc[secondary_city]['city_localisation']}: \t{similarity_between_main_and_secondary.overall_similarity}")
        if similarity_between_main_and_secondary.overall_similarity > similarity_chosen:
            similarities.append([df.iloc[secondary_city]['city_localisation'], df.iloc[secondary_city]['country_localisation'], similarity_between_main_and_secondary.overall_similarity])
        try:
            if similarity_between_main_and_secondary.overall_similarity > similarity_chosen:
                print(f"Similarity between {main_city['city_localisation']} and {df.iloc[secondary_city]['city_localisation']}, {df.iloc[secondary_city]['country_localisation']}: \t{similarity_between_main_and_secondary.overall_similarity}")
        except:
            pass

    create_similarity_external_window.create_window(similarities, similarity_chosen, main_city)
