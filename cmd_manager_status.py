import global_data_variables as dv
from tabulate import tabulate  # type:ignore
from display_pending_commands import view_pending_commands
from style_and_layout import display_all
from style_and_layout import styling, status_info, print_usage_log, view_deleted_commands, status_options
from global_data_variables import RED, GREEN, BLUE, YELLOW, WHITE, BOLD, RESET

s = styling()

def command_manager_status():
    while True:
        s.clear_and_show_title()
        s.star_line()
        print(f"......................{dv.BOLD}{dv.GREEN}MANAGER STATUS{dv.RESET}.......................")
        s.line()

        print(f"..........{dv.BOLD}{dv.GREEN} COMMANDS TABLE{dv.RESET}..........")
        if not dv.all_commands:
            print("⚠️...............table empty...............")
        else:
            display_all()

        s.line()
        print(f"..........{dv.BOLD}{dv.GREEN}DELETED COMMANDS RECORD{dv.RESET}..........")
        if not dv.deleted_commands_queue:
            print("⚠️...............table empty...............")
        else:
            view_deleted_commands()

        s.line()
        status_info()
        s.line()
        s.star_line()

        status_options()
        usage = input("Enter option: ").strip()

        if usage == "1":
            s.clear_and_show_title()
            print(f"....................{dv.BOLD}USAGE LOG{dv.RESET}....................")
            print_usage_log()
            s.line()
            input(f"Press {dv.BOLD}ENTER{dv.RESET} to return to menu...")
        elif usage == "2":
            s.clear_and_show_title()
            break
        else:
            continue
