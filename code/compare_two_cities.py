from functions import autofill_class, attribute_selector, two_city_comparison, \
    create_two_city_window
from tkinter import *


class CompareTwoCities:
    def __init__(self, inherited_root, df, weighting, attribute_min_max):
        global root
        root = inherited_root
        self.inherited_root = inherited_root
        self.df = df
        self.weighting = weighting
        self.attribute_min_max = attribute_min_max
        self.city = []
        self.return_home = False
        choose_first_city_label = Label(root, text="Choose first city:", font=("Helvetica", 16)).pack()
        global autofill_screen
        autofill_screen = autofill_class.AutofillScreen(root, df)

        root.after(200, self.check_if_city_chosen)

    def check_if_city_chosen(self):
        if autofill_screen.city:
            print(f"First city: {autofill_screen.city[0][1]}")
            global autofill_screen2
            initial_city_label = Label(root, text=f"First city: {autofill_screen.city[0][1]}",
                                       font=("Helvetica", 16)).pack()
            choose_second_city_label = Label(root, text="Choose second city:", font=("Helvetica", 16)).pack()
            autofill_screen2 = autofill_class.AutofillScreen(root, self.df)
            root.after(200, self.check_if_second_city_chosen)
        else:
            root.after(20, self.check_if_city_chosen)

    def check_if_second_city_chosen(self):
        if autofill_screen2.city:
            print(f"Second city: {autofill_screen2.city[0][1]}")
            self.cities_are_chosen()
        else:
            root.after(200, self.check_if_second_city_chosen)

    def cities_are_chosen(self):
        self.city.append(self.df.iloc[int(autofill_screen.city[0][0]) - 1])
        self.city.append(self.df.iloc[int(autofill_screen2.city[0][0]) - 1])
        self.attribute_selector()

    def check_if_attributes_chosen(self):
        if selected_attributes.list_of_attributes:
            self.attributes_chosen()
        else:
            root.after(200, self.check_if_attributes_chosen)

    def attribute_selector(self):
        global selected_attributes
        selected_attributes = attribute_selector.AttributeSelector(root, self.city)
        root.after(200, self.check_if_attributes_chosen)

    def attributes_chosen(self):
        self.attributes = selected_attributes.list_of_attributes
        self.similarity_chosen = round(selected_attributes.similarity, 2)
        print(f"Attributes chosen: {self.attributes}")
        if self.similarity_chosen != 0:
            print(f"Similarity chosen: {self.similarity_chosen}")
        return_home_button = Button(root, text="Click here to return home", command=self.return_home_command).pack(
            pady=30)
        city_similarity = two_city_comparison.TwoCityComparison(self.city, self.attributes,
                                                               self.similarity_chosen, self.df, self.weighting,
                                                               self.attribute_min_max)
        print(f"Similarity: {city_similarity.overall_similarity}")
        create_two_city_window.create_window(self.city, city_similarity.overall_similarity, self.attributes)


    def return_home_command(self):
        self.return_home = True
        pass
