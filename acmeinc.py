import csv

def print_products (file_name):
    try:
        with open(file_name, 'r') as file:

            file_csv = csv.DictReader(file) #default delimiter is ","
            lines = 0

            for line in file_csv:
                print('products ->',line["products"])
                lines += 1

                products = line["products"].split()
                for product in products:
                    print("\tproduct -> ", product)
    except IOError:
        print('ERROR: File', file_name,'not found.')

def main():

    file_customers = "customers.csv"
    file_products = "products.csv"
    file_orders = "orders.csv"

    print_products(file_orders)


if __name__ == "__main__":
    main()
