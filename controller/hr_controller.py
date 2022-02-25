from model.hr import hr
from view import terminal as view

def list_employees():
    list_employees = hr.get_hr_data()
    view.print_table(list_employees, hr.HEADERS)



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
    valid_clearance_level_string = str(valid_clearance_level)
    return valid_clearance_level_string


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
    
    user_data = get_valid_user_data_by_id()
    # view.print_table(user_data)
    new_name = get_valid_name()
    new_birthdate = get_valid_date()
    new_department = get_valid_department()
    new_clearance_level = get_valid_clearance_level()

    user_data[1] = new_name
    user_data[2] = new_birthdate
    user_data[3] = new_department
    user_data[4] = new_clearance_level
    hr.update_data(user_data)


def get_valid_user_data_by_id():
    while True:
        try:
            user_id = view.get_input("User-ID: ")
            user_data = hr.get_user_data(user_id)
            return user_data
        except IndexError:
            view.print_error_message(f"Couldn't find user ID: {user_id}")
            continue
    


def delete_employee():
    view.print_message("Delete a Employee")
    user_data = get_valid_user_data_by_id()
    # view.print_table(user_data)
    hr.delete_employee_data(user_data)
    

def get_oldest_and_youngest():
    print(hr.get_names_of_oldest_and_youngest())


def get_average_age():
    todays_date = input("What's todays date(YYYY-MM-DD)?")
    print(hr.average_age_calculator(todays_date))


def next_birthdays():
    date = input("Enter a date to calculate the birthdays around this date(YYYY-MM-DD):")
    print(hr.get_next_birthdays(date))


def count_employees_with_clearance():
    clearance = input("Which clearance level are you filtering for?")
    print(hr.check_for_clearance(clearance))


def count_employees_per_department():
    print(hr.show_department_employees())


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
