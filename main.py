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
    product = [product for product in sonuc['products'] if product[0]['kullanici_id']==product_id]

    for i in range(len(product)):
        print("product id :",product[i]['id'])
        print("product model_id :", product[i]['model_id'])
        print("product model_adi :", product[i]['model_adi'])
        print("product longitude :", product[i]['longitude'])
        print("product latitude :", product[i]['latitude'])
        print("product toplam_adim :", product[i]['toplam_adim'])
        print("product kalori :", product[i]['kalori'])
        print("product oksijen :", product[i]['oksijen'])
        print("product nabiz :", product[i]['nabiz'])
        print("product kullanici_id :", product[i]['kullanici_id'])
        print("product seri_no :", product[i]['seri_no'])
        print("product yazilim_versiyon :", product[i]['yazilim_versiyon'])
        print("product tarih :", product[i]['tarih'])

    if len(product) == 0:
        return jsonify({'product': 'Not found'}), 404
    return jsonify({'product': product})

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