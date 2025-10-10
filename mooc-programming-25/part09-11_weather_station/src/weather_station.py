# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__observations_lst = []
        self.__latest = ""
    
    def add_observation(self, observation: str):
        self.__observations_lst.append(observation)
        self.__latest = observation

    def latest_observation(self):
        return self.__latest

    def number_of_observations(self):
        return len(self.__observations_lst)

    def __str__(self):
        return f"{self.__name}, {len(self.__observations_lst)} observations"


def main():
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)


if __name__ == "__main__":
    main()
