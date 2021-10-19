import requests
import json
api_url = "http://127.0.0.1:5000/azon/api/products/"
todo = {"id":4,"model_id": 2,"kullanici_id":98745632,"longitude": 35421581,"latitude": 38548167,"toplam_adim":30,"kalori":1,"oksijen":96,"nabiz":78,"seri_no":10987654321,"yazilim_versiyon":"v2","tarih":"2021-10-18"}
response = requests.post(api_url, json=todo)
todom = {"id":5,"model_id": 2,"kullanici_id":98745632,"longitude": 35421581,"latitude": 38548167,"toplam_adim":30,"kalori":2,"oksijen":96,"nabiz":78,"seri_no":10987654321,"yazilim_versiyon":"v2","tarih":"2021-10-18"}
responsem = requests.post(api_url, json=todom)
todomm = {"id":6,"model_id": 2,"kullanici_id":98745632,"longitude": 35421581,"latitude": 38548167,"toplam_adim":30,"kalori":3,"oksijen":96,"nabiz":78,"seri_no":10987654321,"yazilim_versiyon":"v2","tarih":"2021-10-18"}
responsemm = requests.post(api_url, json=todomm)
todommm = {"id":7,"model_id": 2,"kullanici_id":98745632,"longitude": 35421581,"latitude": 38548167,"toplam_adim":30,"kalori":4,"oksijen":96,"nabiz":78,"seri_no":10987654321,"yazilim_versiyon":"v2","tarih":"2021-10-18"}
responsemmm = requests.post(api_url, json=todommm)
todommmm = {"id":8,"model_id": 2,"kullanici_id":98745632,"longitude": 35421581,"latitude": 38548167,"toplam_adim":30,"kalori":5,"oksijen":96,"nabiz":78,"seri_no":10987654321,"yazilim_versiyon":"v2","tarih":"2021-10-18"}
responsemmmm = requests.post(api_url, json=todommmm)
todommmmm = {"id":9,"model_id": 2,"kullanici_id":98745632,"longitude": 35421581,"latitude": 38548167,"toplam_adim":30,"kalori":6,"oksijen":96,"nabiz":78,"seri_no":10987654321,"yazilim_versiyon":"v2","tarih":"2021-10-18"}
responsemmmmm = requests.post(api_url, json=todommmmm)

# res =requests.put(url=api_url,data=todommmm,json=todommmmm)
# print("deneme put :",res)
print(response.json())
print(responsem.json())
print(responsemm.json())
print(responsemmm.json())
print(responsemmmm.json())
print(responsemmmmm.json())