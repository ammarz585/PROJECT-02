from style_and_layout import display_all_animated,styling
import global_data_variables as dv
s = styling()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def display():
    if not dv.all_commands:
        s.clear_and_show_title()
        print(".....................\033[1mTABLE EMPTY\033[0m.....................")
        s.line()
        input("\nPress \033[1mENTER\033[0m to return back to menu...")
        s.line()
        s.clear_and_show_title() 
    else:
        s.clear_and_show_title()
        print(f"..........{dv.BOLD}{dv.GREEN} COMMANDS TABLE{dv.RESET}..........")
        display_all_animated()
        s.line()
        input("\nPress \033[1mENTER\033[0m to return back to menu...")
        s.clear_and_show_title()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
