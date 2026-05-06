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

def get_impact_score(player):
  
  return round(player.points + player.rebounds 
               + player.assists + player.steals + player.blocks, 1)

def rank_players_by_impact(players):
  return sorted(
    players, key = lambda player: get_impact_score(player), reverse = True)
          
def display_impact_results(team_name, players):
  ranked_players = rank_players_by_impact(players)
  top_players = ranked_players[:5]
  print(f'\n Top 5 All-Around Impact Players for {team_name}:')
  print('-' * 70)

  for i, player in enumerate(top_players, start = 1):
    print(f'{i}, {player.name:<20}'
          f'Impact score: {get_impact_score(player)}'
          f'(PPG: {player.points}, RPG: {player.rebounds}'
          f'APG: {player.assists}, SPG: {player.steals}, BPG: {player.blocks})'
                                        )
  print ('-' * 70)

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
    

def find_player_by_name(players, name):
    """Finds a player by name (case-insensitive).

    Args:
        players (list[Player]): List of Player objects.
        name (str): Player name input.

    Returns:
        Player or None: Matching player if found, otherwise None.
    """
    name = name.strip().lower()

    for player in players:
        if player.name.strip().lower() == name:
            return player

    return None
  
def compare_players_menu(players):
    """Allows user to input two player names and compares them."""

    print("\nPlayer Comparison Mode")
    print("-" * 40)

    name1 = input("Enter Player 1 name: ")
    name2 = input("Enter Player 2 name: ")

    player1 = find_player_by_name(players, name1)
    player2 = find_player_by_name(players, name2)

    if player1 is None:
        print("-" * 40)
        print(f"Player not found: {name1}")
        return

    if player2 is None:
        print(f"Player not found: {name2}")
        return
      
    compare_players(player1, player2)

def get_team_choice(teams):
    """Prompts the user to select a valid team.

    Args:
        teams (dict): Dictionary of teams.

    Returns:
        str: Valid team name entered by the user.
    """
    
    while True:
        team_name = input("\nEnter a team: ").strip().upper()        
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

def main():
  df = load_data("NBA_Data.csv")
  players = parsing_data(df)
  teams = group_players_by_team(players)

  while True:
      print("\nNBA Stats Analyzer")
      print("1. View Top 5 Players by Team")
      print("2. Compare Two Players")
      print('3. View Top 5 Impact Players')
      print("4. Exit")

      choice = input("Select an option: ")

      if choice == "1":
          team_name = get_team_choice(teams)
          stat_name = get_stat_choice()

          team_players = teams[team_name]
          top_players = get_top_five(team_players, stat_name)
          average = calc_team_avg(top_players, stat_name)

          display_results(team_name, top_players, average, stat_name)

      elif choice == "2":
          compare_players_menu(players)
    
      elif choice == '3':
        team_name = get_team_choice(teams)
        team_players = teams[team_name]
        display_impact_results(team_name, team_players)

      elif choice == "4":
          print("Goodbye!")
          break

      else:
          print("Invalid option. Try again.")

if __name__ == "__main__":
  main()
