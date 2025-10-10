# Write your solution here
import json

class Player:
    def __init__ (self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.country = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games * -1
        self.total_points = self.goals + self.assists

    def __str__(self):
        return f"{self.name:21}{self.team:>3}  {self.goals:>2} + {self.assists:>2} = {self.total_points:>3}"
    

class GetPlayers:
    def __init__(self):
        self.filename = self.get_filename()
        self.players_obj = []
        self.sorted_lst = []
        self.all_teams = []
        self.all_countries = []

    def get_filename(self):
        if True:
            filename = input("file name: ")
        else:
            filename = "partial.json"
        return filename
       
    def get_obj_players(self):
        with open(self.filename) as my_file:
            data = my_file.read()
        players_json = json.loads(data)
        
        for player in players_json:
            name = player["name"]
            nationality = player["nationality"]
            assists = player["assists"]
            goals = player["goals"]
            penalties = player["penalties"]
            team = player["team"]
            games = player["games"]
            
            new_player = Player(name, nationality, assists, goals, penalties, team, games)
            
            if team not in self.all_teams:
                self.all_teams.append(team)
            
            if nationality not in self.all_countries:
                self.all_countries.append(nationality)

            self.players_obj.append(new_player)
        
        self.sorted_lst = sorted(self.players_obj, key = lambda p: p.total_points, reverse=True)        
        print(f"read the data of {len(self.players_obj)} players")


class HockeyApplication():
    def __init__(self):
        self.__player = GetPlayers()

    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        self.__player.get_obj_players()
        print()
        self.help()

        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                name = input("name: ")
                self.search_player(name)
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                team = input("team: ")
                print()
                self.search_team(team)
            elif command == "5":
                country = input("country: ")
                print()
                self.search_country(country)
            elif command == "6":
                number = int(input("how many: "))
                print()
                self.most_points(number)
            elif command == "7":
                number = int(input("how many: "))
                print()
                self.most_goals(number)
            else:
                help()


    # 1 search for player
    def search_player(self, name):
        for player in self.__player.players_obj:
            if name == player.name:
                print(player)
                break
            else:
                print("unknown player")

    # 2 teams
    def get_teams(self):
        sorted_lst = sorted(self.__player.all_teams)
        for team in sorted_lst:
            print(team)

    # 3 countries
    def get_countries(self):
        sorted_lst = sorted(self.__player.all_countries)
        for country in sorted_lst:
            print(country)

    # 4 players in team
    def search_team(self, team):
        for player in self.__player.sorted_lst:
            if player.team == team:
                print(player)

    # 5 players from country
    def search_country(self, country):
        for player in self.__player.sorted_lst:
            if player.country == country:
                print(player)

    # 6 most points
    def most_points(self, number):
        sorted_lst = sorted(self.__player.players_obj, key = lambda p: (p.total_points, p.goals), reverse=True)[0:number]
        for player in sorted_lst:
            print(player)

    # 7 most goals
    def most_goals(self, number):
        sorted_lst = sorted(self.__player.players_obj, key = lambda p: (p.goals, p.games), reverse=True)[0:number]
        for player in sorted_lst:
            print(player)


# when testing, no code should be outside application except the following:
application = HockeyApplication()
application.execute()
