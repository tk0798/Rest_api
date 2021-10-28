import psycopg2
def insert_local_database(kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih):

    print("buraya kadar girdi")
    try:
        connection = psycopg2.connect(user = "postgres",
                          password = "1998*k2005",
                          host = "localhost",
                          port = "5432",
                          database = "deneme")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO saat_veri (kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih)
        cursor.execute(postgres_insert_query,record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Kaydedildi")

    except (Exception, psycopg2.Error) as error:
        print("Hata oldu", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("Bağlantı kapandı")



#### Herokudaki postgresql'e bağlanma
import json
import os


import psycopg2

# DATABASE_URL = os.environ['dfur5u5oon6kmi']


def veritabani_olusturma():
    try:
        db = psycopg2.connect(
            'postgres://arpoydbrxhqzfv:444c6c5f46296d3a9c9843a2be3ae4c556171473dababd686b868822b080a31b@ec2-54-195-246-55.eu-west-1.compute.amazonaws.com:5432/dfur5u5oon6kmi',
            sslmode='require')

        imlec = db.cursor()

        print(db.get_dsn_parameters())
        komut_CREATE = """ CREATE TABLE IF NOT EXISTS public.saat_veri
        (
            kullanici_id integer,
            model_id integer,
            longitude double precision,
            latitude double precision,
            toplam_adim integer,
            kalori integer,
            oksijen integer,
            nabiz integer,
            seri_no bigint,
            yazilim_versiyon text COLLATE pg_catalog."default",
            tarih date,
            id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
            model_adi text COLLATE pg_catalog."default",
            CONSTRAINT saat_veri_pkey PRIMARY KEY (id)
        );
                        """

        imlec.execute(komut_CREATE)
        db.commit()

        print("çalıştı")
    except (Exception, psycopg2.Error) as error:
        print("Hata oldu", error)

    finally:
        # closing database connection.
        if db:
            imlec.close()
            db.close()
            print("Bağlantı kapandı")

def insert_database(kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih):
    try:
        db = psycopg2.connect(
            'postgres://arpoydbrxhqzfv:444c6c5f46296d3a9c9843a2be3ae4c556171473dababd686b868822b080a31b@ec2-54-195-246-55.eu-west-1.compute.amazonaws.com:5432/dfur5u5oon6kmi',
            sslmode='require')

        cursor = db.cursor()

        postgres_insert_query = """ INSERT INTO saat_veri (kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (kullanici_id, model_id, model_adi, longitude, latitude, toplam_adim, kalori, oksijen, nabiz, seri_no, yazilim_versiyon, tarih)
        cursor.execute(postgres_insert_query,record_to_insert)

        db.commit()
        count = cursor.rowcount
        print(count, "Kaydedildi")

    except (Exception, psycopg2.Error) as error:
        print("Hata oldu", error)

    finally:
        # closing database connection.
        if db:
            cursor.close()
            db.close()
            print("Bağlantı kapandı")


def select_database():
    try:
        db = psycopg2.connect(
            'postgres://arpoydbrxhqzfv:444c6c5f46296d3a9c9843a2be3ae4c556171473dababd686b868822b080a31b@ec2-54-195-246-55.eu-west-1.compute.amazonaws.com:5432/dfur5u5oon6kmi',
            sslmode='require')

        cursor_select = db.cursor()
        komut_SELECT = "SELECT * FROM saat_veri"
        cursor_select.execute(komut_SELECT)
        db.commit()
        liste = cursor_select.fetchall()

        for i in liste:
            print(i)

    except (Exception, psycopg2.Error) as error:
        print("Hata oldu", error)

    finally:
        # closing database connection.
        if db:
            cursor_select.close()
            db.close()
            print("Bağlantı kapandı")

def list_database():
    try:

        db = psycopg2.connect(
            'postgres://arpoydbrxhqzfv:444c6c5f46296d3a9c9843a2be3ae4c556171473dababd686b868822b080a31b@ec2-54-195-246-55.eu-west-1.compute.amazonaws.com:5432/dfur5u5oon6kmi',
            sslmode='require')

        cursor_list = db.cursor()
        komut_SELECT = "SELECT * FROM saat_veri"
        cursor_list.execute(komut_SELECT)
        db.commit()
        liste = cursor_list.fetchall()
        print("liste :",liste)
        x = []

        for i in range(len(liste)):
            jsonum = {"kullanici_id": liste[i][0], "model_id": liste[i][1], "model_adi": liste[i][12],
                      "longitude:": liste[i][2], "latitude": liste[i][3], "toplam_adim": liste[i][4],
                      "kalori:": liste[i][5],
                      "oksijen": liste[i][6], "nabiz": liste[i][7], "seri_no": liste[i][8],
                      "yazilim_versiyon": liste[i][9],
                      "tarih": str(liste[i][10])}
            x.append(jsonum)
            print("sonuc :", x)
        print("tüm sonuc :", {"products":x})
        return {"products":x}
    except (Exception, psycopg2.Error) as error:
        print("Hata oldu", error)

    finally:
        # closing database connection.
        if db:
            cursor_list.close()
            db.close()
            print("Bağlantı kapandı")


def delete_database(kullanici_id):
    try:
        db = psycopg2.connect(
            'postgres://arpoydbrxhqzfv:444c6c5f46296d3a9c9843a2be3ae4c556171473dababd686b868822b080a31b@ec2-54-195-246-55.eu-west-1.compute.amazonaws.com:5432/dfur5u5oon6kmi',
            sslmode='require')

        cursor = db.cursor()

        postgres_delete_query = """DELETE FROM saat_veri WHERE kullanici_id=%s"""
        record_to_delete = (kullanici_id)
        cursor.execute(postgres_delete_query,record_to_delete)

        db.commit()
        count = cursor.rowcount
        print(count, "Veritabanından silindi")

    except (Exception, psycopg2.Error) as error:
        print("Hata oldu", error)

    finally:
        # closing database connection.
        if db:
            cursor.close()
            db.close()
            print("Bağlantı kapandı")
##model adı konusunda felan sıkıntı var veri çekiliyor ama tam doğru değil


# insert_database(100000,2,3,4,5,6,7,8,9,10,'v4','2021-10-16')
# select_database()
# list_database()
# delete_database(1)