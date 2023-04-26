from flask import request, jsonify

# Exemplo dicionário de produtos cadastrados
products = {
    1: {
        "id": 1,
        "name": "Lapiseira Pentel Técnica Vermelha",
        "description": "Lapiseira para desenho técnico com grafite de 0.3mm",
        "brand": "Pentel",
        "price": 18.99
    },
    2: {
        "id": 2,
        "name": "Post It 3M",
        "description": "Post It 3M Pink",
        "brand": "3M",
        "price": 9.99
    },
    3: {
        "id": 3,
        "name": "Patinho de borracha",
        "description": "Patinho de borracha amarelo",
        "brand": "Suzano",
        "price": 5.99
    }
}

#create id
def create_id():
    id = max(products.keys()) + 1
    return id

# Return product
def return_product(id:int):
    if id in products.keys():
        return jsonify(products[id])
    else:
        return jsonify({"error": "Product not found"}), 404

# Return products
def return_products():
    return jsonify(products)

#create product
def create_product(id=None):
    if request.method == "POST":
        if id is None:
            id = create_id()
            while id in products:
                id = create_id()
            product = {
                'id': id,
                'name': request.json["name"],
                'description': request.json["description"],
                'brand': request.json["brand"],
                'price': request.json["price"]
            }
            products[id] = product
            return jsonify(products)        
    elif request.method == "PUT":
        id = request.json["id"]
        if id in products:
            product = products[id]
            product['name'] = request.json["name"]
            product['description'] = request.json["description"]
            product['brand'] = request.json["brand"]
            product['price'] = request.json["price"]
            return jsonify(product), 200
        else:
            return jsonify({"error": "Product not found"}), 404

# Delete product
def delete_product(id:int):
    del products[id]
    return {}