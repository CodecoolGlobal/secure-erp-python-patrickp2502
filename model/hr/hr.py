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
    data_list = []
    all_data = data_manager.read_table_from_file(DATAFILE)
    data_list.append(HEADERS)
    data_list.append(all_data)
    return data_list


def add_data(name: string, birth_date: string, department: string, clearance_level: int):
    all_data = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id()
    clearance_level_string = str(clearance_level)
    data_to_save = [id, name, birth_date, department, clearance_level_string]
    all_data.append(data_to_save)
    print(all_data )
    data_manager.write_table_to_file(DATAFILE, all_data)


def get_user_data(user_id):
    data_list = get_hr_data()
    user_index = get_user_index_by_id(data_list, user_id)
    user_data = data_list[user_index]
    return user_data


def get_user_index_by_id(data, user_id):
    for index in range(len(data)):
        if data[index][0] == user_id:
            return index 
    else:
        raise IndexError


def update_data():
    pass

def delete_data():
    pass