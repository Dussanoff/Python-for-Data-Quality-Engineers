"""
Create a tool which will calculate straight-line distance between different cities based on coordinates:
 1. User will provide two city names by console interface
 2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
 3. Return distance between cities in kilometers
Do not forgot that Earth is a sphere, so length of one degree is different.
"""
import os
import re
import math

from DB import DB


class City:
    connection_string = f"DRIVER={{SQLite3 ODBC Driver}};Direct=True;Database={os.path.join(os.path.dirname(__file__), "outputs", "cities.db")}"
    table = "Cities"
    columns = "City_name, City_coordinates"
    def __init__(self):
        self.db = DB(City.connection_string)
        self.db.create_table(City.table, City.columns)
        self.set_name()
        self.set_coordinates()

    def set_name(self):
        name = input("Provide a city name\n")
        #name = "Salt Lake City"
        if name:
            self.name = name
        else: self.set_name()

    def set_coordinates(self):
        if self.is_exists():
            self.select_coordinates()
            print(f"{self}\n")
        else:
            coordinates = input("Provide a coordinates in Decimal Degrees (DD) format: XX.XXXX° N/S, XX.XXXX° E/W (Latitude: 0 - 90, Longitude: 0 - 180)\n")
            if coordinates:
                lat, long = City.format_coordinates(coordinates)
                self.coordinates = {"latitude" : lat, "longitude" : long}
                self.write_city()
            else: self.set_coordinates()


    def __str__(self):
        return f"City: {self.get_name()}\nLatitude: {self.get_coordinates().get("latitude")}, Longitude: {self.get_coordinates().get("longitude")}"

    def get_db(self):
        return self.db
    def get_name(self):
        return self.name

    def get_coordinates(self):
        return self.coordinates

    def is_exists(self):
        is_exists = False
        db = self.get_db()
        column = City.columns.replace(" ", "").split(",")[0]
        db_table = db.select_from_table(City.table, column)
        for row in db_table.fetchall():
            result = re.sub(r"\(|\)|'|\,", "", str(row).replace("None", "null"))
            if result == self.get_name():
                is_exists = True
        return is_exists

    def select_coordinates(self):
        db = self.get_db()
        name = self.get_name()
        db_table = db.select_from_table(City.table).fetchall()
        for row in db_table:
            if row[0] == name:
                lat, long = City.format_coordinates(row[1])#re.sub(r"\(|\)|'|\,", "", str(row).replace("None", "null"))
                self.coordinates = {"latitude": lat, "longitude": long}

    def write_city(self):
        db = self.get_db()
        name = self.get_name()
        latitude = self.get_coordinates().get("latitude")
        longitude = self.get_coordinates().get("longitude")
        if latitude > 0: coordinates = str(latitude) + "° N,"
        elif latitude < 0: coordinates = str(latitude) + "° S,"
        else: coordinates = str(latitude) + "°,"

        if longitude > 0: coordinates = coordinates + str(longitude) + "° E"
        elif longitude < 0: coordinates = coordinates + str(longitude) + "° W"
        else: coordinates = coordinates + str(longitude) + "°"

        values = f"'{name}', '{coordinates}'"
        db.insert_into_table(City.table, values)

    @staticmethod
    def format_coordinates(coordinates):
        latitude, longitude = coordinates.replace(" ", "").split(",")
        if latitude == "0.0000": lat = 0.0000
        else:
            if latitude[-1] == "S": lat = -float(latitude[:-2].strip())
            elif latitude[-1] == "N": lat = float(latitude[:-2].strip())
            else: print("Incorrect latitude direction, can be only N or S")

        if longitude == "0.0000": long = 0.0000
        else:
            if longitude[-1] == "W": long = -float(longitude[:-2].strip())
            elif longitude[-1] == "E": long = float(longitude[:-2].strip())
            else: print("Incorrect longitude direction, can be only E or W")
        return lat, long


    @staticmethod
    def calculate_distances(city1, city2):
        R = 6371.0

        lat1 = city1.coordinates['latitude']
        lon1 = city1.coordinates['longitude']
        lat2 = city2.coordinates['latitude']
        lon2 = city2.coordinates['longitude']

        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return f"{(R * c)} km"


city1 = City()
city2 = City()

print(City.calculate_distances(city1, city2))



"""
Almaty
43.2380° N, 76.8829° E

Sydney
33.8727° S, 151.2057° E

Salt Lake City
40.7606° N, 111.8881° W

Buenos Aires
34.6037° S, 58.3821° W
"""