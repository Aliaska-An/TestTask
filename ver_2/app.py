from flask import Flask, request, json, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/shop'
mongo = PyMongo(app)

# Добавление в коллекцию элемента
@app.route('/products/addProduct', methods=['POST'])
def addProduct():
    name = request.json['name']
    description = request.json['description']
    parameters = request.json['parameters']

    if name and description and parameters:
        id = mongo.db.products.insert(
            {'name': name, 'description': description,
             'parameters': parameters })
        response = {
            'id': str(id),
            'name': name,
            'description': description,
            'parameters': parameters
        }
        return response
    else:
        {'message': 'received'}
    return {'message': 'received'}


# Получить все товары
@app.route('/products/getAllProducts', methods=['GET'])
def getAllProducts():
    products = mongo.db.products.find()
    response = json_util.dumps(products)

    return Response(response, mimetype='application/json')


# Получить товар по ID
@app.route('/products/getProductID/<id>', methods=['GET'])
def getProduct_ID(id):
    product = mongo.db.products.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(product)
    return Response(response, mimetype='application/json')


# Получить список названий товаров
@app.route('/products/getAllProductsNames', methods=['GET'])
def getAllProductsNames():
    docs_list = list(mongo.db.products.find({}, {"name": 1, "_id": 0}))
    return {"products": json.loads(json.dumps(docs_list, default=json_util.default))}


# Получить товар по NAME
@app.route('/products/getProductsName/<name>', methods=['GET'])
def getProducts_NAME(name):
    docs_list = list(mongo.db.products.find({}, {"_id": 0, "name": name}))
    return {"products": json.loads(json.dumps(docs_list, default=json_util.default))}


# Получить товар по YEAR
@app.route('/products/getProductsYear/<year>', methods=['GET'])
def getProducts_YEAR(year):
    docs_list = list(mongo.db.products.find({"parameters.year": int(year)}, {"_id": 0, "parameters.year": 1, "name": 1}))
    return {"products": json.loads(json.dumps(docs_list, default=json_util.default))}


# Получить товар по COUNTRY
@app.route('/products/getProductsCountry/<country>', methods=['GET'])
def getProducts_COUNTRY(country):
    docs_list = list(mongo.db.products.find({"parameters.country": country}, {"_id": 0, "name": 1}))
    return {"products": json.loads(json.dumps(docs_list, default=json_util.default))}


# Получить товар по COUNTRY
@app.route('/products/getProductsColor/<color>', methods=['GET'])
def getProducts_COLOR(color):
    docs_list = list(mongo.db.products.find({"parameters.color": color}, {"_id": 0, "name": 1}))
    return {"products": json.loads(json.dumps(docs_list, default=json_util.default))}

if __name__ == "__main__":
    app.run(debug=True)