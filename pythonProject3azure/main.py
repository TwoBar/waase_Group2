import mysql.connector
try:
    conn = mysql.connector.connect(user='baba@barnaserver',
                                   password='BBgang22',
                                   database='northwind',
                                   host='barnaserver.mysql.database.azure.com')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

except mysql.connector.Error as err:
    print(err)