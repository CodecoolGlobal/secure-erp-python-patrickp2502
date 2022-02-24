""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

import logging
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
    print(all_data )
    data_manager.write_table_to_file(DATAFILE, all_data)


def get_user_data(user_id):
    data_list = get_hr_data()
    logging.debug(f"data list in model {data_list}")
    logging.debug(f"user_id in model = {user_id}")
    user_index = get_user_index_by_id(data_list, user_id)
    user_data = data_list[user_index]
    logging.debug(f"user_data = {user_data}")
    return user_data



def update_data(updated_user_data):
    user_id = updated_user_data[0]
    all_data = get_hr_data()
    user_data_index = get_user_index_by_id(all_data, user_id)
    all_data[user_data_index] = updated_user_data
    data_manager.write_table_to_file(DATAFILE, all_data)
    

def get_user_index_by_id(data, user_id):
    for index in range(len(data)):
        logging.debug(data)
        logging.debug(user_id)
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





d = ['09-2012', '04-2007', '11-2012', '05-2013', '12-2006', '05-2006', '08-2007']
# >>> def sorting(L):
# ...     splitup = L.split('-')
# ...     return splitup[1], splitup[0]
# ... 
# >>> sorted(d, key=sorting) 
