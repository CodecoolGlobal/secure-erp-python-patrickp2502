from model.crm import crm
from view import terminal as view

def add_customer():
    while True:
        name = view.get_input("Type in your Name")
        if name == "":
            print("Please enter your Name.")
        else:
            break
    while True:
        email = view.get_input("Type in your Email")
        if "@" in email and "." in email:
            break
        else:
            print("Enter a valid email please(exampleMail@something.domain)")
    while True:
        subscribed = view.get_input("Do you want a subscription? type in 0 for no and 1 for yes")
        if subscribed in ["0", "1"]:
            break
        else:
            print("0 or 1 please.")
    crm.save_data(name, email, subscribed)

    # model.crm.saveData([name, email, subscribed])

def list_customers():
    all_customer_data, customer_data_header = crm.get_user_data()
    view.print_table(all_customer_data, customer_data_header)


def update_customer():
    while True:
        id = input("What is the customers id?")
        break_out_of_for_loop = False
        for customer in crm.get_user_data()[0]:
            if id == customer[0]:
                break_out_of_for_loop = True
                print(f"This is going to be the customer to be updated:\n",view.print_table([customer], crm.HEADERS))
                break
        if break_out_of_for_loop:
            break
    while True:
        name = view.get_input("Type in your Name")
        if name == "":
            print("Please enter your Name.")
        else:
            break
    while True:
        email = view.get_input("Type in your Email")
        if "@" in email and "." in email:
            break
        else:
            print("Enter a valid email please(exampleMail@something.domain)")
    while True:
        subscribed = view.get_input("Do you want a subscription? type in 0 for no and 1 for yes")
        if subscribed in ["0", "1"]:
            break
        else:
            print("0 or 1 please.")
    crm.update_data(id, name, email, subscribed)


def delete_customer():
    id = view.get_input("Which customer do you want to delete?")
    for customer in crm.get_user_data()[0]:
        print(customer)
        if id == customer[0]:
            crm.delete_data(id)


def get_subscribed_emails():
    crm.pull_subscribed_email_adresses()


def run_operation(option):
    if option == 1:
        add_customer()

    elif option == 2:
        list_customers()

    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "Add new customer",
               "List customers",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
