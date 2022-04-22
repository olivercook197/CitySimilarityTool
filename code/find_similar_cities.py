from functions import autofill_class, attribute_selector, determine_similar_cities
from tkinter import *
import pandas as pd


class FindSimilarCities:
    def __init__(self, inherited_root, df, weighting, attribute_min_max):
        global root
        root = inherited_root
        self.inherited_root = inherited_root
        self.df = df
        self.weighting = weighting
        self.attribute_min_max = attribute_min_max
        self.return_home = False
        global autofill_screen
        autofill_screen = autofill_class.AutofillScreen(root, self.df)

        root.after(200, self.check_if_city_chosen)

    def check_if_city_chosen(self):
        if autofill_screen.city:
            self.city_is_chosen()
        else:
            root.after(200, self.check_if_city_chosen)

    def check_if_attributes_chosen(self):
        if selected_attributes.list_of_attributes and selected_attributes.similarity:
            self.attributes_chosen()
        else:
            root.after(200, self.check_if_attributes_chosen)

    # noinspection PyAttributeOutsideInit
    def city_is_chosen(self):
        self.city = self.df.iloc[autofill_screen.city[0][0] - 1]
        self.attribute_selector()

    def attribute_selector(self):
        global selected_attributes
        selected_attributes = attribute_selector.AttributeSelector(root, self.city)
        root.after(200, self.check_if_attributes_chosen)

    def attributes_chosen(self):
        self.attributes = selected_attributes.list_of_attributes
        self.similarity_chosen = round(selected_attributes.similarity, 2)
        print(self.attributes)
        print(self.similarity_chosen)
        similar_cities = determine_similar_cities.determine_similar_cities_main(self.city, self.attributes,
                                                                                self.similarity_chosen, self.df,
                                                                                self.weighting, self.attribute_min_max,
                                                                                root)
        return_home_button = Button(root, text="Click here to return home", command=self.return_home_command).grid(row=3,
            pady=30)

    def return_home_command(self):
        self.return_home = True
        pass
