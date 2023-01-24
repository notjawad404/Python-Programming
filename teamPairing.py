#
def matches():
    teams = ["Liverpool", "Manchester City", "Chelsea", "Manchester United", "Arsenal", "Tottenham Hotspur"]
    for home_team in teams:
        print("\n\nHome Team: " + home_team)
        for away_team in teams:
            if home_team != away_team:
                print(home_team + " vs " + away_team + " | ", end=" ")


matches()
