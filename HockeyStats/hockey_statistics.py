# Write your solution here
import json

file = input('file name: ')
with open(file) as nhl:
     data = nhl.read()

stats = json.loads(data)
print(f'read the data of {len(stats)} players')

class NHL:
     def __init__(self):
          self.booba = 0

     def player_search(self, name):
          player_stats = list(filter(lambda i: i['name'] == name, stats))[0]
          name = player_stats['name']
          team = player_stats['team']
          goals = player_stats['goals']
          assists = player_stats['assists']
          total = goals + assists
          formatted_string = f"{name:<19}  {team:<3}  {goals:>2} + {assists:>2} = {total:>3}"
          return formatted_string

     def team_players(self, team):
          players = list(filter(lambda i: i['team'] == team, stats))
          sorted_players = list(sorted(players, key=lambda z: z['goals'] + z['assists'], reverse=True))
          final = []
          for i in sorted_players:
               name = i['name']
               team = i['team']
               goals = i['goals']
               assists = i['assists']
               total = goals + assists
               formatted_string = f"{name:<19}  {team:<3}  {goals:>2} + {assists:>2} = {total:>3}"
               final.append(formatted_string)
          return final
     
     def country_players(self, country):
          players = list(filter(lambda i: i['nationality'] == country, stats))
          sorted_players = list(sorted(players, key=lambda z: z['goals'] + z['assists'], reverse=True))
          final = []
          for i in sorted_players:
               name = i['name']
               team = i['team']
               goals = i['goals']
               assists = i['assists']
               total = goals + assists
               formatted_string = f"{name:<19}  {team:<3}  {goals:>2} + {assists:>2} = {total:>3}"
               final.append(formatted_string)
          return final

     def countries(self):
          country_list = list(sorted((list(set([i['nationality'] for i in stats]))), key = lambda z: (z[0], z[1], z[2])))
          return country_list

     def teams(self):
          team_list = list(sorted((list(set([i['team'] for i in stats]))), key = lambda z: (z[0], z[1], z[2])))
          return team_list

     def points(self, n):
          sorted_players = list(sorted(stats, key=lambda z: (z['goals'] + z['assists'], z['goals']), reverse=True))
          final = []
          for i in sorted_players[:n]:
               name = i['name']
               team = i['team']
               goals = i['goals']
               assists = i['assists']
               total = goals + assists
               formatted_string = f"{name:<19}  {team:<3}  {goals:>2} + {assists:>2} = {total:>3}"
               final.append(formatted_string)
          return final


     def goals(self, n):
          sorted_players = list(sorted(stats, key=lambda z: (z['goals'], -z['games']), reverse=True))
          final = []
          for i in sorted_players[:n]:
               name = i['name']
               team = i['team']
               goals = i['goals']
               assists = i['assists']
               total = goals + assists
               formatted_string = f"{name:<19}  {team:<3}  {goals:>2} + {assists:>2} = {total:>3}"
               final.append(formatted_string)
          return final
          

class NHLui:
     def __init__(self):
          self.league = NHL()

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

     def player_search(self):
          player = input('name: ')
          print(self.league.player_search(player))
          
     def teams(self):
          for i in self.league.teams():
               print(i)    

     def countries(self):
          for i in self.league.countries():
               print(i)

     def team_players(self):
          team = input('team: ')
          for i in self.league.team_players(team):
               print(i)
          
     def country_players(self):
          country = input('country: ')
          for i in self.league.country_players(country):
               print(i)
      
     def points(self):
          n = int(input('how many: '))
          for i in self.league.points(n):
               print(i)

     def goals(self):
          n = int(input('how many: '))
          for i in self.league.goals(n):
               print(i)

     def execute(self):
          self.help()
          while True:
               print("")
               command = input("command: ")
               if command == "0":
                    break
               elif command == "1":
                    self.player_search()
               elif command == "2":
                    self.teams()
               elif command == "3":
                    self.countries()
               elif command == "4":
                    self.team_players()
               elif command == "5":
                    self.country_players()
               elif command == "6":
                    self.points()
               elif command == "7":
                    self.goals()                     
               else:
                    self.help()

application = NHLui()
application.execute()