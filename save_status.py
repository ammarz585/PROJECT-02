import global_data_variables as dv
from style_and_layout import get_usage_log_entries  # Assumes this returns a list of log strings

def save_status_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("===== MANAGER STATUS =====\n\n")

        # Commands Table
        f.write("-- COMMANDS TABLE --\n")
        if not dv.all_commands:
            f.write("Table empty\n\n")
        else:
            for idx, cmd_data in enumerate(dv.all_commands, 1):
                try:
                    name, priority, status = cmd_data
                    f.write(f"{idx}. Name: {name}, Priority: {priority}, Status: {status}\n")
                except Exception:
                    f.write(f"{idx}. {cmd_data}\n")
            f.write("\n")

        # Deleted Commands Record
        f.write("-- DELETED COMMANDS RECORD --\n")
        if not dv.deleted_commands_queue:
            f.write("Deleted commands record empty\n\n")
        else:
            for idx, deleted_cmd in enumerate(dv.deleted_commands_queue, 1):
                f.write(f"{idx}. {deleted_cmd}\n")
            f.write("\n")

        # Usage Log
        f.write("-- USAGE LOG --\n")
        usage_entries = get_usage_log_entries()
        if not usage_entries:
            f.write("Usage log empty\n")
        else:
            for entry in usage_entries:
                f.write(entry + "\n")
        f.write("\n")

        # Summary Info
        f.write("-- SUMMARY INFO --\n")
        f.write(f"TOTAL_COMMANDS: {len(dv.all_commands)}\n")
        f.write(f"DELETE_COUNT: {dv.delete_count}\n")
        f.write(f"EXECUTED_COMMANDS: {len(dv.executed_commands)}\n")
        f.write(f"PENDING_COMMANDS: {len(dv.pending_commands_dict)}\n")
        f.write(f"ADD_COUNT: {dv.add_count}\n")
        f.write(f"EXECUTION_COUNT: {dv.execution_count}\n")
        f.write(f"UNDO_COUNT: {dv.undo_count}\n")
        f.write(f"REDO_COUNT: {dv.redo_count}\n")
