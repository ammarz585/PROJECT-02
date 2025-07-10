import global_data_variables as dv
from style_and_layout import styling
from global_data_variables import RED, GREEN, BLUE, YELLOW, WHITE, BOLD, RESET
import heapq
from datetime import datetime
def add_commands():
    s = styling()
    s.clear_and_show_title()
    print(f"...............{dv.GREEN}COMMANDS QUEUEING CENTRE{dv.RESET}...............")

    # Ask how many commands, support 'q' to cancel
    user_input = input("How many commands do you want to add (or 'q' to cancel): ").strip().lower()
    if user_input == 'q':
        print("❎ Adding Command  cancelled.")
        input("Press \033[1mENTER\033[0m to return to menu...")
        s.clear_and_show_title()
        return

    if not user_input.isdigit():
        print("❌ Please enter a valid number.")
        return add_commands()

    count = int(user_input)
    s.line()

    for _ in range(count):
        command_text = input(f"\033[1mEnter command number {_+1}:\033[0m ").strip()
        if not command_text:
            print("⚠️ Empty command skipped.")
            continue
        try:
            priority = int(input(f"\033[1mEnter command {_+1} priority:\033[0m "))
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
        print(f"✅ Added command \033[1m'{command_text}'\033[0m with priority \033[1m{priority}\033[0m")
        s.line()

    s.line()
    print("\033[1m✅ All commands added successfully.\033[0m")
    s.line()
    input("Press \033[1mENTER\033[0m to return to menu...")
    s.clear_and_show_title()

