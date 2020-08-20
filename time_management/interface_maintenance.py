from interface_common import (
    parse_ascii_banner,
    print_ascii_banner,
    clear_screen,
    quit_program,
    to_previous_menu,
)
import os


def prompt_maintenance():
    banner = os.path.join(os.path.dirname(__file__), "banners/maintenance.txt")
    print_ascii_banner(parse_ascii_banner(banner))
    return input(
        """
0: Return to mode menu
1: Delete history
2: Quit
"""
    )


def run_menu_loop_maintenance(facade):
    while True:
        choice = prompt_maintenance()
        map_choice_to_function(choice, facade)


def map_choice_to_function(choice, facade):
    if choice == "0":
        to_previous_menu(facade)
    elif choice == "1":
        delete_history(facade)
    elif choice == "2":
        quit_program(facade)
    else:
        print("Choice not recognized.")


def delete_history(facade):
    clear_screen()
    choice = input(
        "Are you sure you want to delete your history?\nSubmit 'y' to drop table\nSubmit 'n' to return to maintenance\n"
    )
    if choice == "y":
        print("Deleting history...")
        facade.delete_history()
    elif choice == "n":
        run_menu_loop_maintenance(facade)
