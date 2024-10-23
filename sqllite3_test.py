import sqlite3

# 1. SQLite 데이터베이스 연결
conn = sqlite3.connect(':memory:') #일회성 DB에 연결 
cursor = conn.cursor()

# 2. 테이블 생성
cursor.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
conn.commit()

# 3. 데이터 삽입
# 3.1. string 사용
cursor.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")

#3.2. 튜플 사용 
name = 'SangJung'
phoneNumber = '010-5670-2343'
cur = conn.cursor()
cur.execute('INSERT INTO PhoneBook VALUES(?, ?);', (name, phoneNumber))

#3.3. 딕셔너리 사용 
name = 'SangJung'
phoneNumber = '010-5670-2343'
cur = conn.cursor()
cur.execute('INSERT INTO PhoneBook VALUES(:name, :phoneNumber);', {"name":name, "phoneNumber":phoneNumber})

#3.4. 리스트 사용
dataList = (('Tom', '010-543-5432'), ('DSP', '010-123-1234'))
cur = conn.cursor()
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", dataList)

conn.commit()

# 4. 데이터 조회
cursor.execute('SELECT * FROM PhoneBook')
rows = cursor.fetchall() #모두 조회
# cur.fetchone() 단건 조회
# cur.fetchmany(2) 다건 조회 -> 2개 조회함.

for row in rows:
    print(row)

# 5. 연결 종료
conn.close()
