# tee ratkaisu tänne
# Write your solution here
import math

def read_file(filename: str):
    stations_list = []
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            stations_list.append(parts)

    return stations_list

def get_station_data(filename: str):
    stations = read_file(filename)

    stations_dict = {}

    for i in stations:
        stations_dict[i[3]] = (float(i[0]), float(i[1]))
    
    return stations_dict

def distance(stations: dict, station1: str, station2: str):

    for name, coordinates in stations.items():
        if name == station1:
            longitude1 = float(coordinates[0])
            latitude1 = float(coordinates[1])
        elif name == station2:
            longitude2 = float(coordinates[0])
            latitude2 = float(coordinates[1])

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    new_stations = stations.copy()
    distances = []


    for name1, coordinate1 in new_stations.items():
        for name2, coordinate2 in new_stations.items():
            if name1 != name2:
                d = distance(new_stations, name1, name2)
                distances.append((name1, name2, d))

    greatest = distances[0]
    for i in distances:
        if i[2] > greatest[2]:
            greatest = i

    return greatest

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)

    