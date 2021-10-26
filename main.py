from flask import Flask, jsonify
from flask import request
products = [
    {
        'id': 1,
        'model_id': 1,
        'model_adi': '04.00.006',
        'longitude': 35421585,
        'latitude': 38543869,
        'toplam_adim':55,
        'kalori':19,
        'oksijen': 96,
        'nabiz': 98,
        'kullanici_id': 12312564,
        'yazilim_versiyon': 'v1',
        'seri_no': 12345678910,
        'tarih': '2021-10-18',
        # 'kontrol':'456654'
    },
    {
        'id': 2,
        'model_id': 1,
        'model_adi': '04.00.006',
        'longitude': 35429371,
        'latitude': 38543868,
        'toplam_adim':75,
        'kalori':20,
        'oksijen': 96,
        'nabiz': 95,
        'kullanici_id': 12312564,
        'yazilim_versiyon': 'v1',
        'seri_no': 12345678910,
        'tarih': '2021-10-18',
        'kontrol':'456654'
    },
    {
        'id': 3,
        'model_id': 2,
        'model_adi': '04.00.002',
        'longitude': 35421581,
        'latitude': 38548167,
        'toplam_adim':30,
        'kalori':10,
        'oksijen': '94',
        'nabiz': 97,
        'kullanici_id': 98745632,
        'yazilim_versiyon': 'v2',
        'seri_no': 10987654321,
        'tarih': '2021-10-18',
        'kontrol':'456654'
    }
]

app = Flask(__name__)


@app.route('/azon/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})


@app.route('/azon/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product['id']==product_id]

    for i in range(len(product)):
        print("product id :",product[i]['id'])
        print("product model_id :", product[i]['model_id'])
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