import requests
import postgreSQL
api_url = "http://127.0.0.1:5000/azon/api/products"
response = requests.get(api_url)
product = response.json()['products']

print("product :",product)

for i in range(len(product)):
    postgreSQL.insert_database(product[i]['kullanici_id'], product[i]['model_id'], product[i]['model_adi'], product[i]['longitude'], product[i]['latitude'],product[i]['toplam_adim'], product[i]['kalori'], product[i]['oksijen'], product[i]['nabiz'],product[i]['seri_no'], product[i]['yazilim_versiyon'], product[i]['tarih'])
