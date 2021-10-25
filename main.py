from flask import Flask, jsonify
from flask import make_response
from flask import request
import json
products = [
    {
        'id': 1,
        'model_id': 1,
        'model_adi': '04.00.006',
        'longitude': '35.421585',
        'latitude': '38.543869',
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
        'longitude': '35.429371',
        'latitude': '38.543868',
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
        'longitude': '35.421581',
        'latitude': '38.548167',
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


@app.route('/', methods=['GET'])
def get_products():
    return jsonify({'products': products})
# import pyodbc
#
# db = pyodbc.connect(
#             Driver='{SQL Server}',
#             Server='DESKTOP-40GMAHB\MSSSQLSERVER',
#             DATABASE='saat',
#             Trusted_Connection='True'
#         )
# imlec = db.cursor()


@app.route('/<int:product_id>', methods=['GET'])
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
    #     try:
    #         imlec.execute('INSERT INTO saat_veri (kullanici_id,model_id,longitude,latitude,toplam_adim,kalori,oksijen,nabiz,seri_no,yazilim_versiyon,tarih) values (?,?,?,?,?,?,?,?,?,?,?)',
    #                       product[i]['kullanici_id'], product[i]['model_id'],product[i]['longitude'],product[i]['latitude'],product[i]['toplam_adim'],product[i]['kalori'],product[i]['oksijen'],product[i]['nabiz'],product[i]['seri_no'],product[i]['yazilim_versiyon'],product[i]['tarih'])
    #         db.commit()
    #         print("1 kayıt eklendi")
    #     except Exception as e:
    #         print(e)
    #         print("olmadı 18")
    #
    if len(product) == 0:
        return jsonify({'product': 'Not found'}), 404
    return jsonify({'product': product})


@app.route('/', methods=['POST'])
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


@app.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'product': 'Not found'}), 404
    products.remove(product[0])
    return jsonify({'result': True})


# @app.errorhandler(404)
# def not_found(error):
#     return make_response(
#         jsonify({'HTTP 404 Error': 'The content you looks for does not exist. Please check your request.'}), 404)


if __name__ == '__main__':
    app.run(debug=True)  # !flask/bin/python