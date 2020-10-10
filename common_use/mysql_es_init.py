import mysql.connector
from elasticsearch import Elasticsearch

DB_USER = 'root'
DB_PASS = 'sneakerhead'
DB_HOST = '10.0.0.131'
DB = 'vo_account'
ES_HOST = '10.0.0.142'
ESBT_CART = 'esbt_cart'


def read_carts():
    cnx = mysql.connector.connect(user=DB_USER, password=DB_PASS,
                                  host=DB_HOST,
                                  database=DB)
    cursor = cnx.cursor()
    query = "SELECT * FROM mt_platform_cart"
    cursor.execute(query)
    rows = []
    for arr in cursor:
        rows.append(arr)
    cursor.close()
    cnx.close()
    print(rows.__sizeof__())
    print(rows.__sizeof__())
    return rows


def create_doc():
    es = Elasticsearch([
        {'host': ES_HOST}
    ])
    for row in carts:
        print(row)
        body = {
            "id": row[0],
            "sellerId": row[2],
            "platformId": row[3],
            "cartId": row[5],
            "cartName": row[6]
        }
        es.create(index=ESBT_CART, id=body['id'], body=body)
    result = es.search(index=ESBT_CART)
    print(result)


if __name__ == '__main__':
    # read_es()
    carts = read_carts()
    # create_doc()
