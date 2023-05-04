from flask import Flask, jsonify, request
from connector import Connector
from product import Products
import os

way = os.path.dirname(os.path.realpath(__file__))
db_path_way = os.path.join(way, 'products.db')
conn = Connector(db_path_way)

app = Flask(__name__)

# Route to return a single product by id
@app.route("/products/<int:id_product>", methods = ['GET'])
def show_product(id_product):
    product = Products.get_product(id_product, conn.get_connection())
    if product:
        return jsonify(product.to_dictionary())
    else:
        return jsonify({"Error": "Product not found"}), 404

# Route to return all products
@app.route("/products", methods = ['GET'])
def show_all():
    products = Products.get_products(conn.get_connection())
    return jsonify(products)

# Route to register a new product
@app.route("/products", methods = ['POST'])
def new_product():
    data = request.get_json()
    product = Products(name = data["name"], description = data["description"], weight = data["weight"], brand = data["brand"], supplier = data["supplier"], price = data["price"])
    product.create_product(conn.get_connection())
    return product.to_dictionary()

# Route to update product
@app.route("/products/<int:id_product>", methods = ['PUT'])
def update_product(id_product):
    data = request.get_json()
    product = Products.get_product(id_product, conn.get_connection())
    if product:
        product.id = id_product
        product.name = data["name"] 
        product.description = data["description"] 
        product.weight = data["weight"] 
        product.brand = data["brand"] 
        product.supplier = data["supplier"] 
        product.price = data["price"]
        product.create_product(conn.get_connection())
        return jsonify(product.to_dictionary())
    else:
        return jsonify({"Error": "Product not found"}), 404

# Route to delete product
@app.route("/products/<int:id_product>", methods = ['DELETE'])
def remove_product(id_product):
    product = Products.get_product(id_product, conn.get_connection())
    if product:
        product.delete_product(conn.get_connection())
        return jsonify({"Message": "Product successfully deleted"}), 200
    else:
        return jsonify({"Error": "Product not found"}), 404

app.run(debug=True)