import heapq
import global_data_variables as dv
from style_and_layout import styling
from datetime import datetime
s = styling()

class undo_and_redo:
    def undo(self):
        if not dv.execution_stack:
            s.line()
            print(f"⚠️...............{dv.GREEN}NOTHING TO UNDO\033[0m...............")
            s.line()
            return

        prio, cmd_id, text = dv.execution_stack.pop()
        dv.undo_stack.append((prio, cmd_id, text))

        dv.pending_commands_dict[cmd_id] = text  
        heapq.heappush(dv.pending_commands_heap, (prio, cmd_id))

        for entry in dv.all_commands:
            if entry["id"] == cmd_id:
                entry["status"] = "Pending"
                break

        dv.undo_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dv.usage_log.append(f"{dv.BOLD}[{timestamp}]{dv.RESET} ↩️  Undo performed on command: '{text}' (ID: {cmd_id})")
        s.line()
        print(f"...............{dv.GREEN}UNDO SUCCESSFUL\033[0m...............")
        print(f"command '\033[1m{text}\033[0m' marked as pending with priority '\033[1m{prio}\033[0m'.")
        s.line()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def redo(self):
        if not dv.undo_stack:
            s.line()
            print(f"⚠️................{dv.GREEN}NOTHING TO REDO\033[0m...............")
            s.line()
            return

        prio, cmd_id, text = dv.undo_stack.pop()   
        dv.execution_stack.append((prio, cmd_id, text))
        dv.pending_commands_dict.pop(cmd_id, None)
        dv.pending_commands_heap = [
            (p, c) for p, c in dv.pending_commands_heap if c != cmd_id
        ]
        heapq.heapify(dv.pending_commands_heap)   
        for entry in dv.all_commands:
            if entry["id"] == cmd_id:
                entry["status"] = "Executed"
                break
        dv.redo_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dv.usage_log.append(f"{dv.BOLD}[{timestamp}]{dv.RESET} 🔁 Redo performed on command: '{text}' (ID: {cmd_id})")
        s.line()
        print(f"...............{dv.GREEN}REDO SUCCESSFUL{dv.RESET}............... ")
        print(f"command '\033[1m{text}\033[0m' marked as executed with  priority '\033[1m{prio}\033[0m' .")
        s.line()
###########################################################################################
