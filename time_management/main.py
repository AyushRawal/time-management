from interface_mode import run_menu_loop_mode
from facade import DatabaseFacade
import os


def main():
    print("Welcome to Time Management!\n\n")
    database = os.path.join(os.path.dirname(__file__), "time_management.db")
    database_facade = DatabaseFacade(database)
    run_menu_loop_mode(database_facade)


if __name__ == "__main__":
    main()
