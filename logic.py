from data_teams import teams, matches

        # print menu
        # get input data & validate
        # handle user navigation
        

def get_and_validate_choice():
    while True:        
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print()
            print("Invalid choice")
            print("Choice must be an integer\nTry again\n\n")
            continue
        else: 
            if not choice in range(11):
                print()
                print("Invalid choice")
                print("Choice must be one of the menu's options\nTry again\n\n")
                continue
            
            return choice


def is_exist(key, val):
    for team in teams:
        if key == "name":
            val = val.lower()
            team_name = team[key].lower()
        else:
            team_name = team[key]

        if team_name == val:
            print()
            print(f"Invalid {key}")
            print(f"{key} is already exist")
            print(f"Chose a different {key}\n")
            return True
    return False


def add_team_id():
    while True:
        try:
            team_id = int(input("Enter team ID: "))
        except ValueError:
            print()
            print("Invalid choice")
            print("Choice must be an integer\nTry again\n\n")
            continue
        else:     
            if team_id <= 0:
                print()
                print("Invalid choice")
                print("Choice must be positive\nTry again\n\n")
                continue
            
            if is_exist("id", team_id):
                continue

            return team_id


def add_team_name():
    while True:
        team_name = input("Enter taem name: ").strip()

        if not team_name:
            print()
            print("Invalid name")
            print("Name cannot be empty")
            continue

        if is_exist("name", team_name):
                continue

        return team_name


def add_team_details(team_id, team_name):
    new_team = {
        "id": team_id, "name": team_name, "played": 0,
        "wins": 0, "draws": 0, "losses": 0,
        "goals_for": 0, "goals_against": 0, "points": 0
    }
    
    teams.append(new_team)
    print("\nThe team added sucssfully!")
    print()

    return new_team


def show_teams():
    if not teams:
        print("There is no any teams yet...")
        print("Please try again later\n")
        return

    for team in teams:
        print(f"\nTeam ID: {team["id"]}\nTeam name: {team["name"]}\nPlayed: {team["played"]}\nPoints: {team["points"]}\n")
    
def is_id_exist(team_id):
    for team in teams:
        if team["id"] == team_id:
            return True
    return False

def add_and_validate_maches():
    while True:
        home_team_id = input("Enter home team ID: ")
        away_team_id = input("Enter away team ID: ")
        
        if not is_id_exist(home_team_id) and not is_id_exist(away_team_id):
            print()
            print(f"Invalid ID")
            print(f"ID is not exist")
            print(f"Chose a different id\n")
            continue
            
        if home_team_id == away_team_id:
            print()
            print("The teams must not be identical")
            continue

# def (): 
# home_goals, away_goals
        





