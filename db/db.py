import pymysql

connection = pymysql.connect(host='localhost', user='root', password='tiger@12', database='testdb')
cursor = connection.cursor()

# Departments Table
dept_table = """
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100)
)
"""
cursor.execute(dept_table)
print("Departments Table is created successfully")

# Employees Table
emp_table = """
CREATE TABLE IF NOT EXISTS employees(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
dept_id INT,
FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
"""
cursor.execute(emp_table)
print("Employees Table is created successfully")

# insert_query = "INSERT INTO departments (dept_id, name, dept_name) VALUES (%s, %s, %s)"
# data = (101, 'Alice', 'Sales')

# delete_record = "DELETE FROM departments WHERE dept_id='101'"
# cursor.execute(delete_record)

# cursor.execute(insert_query, data)
# print("Record is inserted successfully")

# delete_column = "ALTER TABLE departments DROP COLUMN name"
# cursor.execute(delete_column)
# print("Name column has been dropped")

connection.commit()

cursor.close()
connection.close()
