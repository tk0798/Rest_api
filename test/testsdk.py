import requests
import json
import time
list = ["905465827921","905077476450","905397235545"]
for i in range(len(list)):

    krjson = f"https://api.chat-api.com/instance349832/sendMessage?phone={list[i]}&body=selam&token=mjmyzdx0hecuclh4"
    krcek = requests.get(krjson)
    kodrehberi = json.loads(krcek.text)
    print(kodrehberi)


