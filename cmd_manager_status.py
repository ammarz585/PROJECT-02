import global_data_variables as dv
from tabulate import tabulate  # type:ignore
from display_pending_commands import view_pending_commands
from style_and_layout import display_all,save_options
from style_and_layout import styling, status_info, print_usage_log, view_deleted_commands, status_options
from global_data_variables import RED, GREEN, BLUE, YELLOW, WHITE, BOLD, RESET
from save_status import save_status_to_file
import os
import time

s = styling()
def display_status_view():
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



def command_manager_status():

    while True:
            display_status_view()
            status_options()
            usage = input("Enter option: ").strip()

            if usage == "1": # show usage logs
                s.clear_and_show_title()
                print(f"....................{dv.GREEN}USAGE LOG{dv.RESET}....................")
                print_usage_log()
                s.line()
                input(f"Press {dv.BOLD}ENTER{dv.RESET} to return to menu...")
            elif usage == "2": # save to file
             option_2()
            elif usage == "3":
                s.clear_and_show_title()
                break
            else:
              #  display_status_view()
              #  status_options()
              #  usage = input("Enter option: ").strip()
                continue







def option_2():
    while True:
        s.clear_and_show_title()
        s.star_line() 
        save_options()

        option = input("Enter option number: ").strip()
        
        if option == "":
            continue

        try:
            option_number = int(option)
        except ValueError:
            continue

        if option_number == 1:
            s.clear_and_show_title()
            filename = input("Enter the filename to save status (e.g., status_log.txt): ").strip()
            if filename == "":
                s.line()
                print(f"{dv.RED}Filename cannot be empty.{dv.RESET} {dv.BLUE}Using default: status_log.txt{dv.RESET}")
                s.line()
                filename = "status_log.txt"
            elif not filename.lower().endswith(".txt"):
                filename += ".txt"  # Append .txt if not present

            save_status_to_file(filename)
            print(f"✅ {dv.GREEN}Status saved to file: {filename}{dv.RESET}")
            s.line()
            input(f"Press {dv.BOLD}ENTER{dv.RESET} to return to Save Menu...")
            break

        elif option_number == 2:
            # Just break this loop to return to previous menu
            break

        else:
            continue


            

       
           