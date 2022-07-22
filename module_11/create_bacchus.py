from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter user name: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "DROP DATABASE IF EXISTS bacchus"
        create_db_query_1 = "CREATE DATABASE bacchus"
        create_db_query_2 = "USE bacchus"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            cursor.execute(create_db_query_1)
            cursor.execute(create_db_query_2)

            create_vendor_table_query = """
            CREATE TABLE vendor (
            vendor_id  INT  PRIMARY KEY,
            vendor_name  VARCHAR(75)  NOT NULL
            )
            """
            create_employee_table_query = """
            CREATE TABLE employee (
                employee_id  INT  PRIMARY KEY, 
                employee_first_name  VARCHAR(75)  NOT NULL, 
                employee_last_name  VARCHAR(75)  NOT NULL, 
                employee_role  VARCHAR(75)  NOT NULL, 
                q1_hours  INT  NOT NULL, 
                q2_hours  INT  NOT NULL, 
                q3_hours  INT  NOT NULL, 
                q4_hours  INT  NOT NULL
            )
            """
            create_distributor_table_query = """
            CREATE TABLE distributor (
                distributor_id  INT  PRIMARY KEY,
                distributor_name  VARCHAR(75)  NOT NULL
            )
            """
            create_sales_table_query = """
            CREATE TABLE sales (
                distributor_id  INT  NOT NULL, 
                merlot  INT  NOT NULL, 
                cabernet  INT  NOT NULL, 
                chablis  INT  NOT NULL, 
                chardonnay  INT  NOT NULL,
                CONSTRAINT fk_distributor_id 
                FOREIGN KEY(distributor_id) 
                REFERENCES distributor(distributor_id)
            )
            """
            create_supply_table_query = """
            CREATE TABLE supply (
                supply_id  INT  PRIMARY KEY, 
                supply_name  VARCHAR(75)  NOT NULL, 
                supply_price  DOUBLE, 
                vendor_id  INT  NOT NULL,  
                CONSTRAINT fk_supply_vendor_id 
                FOREIGN KEY(vendor_id) 
                REFERENCES vendor(vendor_id)
            )
            """
            create_supply_order_table_query = """
            CREATE TABLE supply_order(
                order_date  DATE  PRIMARY KEY, 
                promised_delivery_date  DATE  NOT NULL, 
                actual_delivery_date  DATE, 
                order_price  DOUBLE  NOT NULL, 
                vendor_id  INT  NOT NULL,  
                CONSTRAINT fk_order_vendor_id 
                FOREIGN KEY(vendor_id) 
                REFERENCES vendor(vendor_id)
            )
            """
            with connection.cursor() as cursor:
                cursor.execute(create_vendor_table_query)
                cursor.execute(create_employee_table_query)
                cursor.execute(create_distributor_table_query)
                cursor.execute(create_sales_table_query)
                cursor.execute(create_supply_table_query)
                cursor.execute(create_supply_order_table_query)
                connection.commit()
            
            insert_vendor_query = """
            INSERT INTO vendor (vendor_id, vendor_name)
            VALUES 
                (1, "Bobs Bottles and Bungs"),
                (2, "Seans Shipping Supplies"),
                (3, "Victors Vinting Vitals")
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_vendor_query)
                connection.commit()

            insert_employee_query = """
            INSERT INTO employee (employee_id, employee_first_name, employee_last_name, employee_role, q1_hours, q2_hours, q3_hours, q4_hours)
            VALUES 
                (1, "Janet", "Collins", "Finance/Payroll Manager", 456, 483, 459, 489),
                (2, "Roz", "Murphy", "Marketing Manager", 476, 483, 458, 461),
                (3, "Bob", "Ulrich", "Marketing Assistant", 456, 463, 448, 451),
                (4, "Henry", "Doyle", "Production Line Manager", 469, 478, 455, 463),
                (5, "Maria", "Costanza", "Distribution Manager", 467, 458, 470, 482),
                (6, "Jim", "Wino", "Production Line Employee", 453, 462, 471, 451)
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_employee_query)
                connection.commit()

            insert_distributor_query = """
            INSERT INTO distributor (distributor_id, distributor_name)
            VALUES 
                (1, "Wine Harder"),
                (2, "Wines-R-Us"),
                (3, "Winers Warehouse"),
                (4, "Langstons Liquors"),
                (5, "Booze Warehouse"),
                (6, "Liquor Lovers")
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_distributor_query)
                connection.commit()

            insert_sales_query = """
            INSERT INTO sales (distributor_id, merlot, cabernet, chablis, chardonnay)
            VALUES 
                (1, 208, 432, 110, 352), 
                (2, 196, 413, 105, 325),
                (3, 220, 458, 102, 330),
                (4, 235, 467, 99, 328),
                (5, 229, 470, 101, 317),
                (6, 237, 485, 104, 321)
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_sales_query)
                connection.commit()

            insert_supply_query = """
            INSERT INTO supply (supply_id, supply_name, supply_price, vendor_id)
            VALUES 
                (1, "750ml bottle", 2, 1),
                (2, "cork", 0.25, 1),
                (3, "label", 0.10, 2),
                (4, "box", 0.30, 2),
                (5, "vat", 100, 3),
                (6, "tubing", 5, 3)
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_supply_query)
                connection.commit()

            insert_supply_order_query = """
            INSERT INTO supply_order (order_date, promised_delivery_date, actual_delivery_date, order_price, vendor_id)
            VALUES 
                ("2021-08-05", "2021-08-14", "2021-08-15", 123.04, 1),
                ("2021-09-05", "2021-09-14", "2021-09-12", 110.93, 1),
                ("2021-08-04", "2021-08-11", "2021-08-09", 98.34, 2),
                ("2021-09-07", "2021-09-14", "2021-09-10", 101.68, 2),
                ("2021-08-14", "2021-08-21", "2021-09-21", 225, 3),
                ("2021-09-30", "2021-10-13", "2021-10-30", 115, 3)
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_supply_order_query)
                connection.commit()
            print("\nDatabase bacchus created successfully!")
except Error as e:
    print(e)