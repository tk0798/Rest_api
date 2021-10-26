# import psycopg2
def insert_database(kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih):

    print("buraya kadar girdi")
    # try:
    #     connection = psycopg2.connect(user = "postgres",
    #                       password = "1998*k2005",
    #                       host = "localhost",
    #                       port = "5432",
    #                       database = "deneme")
    #     cursor = connection.cursor()
    #
    #     postgres_insert_query = """ INSERT INTO saat_veri (kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    #     record_to_insert = (kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih)
    #     cursor.execute(postgres_insert_query,record_to_insert)
    #
    #     connection.commit()
    #     count = cursor.rowcount
    #     print(count, "Kaydedildi")
    #
    # except (Exception, psycopg2.Error) as error:
    #     print("Hata oldu", error)
    #
    # finally:
    #     # closing database connection.
    #     if connection:
    #         cursor.close()
    #         connection.close()
    #         print("Bağlantı kapandı")

