import csv
import pandas as pd
"""A module for taking, analyzing, and displaying NBA stats"""

def load_data(file_name):
  """A function that loads a data file into pandas df
  Args: file_name: file that is loaded 
  """
  df = pd.read_csv(file_name)
  
def parsing_data(Newdata):
    """A function for parsing data
    Args: Newdata: df of data that is parsed"""
    pass

class Player:
  pass
  
  def __init__(self, name, team, rebounds,points, assists):
    pass

def group_players_by_team(players):
  """A function that groups NBA players into their seperate teams
  Args: players: list of players objects"""
  pass

def rank_players(players, stat_name):
  """A function that ranks players by a certain stat
  Args: players: list of player objects
        stat_name: name of the stat that players are being ranked by
        """
  pass

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

