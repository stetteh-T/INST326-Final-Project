import pandas as pd
"""A module for taking, analyzing, and displaying NBA stats"""

class Player:

  def __init__(self, name, team, games, rebounds, points, assists, steals, blocks):
    self.name = name
    self.team = team
    self.rebounds = rebounds
    self.points = points
    self.assists = assists
    self.games = games
    self.steals = steals
    self.blocks = blocks

def load_data(file_name):
  """A function that loads a data file into pandas df
  Args: file_name: file that is loaded 
  """
  return pd.read_csv(file_name)

def parsing_data(Newdata):
  
  """A function for parsing data
    
    Args: Newdata: df of data that is parsed
  """
  players = []
  for _, row in Newdata.iterrows():
    player = Player(
      row['Player'],
      row['Team'],
      int(row['GP']),
      float(row['RPG']),
      float(row['PPG']),
      float(row['APG']),
      float(row['SPG']),
      float(row['BPG']),
    )
    players.append(player)
  return players

def group_players_by_team(players):
  """A function that groups NBA players into their seperate teams
  Args: players: list of players objects"""
  teams = {}
  for player in players:
    if player.team not in teams:
         teams[player.team] = []
    teams[player.team].append(player)
  return teams
  
def get_stat_value(player, stat_name):
  stats = {
    'GP': player.games,
    'PPG': player.points,
    'RPG': player.rebounds,
    'APG': player.assists,
    'SPG': player.steals,
    'BPG': player.blocks }
  return stats[stat_name]
  
def rank_players(players, stat_name):
  """A function that ranks players by a certain stat
  Args: players: list of player objects
        stat_name: name of the stat that players are being ranked by
        """
  return sorted(
    players,
    key = lambda player: get_stat_value(player, stat_name), reverse =True )

def get_top_five(players, stat_name):
  ranked_players = rank_players(players, stat_name)
  return ranked_players[:5]

def calc_team_avg(players, stat_name):
  total = 0
  for player in players:
    total+= get_stat_value(player, stat_name)
  return round(total/len(players),1)
  
def compare_players(player1, player2):
  pass

def get_team_choice(teams):
    """Prompt user to enter a team name"""
    
    while True:
        team_name = input("Enter a team: ").title()
        
        if team_name in teams:
            return team_name
        
        print("Invalid team name. Please try again.")

def get_stat_choice():
    """Prompt user to enter a stat"""
    
    while True:
        stat = input("Enter a stat: ")
        normalized_stat = normalize_stat(stat)
        
        if normalized_stat is not None:
            return normalized_stat
        
        print("Invalid stat. Choose from PPG, RPG, APG, SPG, BPG, GP.")

def display_results(team_name, top_players, average, stat_name):
  print(f"\nTop players for {team_name} by {stat_name}:")
  print("-" * 40)

  for i, player in enumerate(top_players, start=1):
    stat_value = get_stat_value(player, stat_name)
    print(f"{i}. {player.name:<20} {stat_name}: {stat_value}")

  print("-" * 40)
  print(f"Team Average {stat_name}: {average}")

def normalize_stat(stat_name):
  stat_aliases = {
    'GAMES': 'GP',
    'GAME': 'GP',
    'GP': 'GP',

    'POINTS': 'PPG',
    'POINT': 'PPG',
    'PPG': 'PPG',

    'REBOUNDS': 'RPG',
    'REBOUND': 'RPG',
    'RPG': 'RPG',

    'ASSISTS': 'APG',
    'ASSIST': 'APG',
    'APG': 'APG',

    'STEALS': 'SPG',
    'STEAL': 'SPG',
    'SPG': 'SPG',

    'BLOCKS': 'BPG',
    'BLOCK': 'BPG',
    'BPG': 'BPG'
  }

  return stat_aliases.get(stat_name.upper())
