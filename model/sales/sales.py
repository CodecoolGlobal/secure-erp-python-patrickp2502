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
    float_before_the_dot = [one.split(".")[0] for one in prices]
    whole_number_of_dots = [float(one) for one in float_before_the_dot]
    print(whole_number_of_dots)
    real_biggest = max(whole_number_of_dots)
    print(real_biggest)
    biggest = max(prices)
    print(prices)
    print(biggest)
    for purchase in all_data:
        if purchase[3] == real_biggest:
            print(purchase)


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
    print("The sum of all pricess of transactions in this timespan are:", end_sum)