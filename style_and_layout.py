import pyfiglet #type:ignore
import os
import global_data_variables as dv
from tabulate import tabulate#type:ignore 
from global_data_variables import RED, GREEN, BLUE, YELLOW, WHITE, BOLD, RESET
import time
import sys
class styling:
    def star_line(self):
        print("*******************************************************")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def line(self):
        print("\033[1m-----------------------------------------------------\033[0m")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def print_options(self):
        self.star_line()
        print(f"....................{dv.GREEN}OPTIONS MENU{dv.RESET}.................... ")
        print(f"{dv.GREEN}{dv.BOLD}1.{dv.RESET} {dv.BOLD}Add commands               {dv.GREEN}2.{dv.RESET} {dv.BOLD}Execute commands.{dv.RESET}")
        print(f"{dv.GREEN}{dv.BOLD}3.{dv.RESET} {dv.BOLD}Display all commands       {dv.GREEN}4.{dv.RESET} {dv.BOLD}View pending commands{dv.RESET}")
        print(f"{dv.GREEN}{dv.BOLD}5.{dv.RESET} {dv.BOLD}View executed commands     {dv.GREEN}6.{dv.RESET} {dv.BOLD}Commands status{dv.RESET}")
        print(f"{dv.GREEN}{dv.BOLD}7.{dv.RESET} {dv.BOLD}Delete command             {dv.GREEN}8.{dv.RESET} {dv.RED}{dv.BOLD}Exit command manager{dv.RESET}")
        self.star_line()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def print_title(self):
          ascii = pyfiglet.figlet_format("SMART COMMAND MANAGER")
          print(ascii)
          
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 

    def clear_and_show_title(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_title()
        self.line()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

s = styling()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_usage_log():
    if not dv.usage_log:
        print("⚠️.....No usage logs available......")
        return
    for idx, log_entry in enumerate(dv.usage_log, start=1):
        print(f"{dv.BOLD}{idx}{dv.RESET}. {dv.YELLOW}{log_entry}{dv.RESET}")
def get_usage_log_entries():
    # Assuming you have some internal log list, e.g. dv.usage_log
    usage_log = getattr(dv, 'usage_log', [])

    if not usage_log:
        return ["Usage log empty"]

    # Prepare list of log entries (strings)
    return [str(entry) for entry in usage_log]
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def display_all():
    rows = []
    for idx, entry in enumerate(sorted(dv.all_commands, key=lambda e: e["priority"])):        
        rows.append({
            "S.No": idx + 1,
            "Cmd ID": f"{dv.YELLOW}{entry['id']}{dv.RESET}",
            "Command": f"{dv.BLUE}{entry['command']}{dv.RESET}",
            "Priority": f"{dv.RED}{entry['priority']}{dv.RESET}",
            "Status": f"{dv.GREEN}{entry['status'].capitalize()}{dv.RESET}"
        })
    print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def display_all_animated():
    rows = []
    for idx, entry in enumerate(sorted(dv.all_commands, key=lambda e: e["priority"])):        
        rows.append({
            "S.No": idx + 1,
            "Cmd ID": f"{dv.YELLOW}{entry['id']}{dv.RESET}",
            "Command": f"{dv.BLUE}{entry['command']}{dv.RESET}",
            "Priority": f"{dv.RED}{entry['priority']}{dv.RESET}",
            "Status": f"{dv.GREEN}{entry['status'].capitalize()}{dv.RESET}"
        })
    
    table_str = tabulate(rows, headers="keys", tablefmt="fancy_grid")
    animated_tabulate_print(table_str=table_str)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_pending_commands():
    rows = []
    for idx, entry in enumerate(dv.all_commands):
        if entry["status"].lower() == "pending":
            rows.append({
                "S.No": idx + 1,
                "Cmd ID": f"{dv.YELLOW}{entry['id']}{dv.RESET}",
                "Command": f"{dv.BLUE}{entry['command']}{dv.RESET}",
                "Priority": f"{dv.RED}{entry['priority']}{dv.RESET}"
            })
    table_str = tabulate(rows, headers="keys", tablefmt="fancy_grid")
    animated_tabulate_print(table_str=table_str)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def view_executed_commands():
    rows = []
    for idx, entry in enumerate(dv.all_commands):
        if entry["status"].lower() == "executed":
            rows.append({
                "S.No": idx + 1,
                "Cmd ID": f"{dv.YELLOW}{entry['id']}{dv.RESET}",
                "Command": f"{dv.BLUE}{entry['command']}{dv.RESET}",
                "Priority": f"{dv.RED}{entry['priority']}{dv.RESET}"
            })
    table_str = tabulate(rows, headers="keys", tablefmt="fancy_grid")
    animated_tabulate_print(table_str=table_str)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def view_deleted_commands():
    rows = []
    for idx, entry in enumerate(dv.deleted_commands_queue):
        rows.append({
            "S.No": idx + 1,
            "Cmd ID": f"{dv.YELLOW}{entry.get('id', 'N/A')}{dv.RESET}",
            "Command": f"{dv.BLUE}{entry.get('command', 'N/A')}{dv.RESET}",
            "Priority": f"{dv.RED}{entry.get('priority', 'N/A')}{dv.RESET}",
            "Status": f"{dv.GREEN}{entry.get('status', 'N/A').capitalize()}{dv.RESET}",
            "Deleted At": f"{dv.WHITE}{entry.get('deleted_timestamp', 'N/A')}{dv.RESET}"
        })
    print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def status_info():
    print(f"{dv.WHITE}{dv.BOLD}TOTAL_COMMANDS:{dv.RESET} {dv.BOLD}{len(dv.all_commands)}{dv.RESET}")
    print(f"{dv.WHITE}{dv.BOLD}DELETE_COUNT {dv.RED}:{dv.RESET} {dv.RED}{dv.BOLD}{dv.delete_count}{dv.RESET}")
    print(f"{dv.BLUE}{dv.BOLD}EXECUTED{dv.RESET}-{dv.WHITE}{dv.BOLD}COMMANDS:{dv.RESET} {dv.BLUE}{dv.BOLD}{len(dv.executed_commands)}{dv.RESET}")
    print(f"{dv.YELLOW}{dv.BOLD}PENDING{dv.RESET}-{dv.WHITE}{dv.BOLD}COMMANDS:{dv.RESET} {dv.YELLOW}{dv.BOLD}{len(dv.pending_commands_dict)}{dv.RESET}")
    print(f"{dv.YELLOW}{dv.BOLD}ADD_COUNT:{dv.RESET} {dv.YELLOW}{dv.BOLD}{dv.add_count}{dv.RESET}")
    print(f"{dv.GREEN}{dv.BOLD}EXECUTION_COUNT:{dv.RESET} {dv.GREEN}{dv.BOLD}{dv.execution_count}{dv.RESET}")
    print(f"{dv.RED}{dv.BOLD}UNDO{dv.RESET}_{dv.WHITE}{dv.BOLD}COUNT:{dv.RESET} {dv.RED}{dv.BOLD}{dv.undo_count}{dv.RESET}")
    print(f"{dv.GREEN}{dv.BOLD}REDO{dv.RESET}_{dv.WHITE}{dv.BOLD}COUNT:{dv.RESET} {dv.GREEN}{dv.BOLD}{dv.redo_count}{dv.RESET}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def status_options():
        print(f"....................{dv.BOLD}{dv.GREEN}OPTIONS MENU{dv.RESET}.................... ")
        print(f"{dv.GREEN}{dv.BOLD}1.{dv.RESET} {dv.BOLD}show usage logs               {dv.GREEN}{dv.BOLD}2.{dv.RESET} {dv.BOLD}status save option{dv.RESET}")
        print(f"{dv.GREEN}{dv.BOLD}3.{dv.RESET} {dv.BOLD}return to menu{dv.RESET}")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
        
def menu_execution():
    s.clear_and_show_title()
    s.star_line()
    print(f"....................{dv.GREEN}EXECUTION MENU{dv.RESET}....................")
    print(f"{dv.GREEN}{dv.BOLD}1.{dv.RESET} {dv.BOLD}Execute next command          {dv.GREEN}2.{dv.RESET} {dv.BOLD}Execute by S.No{dv.RESET}")
    print(f"{dv.GREEN}{dv.BOLD}3.{dv.RESET} {dv.BOLD}Undo last execution           {dv.GREEN}4.{dv.RESET} {dv.BOLD}Redo last undo{dv.RESET}")
    print(f"{dv.GREEN}{dv.BOLD}5.{dv.RESET} {dv.RED}Return to main menu{dv.RESET}")
    s.star_line()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def save_options():
    print(f"....................{dv.GREEN}SAVE OPTIONS{dv.RESET}....................")
    print(f"{dv.GREEN}{dv.BOLD}1.{dv.RESET} {dv.BOLD}save status to file          {dv.GREEN}2.{dv.RESET} {dv.BOLD}cancel save{dv.RESET}")
    




def animated_tabulate_print(table_str, delay=0.07, show_loader=True):
    if show_loader:
        print("📋 Loading Table", end="", flush=True)
        for _ in range(5):  # 3 dots over ~1.5 seconds
            time.sleep(0.7)
            print(".", end="", flush=True)
        print("\r" + " " * 40 + "\r", end="")  # Clear loading line

    for line in table_str.split('\n'):
        print(line)
        time.sleep(delay)
    print()
