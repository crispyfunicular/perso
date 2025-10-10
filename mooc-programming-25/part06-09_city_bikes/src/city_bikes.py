# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    station_data = {}
    
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            else:
                station_data[parts[3]] = (float(parts[0]), float(parts[1]))
    
    return station_data


def distance(stations: dict, station1: str, station2: str):
    longitude1 = 0
    longitude2 = 0
    latitude1 = 0
    latitude2 = 0

    #print(stations)
    if station1 in stations:
        longitude1 = stations[station1][0]
        latitude1 = stations[station1][1]
    else:
        raise Exception(f"{station1} not in dictionary")


    if station2 in stations:
        longitude2 = stations[station2][0]
        latitude2 = stations[station2][1]
    else:
        raise Exception(f"{station2} not in dictionary")
    
    #print(longitude1, latitude1)
    #print(longitude2, latitude2)
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance(stations: dict):
    distance_max = 0
    station_max1 = ""
    station_max2 = ""
    for station1 in stations:
        for station2 in stations:
            if distance(stations, station1, station2) > distance_max:
                distance_max = distance(stations, station1, station2)
                station_max1 = station1
                station_max2 = station2
    return(station_max1, station_max2, distance_max)


def main():
    filename = "stations1.csv"
    station_data = get_station_data(filename)
    d = distance(station_data, "Kaivopuisto", "Laivasillankatu")
    print(d)
    print(greatest_distance(station_data))

if __name__ == "__main__":
    main()
