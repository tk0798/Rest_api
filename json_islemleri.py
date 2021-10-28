# import json
# x = {}
# x = json.dumps(x)
# for i in range(2):
#
#     json1 = {'asd':1,'das':'aassdd'}
#
#     y=json.dumps(json1)
#
#     z = x+y
# print(z)


def list_database():
    import json
    liste = [(1, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 1, '3'), (100, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 2, '3'), (100, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 3, '3'), (100000, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 4, '3'), (100000, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 5, '3'), (100000, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 6, '3'), (100000, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 7, '3'), (100000, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 8, '3'), (100000, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 9, '3'), (100000, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 10, '3'), (100000, 2, 4.0, 5.0, 6, 7, 8, 9, 10, 'v4', (2021, 10, 16), 11, '3')]
    x = {}
    x = json.dumps(x)
    for i in range(len(liste)):
        jsonum = {"kullanici_id": liste[i][0], "model_id": liste[i][1], "model_adi": liste[i][12],
                  "longitude:": liste[i][2], "latitude": liste[i][3], "toplam_adim": liste[i][4], "kalori:": liste[i][5],
                  "oksijen": liste[i][6], "nabiz": liste[i][7], "seri_no": liste[i][8], "yazilim_versiyon": liste[i][9],
                  "tarih": liste[i][10]}
        y = json.dumps(jsonum)
        x = x +",\n"+ y
        print("sonuc :",x)
    print("tüm sonuc :",x)
    return x


list_database()