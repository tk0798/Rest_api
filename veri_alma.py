from flask import Flask, jsonify
from flask import make_response
from flask import request

import requests
api_url = "https://rest-api0798.herokuapp.com"
response = requests.get(api_url)
product = response.json()['products']

print("product :",product)


import pyodbc

db = pyodbc.connect(
            Driver='{SQL Server}',
            Server='DESKTOP-40GMAHB\MSSSQLSERVER',
            DATABASE='saat',
            Trusted_Connection='True'
        )
imlec = db.cursor()

for i in range(len(product)):
    print("product id :", product[i]['id'])
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
    try:
        imlec.execute(
            'INSERT INTO saat_veri (kullanici_id,model_id,longitude,latitude,toplam_adim,kalori,oksijen,nabiz,seri_no,yazilim_versiyon,tarih) values (?,?,?,?,?,?,?,?,?,?,?)',
            product[i]['kullanici_id'], product[i]['model_id'], product[i]['longitude'], product[i]['latitude'],
            product[i]['toplam_adim'], product[i]['kalori'], product[i]['oksijen'], product[i]['nabiz'],
            product[i]['seri_no'], product[i]['yazilim_versiyon'], product[i]['tarih'])
        db.commit()
        print("1 kayıt eklendi")
    except Exception as e:
        print(e)
        print("olmadı 18")

# if len(product['product']) == 0:
#     return jsonify({'product': 'Not found'}), 404
# return jsonify({'product': product})