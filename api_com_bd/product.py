import os, sqlite3

way = os.path.dirname(os.path.realpath(__file__))
db_path_way = os.path.join(way, 'products.db')

class Products:
    def __init__(self, name: str, description: str, weight: float , brand: str, supplier: str, price: float,  id = None):
        self.id = id
        self.name = name
        self.description = description
        self.weight = weight
        self.brand = brand
        self.supplier = supplier
        self.price = price

    def to_dictionary(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "weight": self.weight,
            "brand": self.brand,
            "supplier": self.supplier,
            "price": self.price
        }

    def get_products(conn: sqlite3.Connection):
        query = "SELECT * FROM products"
        cursor = conn.cursor()
        results = cursor.execute(query).fetchall()
        items = []
        for result in results:
            items.append(Products(id = result[0], name = result[1], description = result[2], weight = result[3], brand = result[4], supplier = result[5], price = result[6]).to_dictionary())
        conn.close()
        return items
    
    def get_product(id: int, conn: sqlite3.Connection):
        query = "SELECT * FROM products WHERE id_product = ?"
        cursor = conn.cursor()
        answer = cursor.execute(query, (id, )).fetchone()
        conn.close()
        if answer:
            return Products(id = answer[0], name = answer[1], description = answer[2], weight = answer[3], brand = answer[4], supplier = answer[5], price = answer[6])
        else: 
            return None

    def create_product(self, conn: sqlite3.Connection):
        if self.id is None:
            query = "INSERT INTO products (name_product, description_product, weight_product, brand_product, supplier_product, price_product) VALUES (?, ?, ?, ?, ?, ?)"
            cursor = conn.cursor();
            cursor.execute(query, (self.name, self.description, self.weight, self.brand, self.supplier, self.price))
            self.id = cursor.lastrowid
        else:
            query = "UPDATE products SET name_product = ?, description_product = ?, weight_product = ?, brand_product = ?, supplier_product = ?, price_product = ? WHERE id_product = ?"
            cursor = conn.cursor()
            cursor.execute(query, (self.name, self.description, self.weight, self.brand, self.supplier, self.price, self.id))
        conn.commit()
        conn.close()

    def delete_product(self, conn: sqlite3.Connection):
        query = "DELETE FROM products WHERE id_product = ?"
        cursor = conn.cursor()
        cursor.execute(query, (self.id, ))
        conn.commit()
        conn.close()
