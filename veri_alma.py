import requests
import postgreSQL
api_url = "http://rest-api0798.herokuapp.com/azon/api/products"
response = requests.get(api_url)
print(response.json()['products'])
product = response.json()['products']

for i in range(len(product)):
    postgreSQL.insert_database(product[i]['kullanici_id'], product[i]['model_id'], product[i]['model_adi'], product[i]['longitude'], product[i]['latitude'],product[i]['toplam_adim'], product[i]['kalori'], product[i]['oksijen'], product[i]['nabiz'],product[i]['seri_no'], product[i]['yazilim_versiyon'], product[i]['tarih'])
