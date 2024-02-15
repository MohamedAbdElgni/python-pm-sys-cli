from validation import regester_new_user ,login_user,del_project,update_project
from menu_helpers import helper_sec_menu,helper_first_menu
from pro_helpers import view_all_projects,clear,create_project




def run_sec_menu(result):
    while True:
        choice = helper_sec_menu(result)

        if choice == "1":
            clear()
            view_all_projects(result)
            clear()
        elif choice == "2":
            clear()
            create_project(result)
            clear()
        elif choice == "3":
            clear()
            del_project(result)
            clear()
        elif choice == "4":
            clear()
            update_project(result)
            clear()
        elif choice == "5":
            clear()
            return
        else:
            print("Invalid choice")
            continue

def main():
    while True:
        clear()
        choice = helper_first_menu()
        
        if choice == "1":
            result = regester_new_user()
        elif choice == "2":
            result=login_user()
            if result['status']:
                clear()
                run_sec_menu(result)
                
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
            continue
        

main()
