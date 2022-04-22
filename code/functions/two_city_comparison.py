from tkinter import *
import numpy as np


class TwoCityComparison:
    def __init__(self, city, attributes, similarity_chosen, df, weighting, attribute_min_max):
        self.city1 = city[0]
        self.city2 = city[1]
        self.attributes = attributes
        self.similarity_chosen = similarity_chosen
        self.df = df
        self.weighting = weighting
        self.attribute_min_max = attribute_min_max
        self.city1data = self.find_city_data(self.city1)
        self.city2data = self.find_city_data(self.city2)

        self.overall_similarity = self.find_city_similarity()

    def normalise_data(self, point1, point2, attribute_num):
        if self.attributes[attribute_num] == "High Temperature":
            point1 -= self.attribute_min_max["high_temp"][0]
            point1 /= (abs(self.attribute_min_max["high_temp"][0] - self.attribute_min_max["high_temp"][1]))
            point2 -= self.attribute_min_max["high_temp"][0]
            point2 /= (abs(self.attribute_min_max["high_temp"][0] - self.attribute_min_max["high_temp"][1]))
        elif self.attributes[attribute_num] == "Low Temperature":
            point1 -= self.attribute_min_max["low_temp"][0]
            point1 /= (abs(self.attribute_min_max["low_temp"][0] - self.attribute_min_max["low_temp"][1]))
            point2 -= self.attribute_min_max["low_temp"][0]
            point2 /= (abs(self.attribute_min_max["low_temp"][0] - self.attribute_min_max["low_temp"][1]))
        elif self.attributes[attribute_num] == "Pressure":
            point1 -= self.attribute_min_max["pressure"][0]
            point1 /= (abs(self.attribute_min_max["pressure"][0] - self.attribute_min_max["pressure"][1]))
            point2 -= self.attribute_min_max["pressure"][0]
            point2 /= (abs(self.attribute_min_max["pressure"][0] - self.attribute_min_max["pressure"][1]))
        elif self.attributes[attribute_num] == "Wind Speed":
            point1 -= self.attribute_min_max["wind_speed"][0]
            point1 /= (abs(self.attribute_min_max["wind_speed"][0] - self.attribute_min_max["wind_speed"][1]))
            point2 -= self.attribute_min_max["wind_speed"][0]
            point2 /= (abs(self.attribute_min_max["wind_speed"][0] - self.attribute_min_max["wind_speed"][1]))
        elif self.attributes[attribute_num] == "Humidity":
            point1 -= self.attribute_min_max["humidity"][0]
            point1 /= (abs(self.attribute_min_max["humidity"][0] - self.attribute_min_max["humidity"][1]))
            point2 -= self.attribute_min_max["humidity"][0]
            point2 /= (abs(self.attribute_min_max["humidity"][0] - self.attribute_min_max["humidity"][1]))
        elif self.attributes[attribute_num] == "Rainfall":
            point1 -= self.attribute_min_max["rainfall"][0]
            point1 /= (abs(self.attribute_min_max["rainfall"][0] - self.attribute_min_max["rainfall"][1]))
            point2 -= self.attribute_min_max["rainfall"][0]
            point2 /= (abs(self.attribute_min_max["rainfall"][0] - self.attribute_min_max["rainfall"][1]))
        elif self.attributes[attribute_num] == "Rainfall Days":
            point1 -= self.attribute_min_max["rainfall_days"][0]
            point1 /= (abs(self.attribute_min_max["rainfall_days"][0] - self.attribute_min_max["rainfall_days"][1]))
            point2 -= self.attribute_min_max["rainfall_days"][0]
            point2 /= (abs(self.attribute_min_max["rainfall_days"][0] - self.attribute_min_max["rainfall_days"][1]))
        elif self.attributes[attribute_num] == "Snowfall":
            point1 -= self.attribute_min_max["snowfall"][0]
            point1 /= (abs(self.attribute_min_max["snowfall"][0] - self.attribute_min_max["snowfall"][1]))
            point2 -= self.attribute_min_max["snowfall"][0]
            point2 /= (abs(self.attribute_min_max["snowfall"][0] - self.attribute_min_max["snowfall"][1]))
        elif self.attributes[attribute_num] == "Snowfall Days":
            point1 -= self.attribute_min_max["snowfall_days"][0]
            point1 /= (abs(self.attribute_min_max["snowfall_days"][0] - self.attribute_min_max["snowfall_days"][1]))
            point2 -= self.attribute_min_max["snowfall_days"][0]
            point2 /= (abs(self.attribute_min_max["snowfall_days"][0] - self.attribute_min_max["snowfall_days"][1]))
        elif self.attributes[attribute_num] == "Daylight":
            point1 -= self.attribute_min_max["daylight"][0]
            point1 /= (abs(self.attribute_min_max["daylight"][0] - self.attribute_min_max["daylight"][1]))
            point2 -= self.attribute_min_max["daylight"][0]
            point2 /= (abs(self.attribute_min_max["daylight"][0] - self.attribute_min_max["daylight"][1]))
        elif self.attributes[attribute_num] == "Sunshine":
            point1 -= self.attribute_min_max["sunshine"][0]
            point1 /= (abs(self.attribute_min_max["sunshine"][0] - self.attribute_min_max["sunshine"][1]))
            point2 -= self.attribute_min_max["sunshine"][0]
            point2 /= (abs(self.attribute_min_max["sunshine"][0] - self.attribute_min_max["sunshine"][1]))
        elif self.attributes[attribute_num] == "Sunshine Days":
            point1 -= self.attribute_min_max["sunshine_days"][0]
            point1 /= (abs(self.attribute_min_max["sunshine_days"][0] - self.attribute_min_max["sunshine_days"][1]))
            point2 -= self.attribute_min_max["sunshine_days"][0]
            point2 /= (abs(self.attribute_min_max["sunshine_days"][0] - self.attribute_min_max["sunshine_days"][1]))
        elif self.attributes[attribute_num] == "UV Index":
            point1 -= self.attribute_min_max["uv_index"][0]
            point1 /= (abs(self.attribute_min_max["uv_index"][0] - self.attribute_min_max["uv_index"][1]))
            point2 -= self.attribute_min_max["uv_index"][0]
            point2 /= (abs(self.attribute_min_max["uv_index"][0] - self.attribute_min_max["uv_index"][1]))
        elif self.attributes[attribute_num] == "Cloud Cover":
            point1 -= self.attribute_min_max["cloud_cover"][0]
            point1 /= (abs(self.attribute_min_max["cloud_cover"][0] - self.attribute_min_max["cloud_cover"][1]))
            point2 -= self.attribute_min_max["cloud_cover"][0]
            point2 /= (abs(self.attribute_min_max["cloud_cover"][0] - self.attribute_min_max["cloud_cover"][1]))



        return point1, point2

    def find_city_similarity(self):
        list_of_similarities = []
        for attribute in range(0, len(self.city1data)):
            set1 = list(self.city1data[attribute][1:-1].split(", "))
            set2 = list(self.city2data[attribute][1:-1].split(", "))
            for i in range(0, len(set1)):
                set1[i] = float(set1[i])
                set2[i] = float(set2[i])
            point1 = np.array(set1)
            point2 = np.array(set2)
            if self.df.iloc[self.city1[0] - 1][21] == "S":
                point1 = np.roll(point1, 6)
            if self.df.iloc[self.city2[0] - 1][21] == "S":
                point2 = np.roll(point2, 6)
            point1, point2 = self.normalise_data(point1, point2, attribute)
            # this is what determines the similarity between different attributes

            altered_euc_dist = np.linalg.norm(point1 * 100/12 - point2 * 100/12)
            similarity = 1 / (1 + altered_euc_dist)
            altered_similarity = 1 / (similarity + altered_euc_dist)
            altered_similarity2 = (1 + 1 - altered_similarity) / (similarity + altered_euc_dist)
            final_altered_similarity = altered_similarity2 - (0.068 / altered_similarity2) * 0.068 + 0.0042
            times_to_add = self.weighting[self.attributes[attribute]]
            for i in range(0, times_to_add):
                list_of_similarities.append(final_altered_similarity)
        if list_of_similarities == []:
            list_of_similarities.append(0)
        overall_similarity = np.mean(list_of_similarities)
        return overall_similarity

    def find_city_data(self, city):
        city_data = []
        if "High Temperature" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][5])
        if "Low Temperature" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][6])
        if "Pressure" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][7])
        if "Wind Speed" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][8])
        if "Humidity" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][9])
        if "Rainfall" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][10])
        if "Rainfall Days" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][11])
        if "Snowfall" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][12])
        if "Snowfall Days" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][13])
        if "Daylight" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][14])
        if "Sunshine" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][15])
        if "Sunshine Days" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][16])
        if "UV Index" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][17])
        if "Cloud Cover" in self.attributes:
            city_data.append(self.df.iloc[city[0] - 1][18])
        return city_data
