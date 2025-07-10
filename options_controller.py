from add_command import add_commands  
from execution_controller import execute_commands
from display_pending_commands import pending_commands
from display_executed_commands import executed_commands
from cmd_manager_status import command_manager_status
from display_all_commands import display
from delete_command import delete_command

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def option_control(option_number):
        option  = {
            1: add_commands,
            2: execute_commands,
            3: display,
            4: pending_commands,
            5: executed_commands,
            6: command_manager_status,
            7:delete_command
            
        }
        selected_function = option.get(option_number,lambda: print("invalid optiion.....!"))
        selected_function()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
