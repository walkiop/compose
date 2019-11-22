
# Connect to the database
connection = pymysql.connect(host='mysql',
                             user='root',
                             password='senhaFiap',
                             db='fiapdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT posicao, valor FROM fibonacci WHERE posicao = %s"
        cursor.execute(sql, 5)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
