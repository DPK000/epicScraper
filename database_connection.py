import pymysql
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             database='blog', )
cursor = connection.cursor()
sql_query = "SELECT VERSION()"

try:
    cursor.execute(sql_query)
    data = cursor.fetchone()
    print("Database Version : %s" % data)

except Exception as e:
    print("Exeption : ", e)

    connection.close()
