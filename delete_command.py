from style_and_layout import styling
from style_and_layout import display_all
import global_data_variables as dv
import heapq
from datetime import datetime
from datetime import datetime
import heapq

def delete_command_by_id(cmd_id):
    initial_len = len(dv.all_commands)
    deleted_cmd = None

    
    for cmd in dv.all_commands:
        if cmd["id"] == cmd_id:
            deleted_cmd = {
                "id": cmd["id"],
                "command": cmd["command"],
                "priority": cmd.get("priority", "N/A"),
                "status": "Deleted",
                "deleted_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            break

    
    dv.all_commands = [cmd for cmd in dv.all_commands if cmd["id"] != cmd_id]

    if len(dv.all_commands) == initial_len:
        return False  

    
    dv.pending_commands_dict.pop(cmd_id, None)
    dv.pending_commands_heap = [(p, c) for p, c in dv.pending_commands_heap if c != cmd_id]
    heapq.heapify(dv.pending_commands_heap)

    
    dv.executed_commands = [cmd for cmd in dv.executed_commands if cmd["id"] != cmd_id]

    
    dv.delete_count += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dv.usage_log.append(f"{dv.BOLD}[{timestamp}]{dv.RESET} 🗑️  Deleted command: '{deleted_cmd['command']}' (ID: {deleted_cmd['id']})")


    
    if deleted_cmd:
        dv.deleted_commands_queue.append(deleted_cmd)

    return True




def delete_command():
    s = styling()
    sorted_commands = sorted(dv.all_commands, key=lambda e: e["priority"])

    if not sorted_commands:
        s.clear_and_show_title()
        print(f"⚠️   No commands to {dv.RED}delete{dv.RESET}.")
        s.line()
        input("\nPress \033[1mENTER\033[0m to continue...")
        s.clear_and_show_title()
        return

    while True:
        s.clear_and_show_title()
        display_all()
        s.line()

        user_input = input(f"{dv.YELLOW}Enter serial number to delete (or 'q' to cancel):{dv.RESET} ").strip()

        if user_input.lower() == 'q':
            s.line()
            print(f"❎{dv.RED} Deletion cancelled.{dv.RESET}")
            s.line()
            input("\nPress \033[1mENTER\033[0m to return...")
            s.clear_and_show_title()
            return

        if not user_input.isdigit():
            s.line()
            print("⚠️  Invalid input. Enter a valid number.")
            s.line()
            continue

        serial_no = int(user_input)
        if not (1 <= serial_no <= len(sorted_commands)):
            s.line()
            print("⚠️  Serial number out of range.")
            s.line()
            continue

        
        cmd_to_delete = sorted_commands[serial_no - 1]
        cmd_id = cmd_to_delete['id']

        if delete_command_by_id(cmd_id):
            s.line()
            print(f"✅ {dv.RED} Command{dv.RESET} '\033[1m{cmd_to_delete['command']}\033[0m'{dv.RED} with serial{dv.RESET} \033[1m{serial_no}\033[0m {dv.RED}and ID{dv.RESET} '\033[1m{cmd_id}\033[0m' {dv.RED}deleted.{dv.RESET}")
        else:
            s.line()
            print("❌ Failed to delete command.")
        s.line()

        input("\nPress \033[1mENTER\033[0m to continue...")
        s.clear_and_show_title()
        break


