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
    while True:
        id = input("Which purchase yould you like to change?")
        break_out_of_for_loop = False
        for customer in crm.get_user_data()[0]:
            print(purchase)
            if selling_id == purchase[0]:
                break_out_of_for_loop = True
                break
        if break_out_of_for_loop:
            break
    while True:
        customer_id = view.get_input("Type in the ID of the customer who bought something.")
        if customer_id == "":
            print("Please enter a customers ID.")
        else:
            break
    while True:
        product = view.get_input("What was bought?")
        if product.isalnum():
            break
        else:
            print("Please enter the Product name.(letters and numbers possible)")
    while True:
        price = view.get_input("What was the selling price?")
        try:
            float(price)
            break
        except:
            print("Please enter a float type.")
    while True:
        day = view.get_input("What was the selling day?")
        if len(day) == 2:
            if day.isnumeric():
                if int(day) >= 1 and int(day) <= 31:
                    break
                else:
                    print("Input has to be a valid date.")
            else:
                print("Input has to be numbers.")
        else:
            print("2 numbers input only.")
    while True:
        month = view.get_input("What was the selling month?")
        if len(month) == 2:
            if month.isnumeric():
                if int(month) >= 1 and int(month) <= 12:
                    break
                else:
                    print("Input has to be a valid month between 1 and 12.")
            else:
                print("Input has to be numbers.")
        else:
            print("2 numbers input only.")
    while True:
        year = view.get_input("What was the selling year?")
        if len(year) == 4:
            if year.isnumeric():
                if int(year) >= 1800 and int(year) <= 3000:
                    break
                else:
                    print("Input has to be a valid year between 1800 and 3000.")
            else:
                print("Input has to be numbers.")
        else:
            print("4 numbers input only.")
    date = year + "-" + month + "-" + day
    crm.update_data(id, customer_id, product, price, date)
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
