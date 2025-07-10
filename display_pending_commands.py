import global_data_variables as dv
from tabulate import tabulate  # type: ignore
from style_and_layout import view_pending_commands,styling
s = styling()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pending_commands():
    if not dv.pending_commands_dict and dv.executed_commands:
        s.clear_and_show_title()
        print(f".................{dv.GREEN}NO PENDING COMMANDS\033[0m.................")
        s.line()
        input("\nPress \033[1mENTER\033[0m to return back to menu...")
        s.clear_and_show_title()
    else:
        s.clear_and_show_title()
        print(f"..................{dv.GREEN}PENDING COMMANDS\033[0m..................")
        view_pending_commands()
        s.line()
        input("\nPress \033[1mENTER\033[0m to return back to menu...")
        s.clear_and_show_title()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
