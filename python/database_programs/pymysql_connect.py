import pymysql

def connectToDb():
    connectionObj = pymysql.Connect(
        host='localhost', port=3306, user='root', password='Root123', db='nithin_db', charset='utf8'
    )
    print('DB connected')
    return connectionObj    

def disconnectDb(connectionObj):
    connectionObj.close()
    print('DB disconnected')

def createTable():
    query = 'create table IF NOT EXISTS students(id int primary key auto_increment, name varchar(32) not null);'
    try:
        conn = connectToDb()
        my_cursor = conn.cursor()
        my_cursor.execute(query)
        my_cursor.close()
    except:
        print('Table creation failed')
    else:
        disconnectDb(conn)

createTable()

def deleteTable():
    query = 'drop table if exists %s ;'
    table_name = input('Enter table to be deleted: ')
    try:
        conn = connectToDb()
        my_cursor = conn.cursor()
        my_cursor.execute(query, table_name)
        print(f'{table_name} table deleted')
        conn.commit()
        my_cursor.close()
    except Exception as e:
        print('Table deletion failed')
        print(e)
    else:
        disconnectDb(conn)

deleteTable()

deleteTable()

def insertRow():
    query = 'insert into students(name) values(%s)';
    name = input('Enter student name: ')
    try:
        conn = connectToDb()
        my_cursor = conn.cursor()
        my_cursor.execute(query, name)
        conn.commit()
        print('Row inserted')
        my_cursor.close()
        disconnectDb(conn)
    except:
        print('Row insertion failed')

insertRow()

def searchRow():
    query = 'select * from students where id = %s'
    student_id = input('Enter Id of the student to be searched: ')
    try:
        conn = connectToDb()
        my_cursor = conn.cursor()
        count = my_cursor.execute(query, student_id)
        if count == 0:
            print(f'Student with id={student_id} not found') 
        else:
            student_row = my_cursor.fetchone()
            print('Student details = ', str(student_row))
        my_cursor.close()
    except Exception as e:
        print('Table deletion failed')
        print(e)
    else:
        disconnectDb(conn)

searchRow()

def readAllRows():
    query = 'select * from students;'
    try:
        conn = connectToDb()
        my_cursor = conn.cursor()
        count = my_cursor.execute(query)
        if count == 0:
            print(f'No Student records found') 
        else:
            student_rows = my_cursor.fetchall()
            print('%-3s %s'%('ID', 'NAME'))
            print('-----------------')
            for student in student_rows:
                #print(str(student))
                print('%-3d %s'%(student[0], student[1]))
            print('-----------------')
        my_cursor.close()
    except Exception as e:
        print('Read All Rows failed')
        print(e)
    else:
        disconnectDb(conn)

readAllRows()

def updateRow():
    query = 'update students set name = %s where id = %s'
    name = input('Enter name to be updated: ')
    id = input('Enter Id of the student to update record: ')
    try:
        conn = connectToDb()
        my_cursor = conn.cursor()
        count = my_cursor.execute(query, (name, id) )
        if count == 0:
            print(f'Student with id={id} not found') 
        else:
            print('Row updated')
        conn.commit()
        my_cursor.close()
    except Exception as e:
        print('Table deletion failed')
        print(e)
    else:
        disconnectDb(conn)

updateRow()


