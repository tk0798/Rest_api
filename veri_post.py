import requests
import postgreSQL

kullanici_id=789
model_id=5
model_adi='04.00.166'
longitude=35.21581
latitude=38.48167
toplam_adim=30
kalori=1
oksijen=96
nabiz=78
seri_no=10987654321
yazilim_versiyon='v2'
tarih='2021-10-18'


api_url = 'https://rest-api0798.herokuapp.com/azon/api/products'
todo = {'model_id': model_id,'kullanici_id':kullanici_id,'longitude': longitude,'latitude': latitude,'toplam_adim':toplam_adim,'kalori':kalori,'oksijen':oksijen,'nabiz':nabiz,'seri_no':seri_no,'model_adi': model_adi,'yazilim_versiyon':yazilim_versiyon,'tarih':tarih}
response = requests.post(api_url, json=todo)
postgreSQL.insert_database(kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih)
# print(response.json())
