from interface_common import (
    parse_ascii_banner,
    print_ascii_banner,
    quit_program,
    initialize_menu,
)
from interface_time_management import run_menu_loop_tm
from interface_maintenance import run_menu_loop_maintenance
import os


def prompt_mode():
    initialize_menu(run_menu_loop_mode)
    banner = os.path.join(os.path.dirname(__file__), "banners/mode.txt")
    print_ascii_banner(parse_ascii_banner(banner))
    return input(
        """
1: Time management
2: Analytics
3: Maintenance
4: Quit
"""
    )


def map_choice_to_function(choice, facade):
    if choice == "1":
        initialize_menu(run_menu_loop_tm)
        run_menu_loop_tm(facade)
    elif choice == "2":
        pass
    elif choice == "3":
        initialize_menu(run_menu_loop_maintenance)
        run_menu_loop_maintenance(facade)
    elif choice == "4":
        quit_program(facade)
    else:
        print("Choice not recognized.")


def run_menu_loop_mode(facade):
    while True:
        choice = prompt_mode()
        map_choice_to_function(choice, facade)
