import csv


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
            #file_csv_a = csv.DictWriter(file_a, fieldnames=header)
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
        #product_price = get_product_price(product_id, file_products)
        #print("\tproduct:", product_id,'\tprice:',product_price)
        total += get_product_price(product_id, file_products)
    print('Total_order_price ->', total,'\n')
    return float(total)


def create_order_prices(file_orders, file_products, file_order_prices, file_order_prices_header):
    try:
        with open(file_orders, 'r') as file_r:
            file_orders_csv = csv.DictReader(file_r) #default delimiter is ","
            print_csv_header(file_order_prices, file_order_prices_header)
            for order in file_orders_csv:
                print('Products for order:',order['id'],' ->',order['products'])
                #order_price = get_order_price(order, file_products)
                #order_price = {'id': order["id"], 'euros': total_order_price}
                order_price_row = (order['id'], get_order_price(order, file_products))
                print_csv_row(file_order_prices, order_price_row)
    except IOError:
        print('ERROR: File not found.')


def main():

    file_customers = "customers.csv"
    file_products = "products.csv"
    file_orders = "orders.csv"

    file_order_prices = "order_prices.csv"
    file_order_prices_header = ['id', 'euros']

    #task1
    create_order_prices(file_orders, file_products, file_order_prices, file_order_prices_header)


if __name__ == "__main__":
    main()
