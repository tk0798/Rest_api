import requests

api_url = 'https://rest-api0798.herokuapp.com/azon/api/products/'
todo = {'id':4,'model_id': 5,'kullanici_id':9632,'longitude': 35421581,'latitude': 38548167,'toplam_adim':30,'kalori':1,'oksijen':96,'nabiz':78,'seri_no':10987654321,'model_adi': '04.00.166','yazilim_versiyon':'v2','tarih':'2021-10-18'}
response = requests.post(api_url, json=todo)

print(response.json())
