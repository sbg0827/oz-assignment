import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='0000',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # 문제 1: 새로운 제품 추가
        sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('Python Book', 29.99, 50))
        conn.commit()

        # 문제 2: 고객 목록 조회
        sql = "SELECT * FROM Customers"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)

        # 문제 3: 제품 재고 업데이트
        sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
        cursor.execute(sql, (1, 1))
        conn.commit()  # 수정된 부분

        # 문제 4: 고객별 총 주문 금액 계산
        sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)

        # 문제 5: 고객 이메일 업데이트
        new_email = "new_email@example.com"  # 예시 이메일
        customer_id = 1  # 예시 고객 ID
        sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
        cursor.execute(sql, (new_email, customer_id))
        conn.commit()  # 수정된 부분

        # 문제 6: 주문 취소
        order_id = 1  # 예시 주문 ID
        sql = "DELETE FROM Orders WHERE orderID = %s"
        cursor.execute(sql, (order_id,))
        conn.commit()  # 수정된 부분

        # 문제 7: 특정 제품 검색
        sql = "SELECT * FROM Products WHERE productName LIKE %s"
        cursor.execute(sql, ('%Book%'))
        for row in cursor.fetchall():
            print(row)

        # 문제 8: 특정 고객의 모든 주문 조회
        sql = "SELECT * FROM Orders WHERE customerID = %s"
        cursor.execute(sql, (1,))
        for row in cursor.fetchall():
            print(row)

        # 문제 9: 가장 많이 주문한 고객 찾기
        sql = """
        SELECT customerID, COUNT(*) as orderCount 
        FROM Orders 
        GROUP BY customerID 
        ORDER BY orderCount DESC 
        LIMIT 1
        """
        cursor.execute(sql)
        top_customer = cursor.fetchone()
        print(f"Top Customer ID: {top_customer['customerID']}, Orders: {top_customer['orderCount']}")

finally:
    conn.close()
