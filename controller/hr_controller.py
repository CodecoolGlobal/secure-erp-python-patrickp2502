from operator import truediv
from signal import pthread_sigmask
from webbrowser import get
from model.hr import hr
from view import terminal as view


def list_employees():
    list_employees = hr.get_hr_data()
    view.print_table(list_employees)



def get_valid_name():
    while True:
        name = view.get_input("Enter Name: ")
        if len(name) > 0:
            break
        view.print_error_message("Please provide a name")
    return name


def get_valid_date():    
    while True:
        try:
            valid_birth_date = view.get_input("Birth date (YYYY-MM-DD): ")
            if is_valid_birthdate(valid_birth_date):
                return valid_birth_date
            else:
                raise ValueError
        except ValueError:
            view.print_error_message("Please provide a datum Format YYYY-MM-DD")
            continue


def get_valid_department():
    while True:
        valid_department = view.get_input("Enter department: ")
        if valid_department != None:
            break
        view.print_error_message("Please provide department: ")
    return valid_department


def get_valid_clearance_level():
    while True:
        try:
            clearance_level_str = view.get_input("Clearance level from 0 lowest to 7 highest:")
            valid_clearance_level = int(clearance_level_str)
            if hr.CLEARANCE_LEVEL_LOW <= valid_clearance_level <= hr.CLEARANCE_LEVEL_HIGH:
                break 
        except ValueError:
            view.print_error_message("Please provide a number between 1 and 7!")
    return valid_clearance_level


def is_valid_birthdate(birth_date):
    return int(birth_date[:4]) > 0 and 1 <= int(birth_date[5:7]) <= 12 and \
                    1 <= int(birth_date[8:10]) <= 31 and birth_date[4] == "-" and \
                    birth_date[7] == "-"


def add_employee():
    view.print_message("Please provide information of new employee")
    name = get_valid_name()
    birth_date = get_valid_date()
    department = get_valid_department()
    clearance_level = get_valid_clearance_level()
    hr.add_data(name, birth_date, department, clearance_level)


def update_employee():
    view.print_message("Update User Data")
    user_data = get_valid_user_data()
    



def get_valid_user_data():
    while True:
        try:
            user_id = view.get_input("User-ID: ")
            user_data = hr.get_user_data(user_id)
            return user_data
        except IndexError:
            view.print_error_message(f"Couldn't find user ID: {user_id}")
            continue
    




def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
