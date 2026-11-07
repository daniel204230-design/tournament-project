import menu as m
from logic import (
    get_and_validate_choice,
    add_team_id,
    add_team_name,
    add_team_details,
    show_teams
    )



def main():
    while True:
        m.main_menu()

        choice = get_and_validate_choice()

        if choice == 0:
            print("Goodbye!")
            break

        elif choice == 1:
            team_id = add_team_id()
            team_name = add_team_name()
            add_team_details(team_id, team_name)


        elif choice == 2:
            show_teams()
            

        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass

        elif choice == 7:
            pass

        elif choice == 8:
            pass

        elif choice == 9:
            pass

        elif choice == 10:
            pass




if __name__ == "__main__":
    main()