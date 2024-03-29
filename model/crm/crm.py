""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def get_user_data():
    # all_data  = 
    # return
    all_data = data_manager.read_table_from_file(DATAFILE)
    return all_data, HEADERS

def save_data(name, email, subscribed):
    all_data = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id()
    data_to_save = [id, name, email, subscribed]
    all_data.append(data_to_save)
    data_manager.write_table_to_file(DATAFILE, all_data)

def update_data(id, name, email, subscribed):
    all_data = data_manager.read_table_from_file(DATAFILE)
    for customer in all_data:
        if id == customer[0]:
            data_to_update_with = [id, name, email, subscribed]
            all_data[all_data.index(customer)] = data_to_update_with
            break
    data_manager.write_table_to_file(DATAFILE, all_data)

def delete_data(id):
    all_data = data_manager.read_table_from_file(DATAFILE)
    for customer in all_data:
        if id == customer[0]:
            del all_data[all_data.index(customer)]
    data_manager.write_table_to_file(DATAFILE, all_data)

def pull_subscribed_email_adresses():
    mail_adresses_subscribed = []
    all_data = data_manager.read_table_from_file(DATAFILE)
    for customer in all_data:
        if customer[-1] == "1":
            mail_adresses_subscribed.append(customer[2])
    print("THE MAIL ADRESSES OF SUBSCRIBED CUSTOMERS ARE:", " ".join(mail_adresses_subscribed))