import pymysql

connectionObj = pymysql.Connect(
    host='localhost',port=3306,
    user='root',password='root123',
    db='employee',charset='utf8')