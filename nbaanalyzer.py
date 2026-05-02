import pandas as pd
"""A module for taking, analyzing, and displaying NBA stats"""

class Player:

  def __init__(self, name, team, games, rebounds, points, assists, steals, blocks):
    """Initializes a Player object with statistical data."""

    self.name = name
    self.team = team
    self.rebounds = rebounds
    self.points = points
    self.assists = assists
    self.games = games
    self.steals = steals
    self.blocks = blocks

def load_data(file_name):
  """Loads a CSV file into a pandas DataFrame.

    Args:
        file_name (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the loaded data.
    """
  return pd.read_csv(file_name)

def parsing_data(Newdata):
  """Parses a DataFrame into a list of Player objects.

    Args:
        Newdata (pandas.DataFrame): DataFrame containing player statistics.

    Returns:
        list[Player]: List of Player objects created from the data.
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
  """Groups players by their team.

    Args:
        players (list[Player]): List of Player objects.

    Returns:
        dict[str, list[Player]]: Dictionary mapping team names to lists of players.
    """
  teams = {}
  for player in players:
    if player.team not in teams:
        teams[player.team] = []
    teams[player.team].append(player)
  return teams
  
def get_stat_value(player, stat_name):
  """Gets a specific statistic value from a player.

    Args:
        player (Player): Player object.
        stat_name (str): Statistic name (e.g., 'PPG', 'RPG').

    Returns:
        float or int: Value of the requested statistic.
    """
  stats = {
    'GP': player.games,
    'PPG': player.points,
    'RPG': player.rebounds,
    'APG': player.assists,
    'SPG': player.steals,
    'BPG': player.blocks }
  return stats[stat_name]
  
def rank_players(players, stat_name):
  """Ranks players in descending order based on a specific statistic.

    Args:
        players (list[Player]): List of Player objects.
        stat_name (str): Statistic used for ranking.

    Returns:
        list[Player]: Sorted list of players (highest to lowest).
    """
  return sorted(
    players,
    key = lambda player: get_stat_value(player, stat_name), reverse =True )

def get_top_five(players, stat_name):
  """Gets the top five players based on a specific statistic.

    Args:
        players (list[Player]): List of Player objects.
        stat_name (str): Statistic used for ranking.

    Returns:
        list[Player]: Top five players.
    """
  ranked_players = rank_players(players, stat_name)
  return ranked_players[:5]

def calc_team_avg(players, stat_name):
  """Calculates the average value of a statistic for a team.

    Args:
        players (list[Player]): List of Player objects.
        stat_name (str): Statistic to average.

    Returns:
        float: Average value rounded to one decimal place.
    """
  total = 0
  for player in players:
    total+= get_stat_value(player, stat_name)
  return round(total/len(players),1)
  
def compare_players(player1, player2):
  """Compares two players based on their statistics.

    Args:
        player1 (Player): First player.
        player2 (Player): Second player.

    Note:
        This function is not yet implemented.
    """
  stats = ['GP','PPG', 'RPG', 'APG', 'SPG', 'BPG']

  score1 = 0
  score2 = 0

  print(f"\nPlayer Comparison: {player1.name} vs {player2.name}")
  print("=" * 55)

  for stat in stats:
      val1 = get_stat_value(player1, stat)
      val2 = get_stat_value(player2, stat)
      diff = round(abs(val1 - val2), 2)

      if val1 > val2:
            winner = player1.name
            score1 += 1
      elif val2 > val1:
            winner = player2.name
            score2 += 1
      else:
            winner = "Tie"

      print(f"{stat}: {player1.name} ({val1}) vs {player2.name} ({val2}) "
            f"| Diff: {diff} | Winner: {winner}")

  print("=" * 55)
  
  if score1 > score2:
      overall = player1.name
  elif score2 > score1:
      overall = player2.name
  else:
      overall = "Tie"

  print(f"Overall Winner: {overall}")
  print(f"Category Score -> {player1.name}: {score1}, {player2.name}: {score2}")
    

def get_team_choice(teams):
    """Prompts the user to select a valid team.

    Args:
        teams (dict): Dictionary of teams.

    Returns:
        str: Valid team name entered by the user.
    """
    
    while True:
        team_name = input("Enter a team: ").upper()
        
        if team_name in teams:
            return team_name
        
        print("Invalid team name. Please try again.")

def get_stat_choice():
    """Prompts the user to select a valid statistic.

    Returns:
        str: Normalized statistic abbreviation (e.g., 'PPG', 'RPG').
    """
    
    while True:
        stat = input("Enter a stat: ")
        normalized_stat = normalize_stat(stat)
        
        if normalized_stat is not None:
            return normalized_stat
        
        print("Invalid stat. Choose from PPG, RPG, APG, SPG, BPG, GP.")

def display_results(team_name, top_players, average, stat_name):
  """Displays ranked player results and team average.

    Args:
        team_name (str): Name of the team.
        top_players (list[Player]): Top players list.
        average (float): Team average for the stat.
        stat_name (str): Statistic being displayed.
    """
  print(f"\nTop players for {team_name} by {stat_name}:")
  print("-" * 40)

  for i, player in enumerate(top_players, start=1):
    stat_value = get_stat_value(player, stat_name)
    print(f"{i}. {player.name:<20} {stat_name}: {stat_value}")

  print("-" * 40)
  print(f"Team Average {stat_name}: {average}")

def normalize_stat(stat_name):
  """Normalizes user input into a valid statistic abbreviation.

    Args:
        stat_name (str): User input for a statistic.

    Returns:
        str or None: Normalized stat abbreviation, or None if invalid.
    """
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
