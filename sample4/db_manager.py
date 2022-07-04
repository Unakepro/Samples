import sqlite3
import os


class MyDatabaseManager:

    def __init__(self, data_name):
        self._data_name = data_name

    def __enter__(self):
        self.conn = sqlite3.connect(f"{os.getcwd()}/{self._data_name}")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise exc_type


database_manager = MyDatabaseManager("product.db")


class DbCommands:

    @staticmethod
    def get_category():
        with database_manager as conn:
            cursor = conn.cursor()
            res = cursor.execute("SELECT category FROM categories")
            my_list = []

            for category in res.fetchall():
                my_list.append(category[0])
            return my_list

    @staticmethod
    def get_product():
        with database_manager as conn:
            cursor = conn.cursor()
            res = cursor.execute("SELECT name FROM products")

            my_list = []
            for product in res.fetchall():
                my_list.append(product[0])

            return my_list

    @staticmethod
    def get_product_info():
        with database_manager as conn:
            cursor = conn.cursor()

            part1 = "SELECT category, name, location, price, quantity FROM products"
            part2 = "INNER JOIN categories ON products.owner_id = categories.Id"

            res = cursor.execute(f"{part1} {part2}")
            res = res.fetchall()

            return res

    @staticmethod
    def send_new_category(category):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO 'categories'('category') VALUES (?)", [category])
            conn.commit()
            return "Successful"

    @staticmethod
    def send_new_item(name, location, price, quantity, owner_id):
        with database_manager as conn:
            cursor = conn.cursor()
            id = cursor.execute(f"SELECT Id FROM categories WHERE category = '{owner_id}'")
            owner = id.fetchall()[0][0]
            cursor.execute(f"INSERT INTO 'products'('name','location','price','quantity','owner_id') VALUES (?,?,?,?,?)"
                           , [name, location, price, quantity, owner])
            conn.commit()
            return "Successful"

