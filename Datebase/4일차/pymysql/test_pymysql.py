import pymysql
import pymysql.cursors

connection = pymysql.connect(
    host='127.0.0.1',  # 로컬 서버의 IP 주소
    user='root',  # MySQL 사용자 이름
    password='0000',  # MySQL 비밀번호
    db='classicmodels',  # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

sql = "SELECT * FROM customers"
cursor.execute(sql)

customers = cursor.fetchone()
print("customers : ", customers)
print("customers : ", customers['id'])
print("customers : ", customers['country'])
print("customers : ", customers['customerName'])


