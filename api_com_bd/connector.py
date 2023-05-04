import sqlite3, os

class Connector:

    #way = os.path.dirname(os.path.realpath(__file__))
    #db_path_way = os.path.join(way, 'products.db')

    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        return conn