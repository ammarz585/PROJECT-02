from undo_and_redo_command import undo_and_redo
from style_and_layout import styling
import global_data_variables as dv
from style_and_layout import display_all,menu_execution
import heapq
from datetime import datetime

s = styling()
ur = undo_and_redo()
def _set_status(cmd_id, new_status):
    for entry in dv.all_commands:
        if entry["id"] == cmd_id:
            entry["status"] = new_status
            return
def execute_command_by_serial():
    s = styling()

    sorted_list = sorted(dv.all_commands, key=lambda e: e["priority"])

    

    if not dv.pending_commands_heap:
        s.clear_and_show_title()
        print("⚠️  No commands  to execute.")
        s.line()
        input("\nPress \033[1mENTER\033[0m to continue...")
        return False
    s.clear_and_show_title()
    display_all()
    s.line()
    while True:
        serial_input = input("Enter \033[1mS.No\033[0m to execute (or 'q' to cancel): ").strip()

        if serial_input.lower() == 'q':
            s.line()
            print("❎ Execution cancelled.")
            s.line()
            input("Press \033[1mENTER\033[0m to return to menu...")
            s.clear_and_show_title()
            return False

        if not serial_input.isdigit():
            s.clear_and_show_title()
            display_all()
            continue

        serial_no = int(serial_input)

        if not (1 <= serial_no <= len(sorted_list)):
            print("❌ Serial number out of range.")
            input("Press \033[1mENTER\033[0m to try again...")
            
            s.clear_and_show_title()
            display_all()
            continue

        entry = sorted_list[serial_no - 1]

        if entry["status"].lower() == "executed":
            s.line()
            print("\033[1m⚠️ This command has already been executed.\033[0m")
            s.line()
            input("Press \033[1mENTER\033[0m to try again...")
            s.clear_and_show_title()
            display_all()
            continue

        # Proceed with execution
        cmd_id = entry["id"]
        prio = entry["priority"]
        text = entry["command"]

        # Remove from pending structures
        dv.pending_commands_dict.pop(cmd_id, None)
        dv.pending_commands_heap = [(p, c) for p, c in dv.pending_commands_heap if c != cmd_id]
        heapq.heapify(dv.pending_commands_heap)

        # Update status and logs
        _set_status(cmd_id, "Executed")
        dv.execution_stack.append((prio, cmd_id, text))
        dv.undo_stack.clear()
        dv.execution_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        dv.usage_log.append(f"{dv.BOLD}[{timestamp}]{dv.RESET} ✅ Executed command: '{text}' (ID: {cmd_id})")
        dv.executed_commands.append(entry)

        # Display result
        s.line()
        print(f"✅ Executed command: \033[1m'{text}'\033[0m with priority \033[1m{prio}\033[0m.")
        s.line()
        input("\nPress \033[1mENTER\033[0m to continue...")
        s.clear_and_show_title()
        return True

def option_1():

    if not dv.pending_commands_heap:
        s.clear_and_show_title()
        print("⚠️  No commands to execute.")
        s.line()
        input("\nPress \033[1mENTER\033[0m to continue...")
        return  
    s.clear_and_show_title()
    display_all()
    while True:
        s.line()
        user_input = input("Press \033[1mENTER\033[0m to execute top-priority or \033[1m'q'\033[0m to cancel: ").strip().lower()
        if user_input == '':
            break  
        elif user_input == 'q':
            print("❎ Execution cancelled by user.")
            s.line()
            input("\nPress \033[1mENTER\033[0m to return to execution menu...")
            return  
        else:
            s.clear_and_show_title()
            display_all()
            continue 

    # --- Execute command ---
    prio, cmd_id = heapq.heappop(dv.pending_commands_heap)
    text = dv.pending_commands_dict.pop(cmd_id, None)

    _set_status(cmd_id, "Executed")
    dv.execution_stack.append((prio, cmd_id, text))
    dv.undo_stack.clear()
    dv.execution_count += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dv.usage_log.append(f"{dv.BOLD}[{timestamp}]{dv.RESET} ✅ Executed command: '{text}' (ID: {cmd_id})")

    
    dv.executed_commands.append({
        "id": cmd_id,
        "command": text,
        "priority": prio,
        "status": "Executed"
    })

    s.line()
    if text:
        print(f"✅ Executed: '\033[1m{text}\033[0m' with priority {prio}.")
    else:
        print(f"⚠️ Executed: [Unknown ID '{cmd_id}']")
    s.line()

    input("\nPress \033[1mENTER\033[0m to continue...")
    s.clear_and_show_title()

def execute_commands():


    while True:
        menu_execution()
        try:
            choice = int(input("\033[1mEnter option number: \033[0m"))
        except ValueError:
          #  print("Invalid input.")
          #  input("\nPress \033[1mENTER\033[0m to continue...")
            continue

        # 1) Priority-based execution
        if choice == 1:
          option_1()
        # 2) Execute by serial number
        elif choice == 2:
            if execute_command_by_serial():
                pass

        # 3) Undo
        elif choice == 3:
            ur.undo()
            input("\nPress \033[1mENTER\033[0m to continue...")

        # 4) Redo
        elif choice == 4:
            ur.redo()
            input("\nPress \033[1mENTER\033[0m to continue...")

        # 5) Exit
        elif choice <= 5:
            s.clear_and_show_title()
            break
        

        else:
            continue
           # print("Invalid option.")
           # input("\nPress \033[1mENTER\033[0m to continue...")
           


