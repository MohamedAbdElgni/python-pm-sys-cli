from validation import regester_new_user ,login_user
from menu_helpers import helper_sec_menu,helper_first_menu
from pro_helpers import view_all_projects,clear
import json



def run_sec_menu(result):
    while True:
        choice = helper_sec_menu(result)
        
        if choice == "1":
            view_all_projects(result)
            clear()
            run_sec_menu(result)
            break
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            clear()
            main()
            break
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
            continue

def main():
    while True:
        choice = helper_first_menu()
        
        if choice == "1":
            result = regester_new_user()
        elif choice == "2":
            result=login_user()
            if result['status']:
                clear()
                run_sec_menu(result)
                break
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
            continue
        

main()
