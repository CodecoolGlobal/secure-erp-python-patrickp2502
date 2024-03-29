

def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    
    print(title)
    for list_option_index in range(1, len(list_options)):
        print(f"({list_option_index}) {list_options[list_option_index]}")
    print(f"({0}) {list_options[0]}")
    

def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if isinstance(result, float):
        value = round(result, 2)
        print(f"{label}: {value}")
    elif isinstance(result, list) or isinstance(result, tuple):
        value =  ";".join(result)
        print(f"{label}:\n {value}")
    elif isinstance(result, dict):
        value = []
        for key in result:
            value.append(f"{key}: {result[key]}")
        print(label, "; ".join(value))
    else:
        print(print(f"{label} \n{result}"))



# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, header):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
   
    #TODO ADD VISUALS! Add flex column width
    colum_length = max([len(data_cell) for row in table for data_cell in row]) + 4 
    upper_header = "/" + ("-" * colum_length) * len(header) + ("-" * (len(header) - 1)) + "\\"
    middle_header = "|" + ("-" * colum_length) * len(header) + ("-" * (len(header) - 1)) + "|"
    lower_string = "\\" + ("-" * colum_length) * len(header) + ("-" * (len(header) - 1)) + "/"
    header_string = "|" + "|".join(["".join(header_data).center(colum_length) for header_data in header]) + "|"
    print(upper_header + "\n" + header_string)
    for row in table:
        if row != "":
            row_string = "|" + "|".join(["".join(row_data).center(colum_length) for row_data in row]) + "|"
            print(middle_header + "\n" + row_string)
    print(lower_string)
    
    





    # header_row_string =  "|".join([str(column).center(10) for column in table[0]]) + "|"
    # print(header_row_string)
    
    # for row in table:
    #     row_string = "|" + 
    #     pass

    # print(f"id".center(8) + "|" + f"product".center(12) + "|" + f"type".center(10) + "|")
    # for row in table:
    #     print(f"{row[0]}".center(8) + "|" + f"{row[1]}".center(12) + "|" + f"{row[2]}".center(10) + "|")
        

    


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(label)
    return user_input

def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    user_inputs = []
    for label in labels:
        print(label)
        user_inputs.append(input("Enter here:"))
    return user_inputs
        


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)


if __name__ == "__main__":
    
    test_table = [["ASBDABSDB", "IDEED", "BLALALALALALAL", "noice"],
                    ["ASBDABSDB", "IDasdasdasdEED", "BLALALALALALALasdasdasdas", "noice"],
                    ["ASBDABSDB", "ID11111EED", "BLALALAL11111ALALAL", "nadsasdasdasoice"]]

    print_table(test_table)