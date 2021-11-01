from flask import Flask, jsonify
from flask import request

import postgreSQL

products = []

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'products': products})


@app.route('/azon/api/products', methods=['GET'])
def get_products():
    sonuc = postgreSQL.list_database()
    return sonuc


@app.route('/azon/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    #aktif değil
    sonuc = postgreSQL.list_database()
    print("sonuc['products'] :",sonuc['products'])
    print("sonuc['products'][0] :",sonuc['products'][0])
    print("sonuc['products'][0]['kullanici_id'] :",sonuc['products'][0]['kullanici_id'])
    productss = [productss for productss in sonuc['products'] if int(productss['kullanici_id'])==int(product_id)]
    # print("productss :",productss)
    # print("type(productss) :",type(productss))
    # print("productss['kullanici_id'] :",productss['kullanici_id'])
    # print("int(product_id) :",int(product_id))
    if len(productss) == 0:
        return jsonify({'product': 'Not found'}), 404
    else:
        print("product model_id :", productss['model_id'])
        print("product model_adi :", productss['model_adi'])
        print("product longitude :", productss['longitude'])
        print("product latitude :", productss['latitude'])
        print("product toplam_adim :", productss['toplam_adim'])
        print("product kalori :", productss['kalori'])
        print("product oksijen :", productss['oksijen'])
        print("product nabiz :", productss['nabiz'])
        print("product kullanici_id :", productss['kullanici_id'])
        print("product seri_no :", productss['seri_no'])
        print("product yazilim_versiyon :", productss['yazilim_versiyon'])
        print("product tarih :", productss['tarih'])
        return jsonify({'product': productss})

    # print("product id :",productss['id'])




@app.route('/azon/api/products/', methods=['POST'])
def create_product():
    newProduct = {
        'id': request.json['id'],
        'model_id': request.json['model_id'],
        'model_adi': request.json['model_adi'],
        'longitude': request.json['longitude'],
        'latitude': request.json['latitude'],
        'kullanici_id': request.json.get('kullanici_id'),
        'kalori': request.json['kalori'],
        'oksijen': request.json['oksijen'],
        'nabiz': request.json['nabiz'],
        'seri_no': request.json['seri_no'],
        'yazilim_versiyon': request.json['yazilim_versiyon'],
        'toplam_adim': request.json['toplam_adim'],
        'tarih': request.json['tarih'],

    }
    products.append(newProduct)
    return jsonify({'product': newProduct}), 201


@app.route('/azon/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'product': 'Not found'}), 404
    products.remove(product[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)  # !flask/bin/python