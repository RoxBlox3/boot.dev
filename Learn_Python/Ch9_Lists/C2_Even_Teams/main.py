def split_players_into_teams(players):
    even_team = players[1::2]
    odd_team = players[0::2]
    return odd_team, even_team
