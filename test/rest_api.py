import requests
import json
api_url = "http://127.0.0.1:5000/azon/api/products/"
todo = {"id":14,"model_id": 2,"kullanici_id":98745632,"longitude": 35421581,"latitude": 38548167,"toplam_adim":30,"kalori":1605,"oksijen":96,"nabiz":78,"seri_no":10987654321,"yazilim_versiyon":"v2","tarih":"2021-10-18"}
response = requests.post(api_url, json=todo)

print(response.json())