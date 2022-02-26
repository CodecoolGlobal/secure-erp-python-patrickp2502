""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

import string
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
CLEARANCE_LEVEL_LOW = 0
CLEARANCE_LEVEL_HIGH = 7


def get_hr_data():
   
    all_data = data_manager.read_table_from_file(DATAFILE)
    
    return all_data


def add_data(name: string, birth_date: string, department: string, clearance_level):
    all_data = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id()
    clearance_level_string = clearance_level
    data_to_save = [id, name, birth_date, department, clearance_level_string]
    all_data.append(data_to_save)
    data_manager.write_table_to_file(DATAFILE, all_data)


def get_user_data(user_id):
    data_list = get_hr_data()
    user_index = get_user_index_by_id(data_list, user_id)
    user_data = data_list[user_index]
    return user_data



def update_data(updated_user_data):
    user_id = updated_user_data[0]
    all_data = get_hr_data()
    user_data_index = get_user_index_by_id(all_data, user_id)
    all_data[user_data_index] = updated_user_data
    data_manager.write_table_to_file(DATAFILE, all_data)
    

def get_user_index_by_id(data, user_id):
    for index in range(len(data)):
        if data[index][0] == user_id:
            return index 
    else:
        raise IndexError


def delete_employee_data(user_data):
    all_data = get_hr_data()
    user_id = user_data[0]
    user_data_index = get_user_index_by_id(all_data, user_id)
    del all_data[user_data_index]
    data_manager.write_table_to_file(DATAFILE, all_data)
    

def sort_date(asc = True):
    all_data = get_hr_data()
    sorted(all_data, key=help_split_date)
    earliest = all_data[0][1]
    latest = all_data[-1][1]
    print(earliest)
    print(latest)
    return (earliest, latest)

#for sort function
def help_split_date(data: str):
    splitup = data[2].split("-")
    return splitup[2],splitup[1], splitup[0]

def get_names_of_oldest_and_youngest():
    all_data = data_manager.read_table_from_file(DATAFILE)
    birthdays = []
    names = []
    for employee in all_data:
        birthdays.append(employee[2])
        names.append(employee[1])
    
    birthdays_sorted = sorted(birthdays[:])
    youngest = birthdays_sorted[-1]
    oldest = birthdays_sorted[0]
    oldest_name = []
    youngest_name = []
    youngest_name.append(names[birthdays.index(youngest)])
    oldest_name.append(names[birthdays.index(oldest)])
    
    name_tuple = ("".join(oldest_name), "".join(youngest_name))
    return name_tuple
        
def average_age_calculator(todays_date):
    all_data = data_manager.read_table_from_file(DATAFILE)
    birthdays = []
    for employee in all_data:
        birthdays.append(employee[2])
    birth_year = []
    birth_month = []
    birth_day = []
    for birthday in birthdays:
        splittet_birthdays = birthday.split("-")
        birth_year.append(int(splittet_birthdays[0]))
        birth_month.append(int(splittet_birthdays[1]))
        birth_day.append(int(splittet_birthdays[2]))

    average_year = round(sum(birth_year) / len(birth_year))
    average_month = round(sum(birth_month) / len(birth_month))
    average_day = round(sum(birth_day) / len(birth_day))

    if average_day < 10:
        average_day = "0" + str(average_day)
    if average_month < 10:
        average_month = "0" + str(average_month)
    
    average_year_int, average_month_int, average_day_int = int(average_year), int(average_month), int(average_day)
    todays_year, todays_month, todays_day = int(todays_date.split("-")[0]), int(todays_date.split("-")[1]), int(todays_date.split("-")[2])
    average_age = average_calculator(average_year_int, average_month_int, average_day_int, todays_year, todays_month, todays_day)
    return "The average age of our employees is:", average_age


def average_calculator(average_year_int, average_month_int, average_day_int, todays_year, todays_month, todays_day):
    year_age = todays_year - average_year_int 
    if todays_month < average_month_int or (average_month_int == todays_month and average_day_int > todays_day):
        year_age -= 1
    return year_age


def get_next_birthdays(date):
    all_data = data_manager.read_table_from_file(DATAFILE)
    birthdays = []
    names = []
    for employee in all_data:
        birthdays.append(employee[2])
        names.append(employee[1])

    next_birthday = []
    date_month, date_day = int(date.split("-")[1]), int(date.split("-")[2])

    for birthday in birthdays:
        splittet_birthdays = birthday.split("-")
        birth_month = int(splittet_birthdays[1])
        birth_day = int(splittet_birthdays[2])
        if (birth_month == date_month and birth_day - date_day >= 0 and birth_day - date_day <= 14) or (date_month + 1 == birth_month and (31 + birth_day) - date_day <= 14):
            next_birthday.append(names[birthdays.index(birthday)])
    if next_birthday == []:
        return "It's nobodies birthday within 2 weeks."
    else:
        return "It's the birthday of", "".join(next_birthday), "soon!"
    

def check_for_clearance(clearance):
    clearances = []
    all_data = data_manager.read_table_from_file(DATAFILE)
    for employee in all_data:
        clearances.append(employee[-1])
    all_clearances_needed = clearances.count(clearance)
    good_string = f"There are {all_clearances_needed} employees with the requested clearance level: {clearance}."
    if all_clearances_needed == 1:
        good_string = f"There is {all_clearances_needed} employee with the requested clearance level: {clearance}."
    elif all_clearances_needed == 0:
        good_string = f"There is no employee with the requested clearance level: {clearance}."
  
    return good_string

def show_department_employees():
    departments = []
    department_dictionary = {}
    all_data = data_manager.read_table_from_file(DATAFILE)
    for employee in all_data: 
        departments.append(employee[3])
    for department in departments:
        department_dictionary[department] = departments.count(department)
    return department_dictionary

# d = ['09-2012', '04-2007', '11-2012', '05-2013', '12-2006', '05-2006', '08-2007']
# >>> def sorting(L):
# ...     splitup = L.split('-')
# ...     return splitup[1], splitup[0]
# ... 
# >>> sorted(d, key=sorting) 
