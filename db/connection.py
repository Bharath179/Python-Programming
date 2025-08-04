# import mysql.connector
#
# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='tiger@12',
#     database='mydb'
# )
#
# cursor = conn.cursor()
# cursor.execute("SELECT DATABASE();")
# print("Connected to:", cursor.fetchone())
# cursor.execute("USE mydb")
# cursor.execute("select ename from emp where sal>1000")
# employees_names = cursor.fetchall()
# cursor.execute("select MAX(sal) from emp")
# max_sal = cursor.fetchone()[0]
# print("Maximum Salary:", max_sal)
# print("Names of employees whose sal is greater then 1000")
# for row in employees_names:
#     print(row[0])
# cursor.execute("select * from emp")
# table = cursor.fetchall()
# print("Total records:", len(table))
# column_names = [asc[0] for asc in cursor.description]
# print(column_names)
# for rows in table:
#     print(rows)
