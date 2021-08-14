import csv
import pandas


def print_csv_header(file_name,header):
    try:
        with open(file_name, 'w', newline='') as file_w:
            file_csv_w = csv.DictWriter(file_w, fieldnames=header)
            file_csv_w.writeheader()
    except Exception as e:
        print('ERROR:',e)


def print_csv_row(file_name,row):
    try:
        with open(file_name, 'a+', newline='') as file_a:
            file_csv_a = csv.writer(file_a) #default delimiter is ","
            file_csv_a.writerow(row)
    except Exception as e:
        print('ERROR:',e)


def get_product_price(product_id, file_products):
    try:
        with open(file_products, 'r') as file:
            file_products_csv = csv.DictReader(file) #default delimiter is ","
            for product in file_products_csv:
                if product_id == str(product['id']):
                    return float(product['cost'])
    except Exception as e:
        print('ERROR:',e)


def get_order_price(order, file_products):
    total = 0
    products = order['products'].split()
    for product_id in products:
        total += get_product_price(product_id, file_products)
    return float(total)


def create_order_prices(file_orders, file_products, file_order_prices, file_order_prices_header):
    try:
        print_csv_header(file_order_prices, file_order_prices_header)
        with open(file_orders, 'r') as file_r:
            file_orders_csv = csv.DictReader(file_r) #default delimiter is ","
            for order in file_orders_csv:
                order_price_row = (order['id'], get_order_price(order, file_products))
                print_csv_row(file_order_prices, order_price_row)
    except IOError:
        print('ERROR: File not found.')


def get_product_customers(product_id, file_orders):
    try:
        order_id_list = []
        with open(file_orders, 'r') as file_r:
            file_orders_csv = csv.DictReader(file_r) #default delimiter is ","
            for order in file_orders_csv:
                if product_id in order['products']:
                    order_id_list.append(order['id'])
        return order_id_list
    except Exception as e:
        print('ERROR:',e)


def create_products_customers(file_orders, file_products, file_products_customers, file_products_customers_header):
    try:
        print_csv_header(file_products_customers, file_products_customers_header)
        with open(file_products, 'r') as file_r:
            file_products_csv = csv.DictReader(file_r) #default delimiter is ","
            for product in file_products_csv:
                customers_ids = get_product_customers(product['id'], file_orders)
                customers_ids_spaced = ' '.join(customers_ids)
                product_customers_row = (product['id'], customers_ids_spaced)
                print_csv_row(file_products_customers, product_customers_row)
    except IOError:
        print('ERROR: File not found.')


def get_customer_total_euros(customer_id, file_orders, file_products):
    try:
        total = 0
        with open(file_orders, 'r') as file_r:
            file_orders_csv = csv.DictReader(file_r) #default delimiter is ","
            for order in file_orders_csv:
                if customer_id in order['customer']:
                    total += get_order_price(order, file_products)
        return float(total)
    except Exception as e:
        print('ERROR:',e)


def order_file_desc(file_name, value):
    df = pandas.read_csv(file_name)
    sorted_df = df.sort_values(by=[value], ascending=False)
    sorted_df.to_csv(file_name, index=False)


def create_customer_ranking(file_orders, file_products, file_customers, file_customer_ranking, file_customer_ranking_header):
    try:
        print_csv_header(file_customer_ranking, file_customer_ranking_header)
        with open(file_customers, 'r') as file_r:
            file_customers_csv = csv.DictReader(file_r) #default delimiter is ","
            for customer in file_customers_csv:
                total_euros = get_customer_total_euros(customer['id'],file_orders, file_products)
                customer_ranking_row = (customer['id'], customer['firstname'], customer['lastname'], total_euros)
                print_csv_row(file_customer_ranking, customer_ranking_row)
                order_file_desc(file_customer_ranking, file_customer_ranking_header[3])
    except IOError:
        print('ERROR: File not found.')


def main():

    #source files
    file_customers = "customers.csv"
    file_products = "products.csv"
    file_orders = "orders.csv"

    #task1
    file_order_prices = "order_prices.csv"
    file_order_prices_header = ['id', 'euros']
    create_order_prices(file_orders, file_products, file_order_prices, file_order_prices_header)

    #task2
    file_products_customers = "product_customers.csv"
    file_products_customers_header = ['id', 'customer_ids']
    create_products_customers(file_orders, file_products, file_products_customers, file_products_customers_header)

    #task3
    file_customer_ranking = "customer_ranking.csv"
    file_customer_ranking_header = ['id', 'firstname', 'lastname', 'total_euros']
    create_customer_ranking(file_orders, file_products, file_customers, file_customer_ranking, file_customer_ranking_header)

if __name__ == "__main__":
    main()
