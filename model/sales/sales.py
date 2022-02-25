""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

# Date in form: ISO 8601

def get_user_data():
    # all_data  = 
    # return
    all_data = data_manager.read_table_from_file(DATAFILE)
    # all_data = data_manager.read_table_from_file(DATAFILE)
    return all_data, HEADERS

def save_data(customer_id, product, price, date):
    all_data = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id()
    data_to_save = [id, customer_id, product, price, date]
    all_data.append(data_to_save)
    data_manager.write_table_to_file(DATAFILE, all_data)

def update_data(selling_id, customer_id, product, price, date):
    all_data = data_manager.read_table_from_file(DATAFILE)
    for purchase in all_data:
        if selling_id == purchase[0]:
            data_to_update_with = [selling_id, customer_id, product, price, date]
            all_data[all_data.index(purchase)] = data_to_update_with
            break
    data_manager.write_table_to_file(DATAFILE, all_data)

def delete_data(selling_id):
    all_data = data_manager.read_table_from_file(DATAFILE)
    for purchase in all_data:
        if selling_id == purchase[0]:
            del all_data[all_data.index(purchase)]
    data_manager.write_table_to_file(DATAFILE, all_data)


def get_biggest_revenue():
    all_data = data_manager.read_table_from_file(DATAFILE)
    prices = []
    for purchase in all_data:
        prices.append(purchase[3])
    
    max_float = max(float(number[3]) for number in all_data)
    for purchase in all_data:
        if purchase[3] == str(max_float):
            print(purchase)

def get_max_revenue_of_all_sales_with_one_product():
    all_data = data_manager.read_table_from_file(DATAFILE)
    products = []
    prices = []
    for purchase in all_data:
        products.append(purchase[2])
    for purchase in all_data:
        prices.append(purchase[3])
    added_items = []
    for product in products:
        added_items.append(str(products.count(product)) + product)
    prices_added = []
    productuess = set()
    # for product in products:
    #     productuess.add(product)
    for product in added_items:
        prices_added.append([int(product[0]) * float(prices[products.index(product[1:])]), product[1:]])
    check_set = set()
    for lst in prices_added:
        for item in lst:
            if isinstance(item, float):
                check_set.add(item)
    biggest_number = max(check_set)
    for lst in prices_added:
        if biggest_number in lst:
            return lst

def check_in_timespan(time_span_beginn, time_span_end):
    all_data = data_manager.read_table_from_file(DATAFILE)
    dates = [] 
    for transaction in all_data:
        dates.append(transaction[4])
    dates.append(time_span_beginn)
    dates.append(time_span_end)
    sorted_dates = sorted(dates)
    start = sorted_dates.index(time_span_beginn) + 1
    end = sorted_dates.index(time_span_end)
    print(f"THE AMOUNT OF TRANSACTIONS BETWEEN THE {time_span_beginn} AND THE {time_span_end}, WERE: {end - start}")


def check_in_timespan_sum_of_transactions(start, end):
    all_data = data_manager.read_table_from_file(DATAFILE)
    dates = [] 
    revenue = []
    for transaction in all_data:
        dates.append(transaction[4])
        revenue.append(transaction[3])

    cache_dates = dates[:]
    relevant_revenues = []
    dates.append(start)
    dates.append(end)
    sorted_dates = sorted(dates)
    start_date = sorted_dates.index(start) + 1
    end_date = sorted_dates.index(end)
    relevant_dates =  sorted_dates[start_date:end_date]
    for date in relevant_dates:
        relevant_revenues.append(revenue[cache_dates.index(date)])
    sum_relevant_revenues = []
    for number in relevant_revenues:
        sum_relevant_revenues.append(float(number))
    end_sum = sum(sum_relevant_revenues)
    print(end_sum)




