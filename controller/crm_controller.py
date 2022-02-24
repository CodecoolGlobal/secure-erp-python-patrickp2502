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
    view.print_error_message("Not implemented yet.")


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


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
               "List customers",
               "Add new customer",
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
