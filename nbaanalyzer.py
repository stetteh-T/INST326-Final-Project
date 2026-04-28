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
  pass

def calc_team_avg(players, stat_name):
  pass
  
def compare_players(player1, player2):
  pass

def get_team_choice():
  pass

def get_stat_choice():
  pass

def display_results(team_name, top_players,average, stat_name):
  pass

