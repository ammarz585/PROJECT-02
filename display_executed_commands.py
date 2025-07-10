import global_data_variables as dv
from tabulate import tabulate  # type: ignore
from style_and_layout import view_executed_commands,styling
s = styling()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def executed_commands():
    if not dv.executed_commands and dv.pending_commands_dict:
        s.clear_and_show_title()
        print(f".................{dv.GREEN}NO EXECUTED COMMANDS\033[0m.................")
        s.line()
        input("\nPress \033[1mENTER\033[0m to return back to menu...")
        s.clear_and_show_title()
    else:
        s.clear_and_show_title()
        print(f"..................{dv.GREEN}EXECUTED COMMANDS\033[0m..................")
        view_executed_commands()
        s.line()
        input("\nPress \033[1mENTER\033[0m to return back to menu...")
        s.clear_and_show_title()
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        