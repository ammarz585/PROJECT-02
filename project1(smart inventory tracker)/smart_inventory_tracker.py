import os 
import tempfile
import glob
import heapq
import pyfiglet # type: ignore
from datetime import datetime
def star_line():
    print("*******************************************************")

def line():
    print("\033[1m-----------------------------------------------------\033[0m")
def print_options():
        star_line()
        print("\033[1mselect option: \033[0m ")
        print("1.add products.")
        print("2.remove products.")
        print("3.display the inventory.")
        print("4.show sorted inventory.")
        print("5.availibility check.")
        print('6.clear all inventory.')
        print("7.inventory status.")
        print("8.open inventory data file.")
        print("\033[1m9..exit program.\033[0m ")
        star_line()
        
class  smart_Inventory_Tracker:
    def __init__(self):
        self.array = {}
        self.add_count = 0
        self.remove_count = 0
        self.usage_log = []  

    def print_title(self):
          ascii = pyfiglet.figlet_format("SMART INVENTORY TRACKING SYSTEM")
          print(ascii)
          
 #-----------------------------------------------------------------------------------------------------

        
    def clear_and_show_title(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_title()
        line()
 #-----------------------------------------------------------------------------------------------------

    def add_item(self):
        self.clear_and_show_title()
        try:
           count = int(input("\033[1menter number of products you want to enter:\033[0m "))
        except ValueError:
            print("Please enter a valid number.")
            return self.add_item()
        line()
         
        for i in range(count):
                item_name = input(f"enter item {i+1} to insert: ").strip().lower()
                self.add_count += 1
                self.usage_log.append(f"add {item_name}")

                try:
                    quantity = int(input("enter the quantity of product: "))
                except ValueError:
                    print("Invalid quantity. Skipping this item.")
                    continue
                line()
                
                if item_name in self.array:
                    self.array[item_name] += quantity
                else:
                    self.array[item_name] = quantity
        now = datetime.now()
        formatted_time = now.strftime("%d-%m-%Y %I:%M %p")           
        line()
        print("\033[1mall items added to inventory\033[0m ")
        line()
        input("\n\033[1mPress Enter to return to menu...\033[0m")
        self.clear_and_show_title()
        
 #-----------------------------------------------------------------------------------------------------
     
    def is_empty(self):
        return len(self.array) == 0
    
 #-----------------------------------------------------------------------------------------------------
    def  display_for_pop(self):
        
        print("\033[1m______INVENTORY STOCK______\033[0m")  
        if self.is_empty():
            print("\033[1mInventory is empty.\033[0m")  
        else:
            for i, (item, quantity) in enumerate(self.array.items(), start=1):
             print(f"{i}. {item} - Quantity: {quantity}") 
        line()
 #-----------------------------------------------------------------------------------------------------

    def remove_item(self):
        self.clear_and_show_title()
        self.display_for_pop()

        if self.is_empty():
            print("\033[1mnothing to remove as the list is empty.\033[0m ")
            input("\n\033[1mPress Enter to return to menu...\033[0m")
            self.clear_and_show_title()
            return

        while True:
            item_to_remove = input("enter item name you want to remove from the inventory items list: ")
            small_case = item_to_remove.lower()

            if small_case in self.array:
                try:
                    quantity = int(input(f"enter number of {small_case} you want to remove: "))
                    if quantity >= self.array[small_case]:
                        del self.array[small_case]
                        print(f"item {small_case} is removed completely.")
                    else:
                       self.array[small_case] -= quantity
                       print(f"{quantity} {small_case} were removed.")
                    self.remove_count -= 1
                    self.usage_log.append(f"remove {small_case}")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("item not found in the inventory.")

            more = input("do you want to remove more items (y/n): ").lower()
            if more != "y":
                input("\n\033[1mPress Enter to return to menu...\033[0m")
                self.clear_and_show_title()
                break

        
#-----------------------------------------------------------------------------------------------------
   
    def display_inventory_record(self):
        self.clear_and_show_title()
        line()
        print("\033[1m______INVENTORY STOCK______\033[0m")  
        if self.is_empty():
            print("\033[1mInventory is empty.\033[0m")  
        else:
           for i, (item, quantity) in enumerate(self.array.items(), start=1):
             print(f"{i}. {item} - Quantity: {quantity}")
        line()
        input("\n\033[1mPress Enter to return to menu...\033[0m")
        self.clear_and_show_title()
 #-----------------------------------------------------------------------------------------------------


    def sorted_inventory(self):
        self.clear_and_show_title()
        if self.is_empty():
            print("\033[1mInventory is empty. Nothing to sort.\033[0m")
            return
        heap = []
        for item in self.array:
            heapq.heappush(heap, item)
        sorted_items = []
        while heap:
            sorted_items.append(heapq.heappop(heap))
        line()
        print(f"\033[1m______SORTED INVENTORY STOCK______:\033[0m")
        for i, item in enumerate(sorted_items, start=1):
            quantity  = self.array[item]
            print(f"\033[1m{i}. {item} - quantity {quantity}\033[0m")
        line()
        input("\n\033[1mPress Enter to return to menu...\033[0m")
        self.clear_and_show_title()
            

#-----------------------------------------------------------------------------------------------------
    def is_available_in_stock(self):
        self.clear_and_show_title() 
        print("AVAILIBILITY CHECK")
        line()
        for i, (item, quantity) in enumerate(self.array.items(), start=1):
            print(f"{i}. {item}")

        availibility_check= input("\033[1mEnter item for availability check:\033[0m ")
        line()
        if self.is_empty():
            print("\033[1mno stock in the inventory\033[0m")
            return 
        if availibility_check in self.array:
                    quantity = self.array[availibility_check]
                    print(f"\033[1m{quantity}  '{availibility_check}' available .\033[0m")

        else:
                    print(f"\033[1mProduct '{availibility_check}' NOT FOUND.\033[0m")
        input("\n\033[1mPress Enter to return to menu...\033[0m")
        self.clear_and_show_title()

  

    
 #-----------------------------------------------------------------------------------------------------
   
 #-----------------------------------------------------------------------------------------------------
    
 

    def inventory_status(self):
        self.clear_and_show_title()

        if self.is_empty():
            print("\033[1mInventory is empty.\033[0m") 
            return 

        total_items = sum(self.array.values())
        unique_total_items = len(self.array)

        print("\033[1m______INVENTORY STATUS_______\033[0m")
        line()
        print(f"the total items altogether are: {total_items} ")
        print(f"the unique items altogether are: {unique_total_items}.")
        print(f"\033[1mthe add count is: {self.add_count}.\033[0m ")
        print(f"\033[1mthe remove count is: {self.remove_count}.\033[0m ")
        line()
        print("\033[1mDETAILED INVENTORY STOCKS:\033[0m ")
        for i, (item, quantity) in enumerate(self.array.items(), start=1):
            print(f"{i}. {item} - Quantity: {quantity}")
        line()

        now = datetime.now()
        formatted_time = now.strftime("%d-%m-%Y %I:%M %p")
        print(f"\033[1mStatus updated on:\033[0m {formatted_time}")

        print_option = input("\n\033[1mDo you want to print and save this inventory status? (y/n): \033[0m").strip().lower()
        if print_option == 'y':
            custom_name = input("\033[1mEnter a custom name for the inventory report file (no extension): \033[0m").strip()
            folder = "D:\\internship\\DSA\\projects\\project1(smart inventory tracker)"
            filename = os.path.join(folder, f"{custom_name}.txt")

            with open(filename, 'w') as f:
                f.write("SMART INVENTORY TRACKER - STATUS REPORT\n")
                f.write(f"Status updated on: {formatted_time}\n\n")
                f.write(f"Total Items: {total_items}\n")
                f.write(f"Unique Items: {unique_total_items}\n")
                f.write(f"Add Count: {self.add_count}\n")
                f.write(f"Remove Count: {self.remove_count}\n\n")
                f.write("------ DETAILED STOCKS ------\n")
                for i, (item, quantity) in enumerate(self.array.items(), start=1):
                    f.write(f"{i}. {item} - Quantity: {quantity}\n")

            print("\033[1mReport saved and sending to printer...\033[0m")
            os.startfile(filename, "print")
            input("\n\033[1mPress Enter to return to menu...\033[0m")
            self.clear_and_show_title()
        else:
             input("\n\033[1mPress Enter to return to menu...\033[0m")
             self.clear_and_show_title()

        
        
        
        
 #-----------------------------------------------------------------------------------------------------
        
    def clear_inventory(self):
        self.clear_and_show_title()
        if self.is_empty():
            print("inventory is already empty")
            return 
        else:
            self.array.clear()
            print("\033[1mall the inventory records were cleared.\033[0m")  
        input("\n\033[1mPress Enter to return to menu...\033[0m")
        self.clear_and_show_title()
        
 #-----------------------------------------------------------------------------------------------------
    def open_inventory_data_file(self):
        self.clear_and_show_title()
    
        folder = "D:\\internship\\DSA\\projects\\project1(smart inventory tracker)"
        pattern = os.path.join(folder, "*.txt")

        while True:
            print("\n\033[1mAvailable saved inventory records:\033[0m")

            report_files = glob.glob(pattern)
            if not report_files:
                print("\033[1mNo saved inventory reports found.\033[0m")
                break

            available_files = [os.path.splitext(os.path.basename(f))[0] for f in report_files]
            for idx, fname in enumerate(available_files, start=1):
                print(f"{idx}. {fname}")

            choice = input("\n\033[1mEnter number or exact name of the report to open: \033[0m").strip()

            selected_file = None
            if choice.isdigit():
                index = int(choice) - 1
            if 0 <= index < len(available_files):
                selected_file = os.path.join(folder, available_files[index] + ".txt")
            else:
                if choice in available_files:
                    selected_file = os.path.join(folder, choice + ".txt")

            if selected_file and os.path.exists(selected_file):
                os.startfile(selected_file)
                print(f"\033[1mOpened file: {os.path.basename(selected_file)}\033[0m")
            else:
                print("\033[1mInvalid selection or file does not exist.\033[0m")

            cont = input("\n\033[1mDo you want to open another report? (y/n): \033[0m").strip().lower()
            if cont != 'y':
                self.clear_and_show_title()
                input("\n\033[1mPress Enter to return to menu...\033[0m")
                self.clear_and_show_title()
                
                break

 #-----------------------------------------------------------------------------------------------------

   
#################################################
def option_control(option_number,s):
        option  = {
            1: s.add_item,
            2: s.remove_item,
            3: s.display_inventory_record,
            4: s.sorted_inventory,
            5: s.is_available_in_stock,
            6: s.clear_inventory,
            7: s.inventory_status,
            8: s.open_inventory_data_file 
        }
        selected_function = option.get(option_number,lambda: print("invalid optiion.....!"))
        selected_function()
###################################################
def main():
    s = smart_Inventory_Tracker()
    s.print_title()
    star_line()
    
    print("\033[1mwelcome to smart inventory tracking system....................> \033[0m ")
    while True:
        print_options()
        
        user_input = input("enter option number: ").strip()
        
        if user_input == "":
            print("Input cannot be empty. Please enter a valid option.")
            input("\033[1mPress any key to continue..............\033[0m")
            s.clear_and_show_title()
            continue
        
        try:
            option_number = int(user_input)
            if 1 <= option_number <= 9:
                if option_number == 9:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\033[1m***********exited program*************\033[0m")
                    break
                option_control(option_number, s)
            else:
                print("Please enter a valid option.")
                input("\033[1mPress any key to continue..............\033[0m")
                s.clear_and_show_title()
        except ValueError:
            print("Please enter a valid option.")
            input("\033[1mPress any key to continue..............\033[0m")
            s.clear_and_show_title()

       
##############################################################
main()
##############################################################
