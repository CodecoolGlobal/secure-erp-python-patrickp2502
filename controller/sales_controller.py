from model.sales import sales
from view import terminal as view

def add_transaction():
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
    sales.save_data(customer_id, product, price, date)


def list_transactions():
    view.print_table(sales.get_user_data(),sales.HEADERS)
    # view.print_error_message("Not implemented yet.")


def update_transaction():
    while True:
        selling_id = input("Which purchase yould you like to change?")
        break_out_of_for_loop = False
        for purchase in sales.get_user_data():
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
    sales.update_data(selling_id, customer_id, product, price, date)


def delete_transaction():
    selling_id = view.get_input("Which purchase do you want to delete?")
    found = False
    for purchase in sales.get_user_data():
        if selling_id == purchase[0]:
            sales.delete_data(selling_id)
            print("deleting successful")
            found = True
    if not found:
        print("No such id found.")
            


def get_biggest_revenue_transaction():
    view.print_table([sales.get_biggest_revenue()], sales.HEADERS)
    


def get_biggest_revenue_product():
    item_pricesAdded = sales.get_max_revenue_of_all_sales_with_one_product()
    label = item_pricesAdded[0]
    result = item_pricesAdded[1]
    view.print_general_results(result, label)


def count_transactions_between():
    start = input("Enter Start date (YYYY-MM-DD):")
    end = input("Enter End date (YYYY-MM-DD):")
    sales.check_in_timespan(start, end)


def sum_transactions_between():
    start = input("Enter Start date (YYYY-MM-DD):")
    end = input("Enter End date (YYYY-MM-DD):")
    sales.check_in_timespan_sum_of_transactions(start, end)


def run_operation(option):
    if option == 1:
        add_transaction()
    elif option == 2:
        list_transactions()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "Add new transaction",
               "List transactions",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
