import global_data_variables as dv
from style_and_layout import styling
from global_data_variables import RED, GREEN, BLUE, YELLOW, WHITE, BOLD, RESET
import heapq
from datetime import datetime
def add_commands():
    s = styling()
    s.clear_and_show_title()
    print(f"...............{dv.GREEN}COMMANDS QUEUEING CENTRE{dv.RESET}...............")


    user_input = input(F"How many commands do you want to add {dv.RED}(or 'q' to cancel){dv.RESET}: ").strip().lower()
    if user_input == 'q':
        print(f"❎ {dv.RED}Adding Command  cancelled.{dv.RESET}")
        input("Press \033[1mENTER\033[0m to return to menu...")
        s.clear_and_show_title()
        return

    if not user_input.isdigit():
        print("❌ Please enter a valid number.")
        return add_commands()

    count = int(user_input)
    s.line()

    for _ in range(count):
        command_text = input(f"\033[1mEnter {dv.GREEN}command number {_+1}{dv.RESET}: ").strip()
        if not command_text:
            print("⚠️ Empty command skipped.")
            continue
        try:
            priority = int(input(f"\033[1mEnter command {_+1} {dv.YELLOW}priority:\033[0m "))
        except ValueError:
            print("⚠️ Invalid priority. Skipping this command.")
            continue
        s.line()
        cmd_id = str(dv.add_count)
        if any(cmd["command"] == command_text for cmd in dv.all_commands):
            print(f"⚠️ Command '\033[1m{command_text}\033[0m' already exists. Skipping duplicate.")
            continue
        dv.pending_commands_dict[cmd_id] = command_text
        heapq.heappush(dv.pending_commands_heap, (priority, cmd_id))
        dv.all_commands.append({
            "id": cmd_id,
            "command": command_text,
            "priority": priority,
            "status": "pending"
        })
        dv.add_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dv.usage_log.append(f"{dv.BOLD}[{timestamp}]{dv.RESET} ➕ Added command: {command_text}")
        print(f"✅ {dv.GREEN}Added successsfully.{dv.RESET}")
        s.line()

    s.line()
    print(f"\033[1m✅ {dv.GREEN}All commands added successfully.{dv.RESET}\033[0m")
    s.line()
    input("Press \033[1mENTER\033[0m to return to menu...")
    s.clear_and_show_title()

