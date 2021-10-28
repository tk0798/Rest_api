import requests
import postgreSQL
api_url = "http://rest-api0798.herokuapp.com/azon/api/products"
response = requests.get(api_url)
print(response.json())
product = response.json()

print("product :",product)

for i in range(len(product)):
    postgreSQL.select_database()