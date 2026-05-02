from nbaanalyzer import (
    Player,
    group_players_by_team,
    get_stat_value,
    rank_players,
    get_top_five,
    calc_team_avg,
    normalize_stat
)


def test_group_players_by_team():
    players = [
        Player("Player A", "LAL", 70, 5.0, 25.0, 6.0, 1.0, 0.5),
        Player("Player B", "LAL", 65, 7.0, 20.0, 4.0, 0.8, 1.0),
        Player("Player C", "BOS", 72, 4.0, 18.0, 3.0, 1.2, 0.3)
    ]

    teams = group_players_by_team(players)

    assert len(teams["LAL"]) == 2
    assert len(teams["BOS"]) == 1


def test_get_stat_value():
    player = Player("Player A", "LAL", 70, 5.0, 25.0, 6.0, 1.0, 0.5)

    assert get_stat_value(player, "PPG") == 25.0
    assert get_stat_value(player, "RPG") == 5.0
    assert get_stat_value(player, "APG") == 6.0


def test_rank_players():
    players = [
        Player("Player A", "LAL", 70, 5.0, 25.0, 6.0, 1.0, 0.5),
        Player("Player B", "LAL", 65, 7.0, 20.0, 4.0, 0.8, 1.0),
        Player("Player C", "LAL", 72, 4.0, 30.0, 3.0, 1.2, 0.3)
    ]

    ranked = rank_players(players, "PPG")

    assert ranked[0].name == "Player C"
    assert ranked[1].name == "Player A"
    assert ranked[2].name == "Player B"


def test_get_top_five():
    players = [
        Player("A", "LAL", 70, 1, 10, 1, 1, 1),
        Player("B", "LAL", 70, 1, 20, 1, 1, 1),
        Player("C", "LAL", 70, 1, 30, 1, 1, 1),
        Player("D", "LAL", 70, 1, 40, 1, 1, 1),
        Player("E", "LAL", 70, 1, 50, 1, 1, 1),
        Player("F", "LAL", 70, 1, 60, 1, 1, 1)
    ]

    top_five = get_top_five(players, "PPG")

    assert len(top_five) == 5
    assert top_five[0].name == "F"
    assert top_five[-1].name == "B"


def test_calc_team_avg():
    players = [
        Player("A", "LAL", 70, 5.0, 10.0, 1, 1, 1),
        Player("B", "LAL", 70, 7.0, 20.0, 1, 1, 1),
        Player("C", "LAL", 70, 9.0, 30.0, 1, 1, 1)
    ]

    assert calc_team_avg(players, "PPG") == 20.0
    assert calc_team_avg(players, "RPG") == 7.0


def test_normalize_stat():
    assert normalize_stat("points") == "PPG"
    assert normalize_stat("rebounds") == "RPG"
    assert normalize_stat("assists") == "APG"
    assert normalize_stat("steals") == "SPG"
    assert normalize_stat("blocks") == "BPG"
    assert normalize_stat("games") == "GP"
    assert normalize_stat("random") is None