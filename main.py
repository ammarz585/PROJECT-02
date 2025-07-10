import os
from style_and_layout import styling
from options_controller import option_control
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    s = styling()
    s.print_title()
    while True:

        s.print_options()
        user_input = input("enter option number: ").strip()
        if user_input == "":
            s.clear_and_show_title()
            continue
        
        try:
            option_number = int(user_input)
            if 1 <= option_number <= 8:
                if option_number ==  8: 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("***********\033[1mEXITED PROGRAM\033[0m*************")
                    break
                option_control(option_number)
            else:
               # print("Please enter a valid option.")
               # input("\033[1mPress ENTER to continue..............\033[0m")
                s.clear_and_show_title()
        except ValueError:
            s.clear_and_show_title()

       
##############################################################
main()
##############################################################

