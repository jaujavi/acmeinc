import csv

def get_product_price(product_id, file_products):
    try:
        #print('\tSearching for product',product_id,'in file',file_products)

        with open(file_products, 'r') as file:
            file_csv = csv.DictReader(file) #default delimiter is ","

            for product in file_csv:

                #print('\tIs the product',product_id,'same as',product["id"],'??')
                if product_id == str(product["id"]):

                    #print('\tPRICE FOUND! Product:',str(product["id"]),'Price:',product["cost"])
                    return float(product["cost"])
                #else:
                    #print('\tPRICE NOT FOUND! Product:',product["id"])

    except IOError:
        print('ERROR: File', file_products,'not found.')


def order_prices(file_name, file_products):
    try:
        with open(file_name, 'r') as file:
            file_csv = csv.DictReader(file) #default delimiter is ","

            for order in file_csv:
                print('products ->',order["products"])
                #print('products ->',order["products"].split())

                total_order_price = 0
                products = order["products"].split()

                for product_id in products:
                    product_price = get_product_price(product_id, file_products)
                    print("\tproduct:", product_id,'\tprice:',product_price)
                    #total_order_price += get_product_price(product, file_products)
                    total_order_price += product_price
                print('order id -> ',order["id"],'\n\ttotal_order_price ->', total_order_price)

    except IOError:
        print('ERROR: File', file_name,'not found.')


def main():

    file_customers = "customers.csv"
    file_products = "products.csv"
    file_orders = "orders.csv"

    #task1
    order_prices(file_orders, file_products)


if __name__ == "__main__":
    main()
