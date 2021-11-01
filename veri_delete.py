import requests
import postgreSQL

todo = {"id":4,"model_id": 2,"kullanici_id":98745632,"longitude": 35421581,"latitude": 38548167,"toplam_adim":30,"kalori":1605,"oksijen":96,"nabiz":78,"seri_no":10987654321,"yazilim_versiyon":"v2","tarih":"2021-10-18"}
api_url = f"http://rest-api0798.herokuapp.com/azon/api/products/{todo['id']}"
response = requests.delete(api_url)
kullanici_idler=[433]
for i in range(len(kullanici_idler)):

    postgreSQL.delete_database(kullanici_idler[i])

print(response.json())