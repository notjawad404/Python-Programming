# Code for generating match fixtures

def matches():
    teams = ["Liverpool", "Manchester City", "Chelsea", "Manchester United", "Arsenal", "Tottenham Hotspur"]
    for home_team in teams:
        print("\n\nHome Team: " + home_team)  # Print the home team
        for away_team in teams:
            if home_team != away_team:  # Check if the home team is not the same as the away team
                print(home_team + " vs " + away_team + " | ", end=" ")  # Print the match fixture

matches()  # Calling the matches function
