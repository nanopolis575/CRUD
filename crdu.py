import pymysql

conn = pymysql.connect(host='127.0.0.1', user='u0_a54', password='', db='crud_py', port=3306)

with conn:
    cursors = conn.cursor()
    print("Connected")

def create_employee():
    print("Create employee")
    employee_id = input("Input worker's ID::")
    employee_name = input("Input worker's name::")
    employee_salary = input("Input worker's salary:")
    insertion_query = "INSERT INTO employees(id, name, salary) VALUES (" + employee_id + ", " + employee_name + ", " + employee_salary + ");"
    cursors.execute(insertion_query)
    conn.commit()
    print(cursors.rowcount, "Employee registered")


def edit_employee():
    print("Edit employee")
    employee_id = input("Input employee's ID:")
    loo = 1
    while loo==1:
        opc = input("1.- Modify name\n 2.-Modify salary")
        if opc==1:
            employee_name =  input("Input the new name:")
            update_query = "UPDATE employees Set Name= " + employee_name + "WHERE ID = "+ employee_id +";"
        if opc==2:
            employee_salary = input("Input the new name:")
            update_query = "UPDATE employees Set Name= " + employee_salary + "WHERE id = "+ employee_id +";"
    cursors.execute(update_query)
    conn.commit()
    print("Employee updated")


def find_employee():
    print("Find employee")
    employee_id = input("Input employee's ID:")
    select_query = "SELECT * FROM employees(code, name, salary) WHERE id = "+ employee_id +";"
    cursors.execute(select_query)
    fetched = cursors.fetchall()
    for i in fetched:
        print(i)
    conn.commit()


def delete_employee():
    print("Delete employee")
    employee_id = input("Input employee's ID:")
    delete_query = "DELETE * FROM employees WHERE id = "+ employee_id +";"
    cursors.execute(delete_query)
    conn.commit()


def index_employees():
    print("Index employees")
    select_query = "SELECT * FROM employees"
    cursors.execute(select_query)
    fetched = cursors.fetchall()
    for i in fetched:
        print(i)
    conn.commit()


def main():
    cycle = 0

    while cycle == 0:
        print("MYSQL CRUD WITH PYMYSQL")
        print("1. Insert employee\n2. Search employee by id\n3.- Edit employee")
        print("4. Delete employee \n5. List all employees \n6. Exit\n")
        user_option = input("Select an option between 1 and 6: ")

        if user_option == 1:
            create_employee()
        elif user_option == 2:
            find_employee()
        elif user_option == 3:
            edit_employee()
        elif user_option == 4:
            delete_employee()
        elif user_option == 5:
            index_employees()
        elif user_option == 6:
            cycle = 1
    else:
        print("Please check your input, you must input one number that could be in range of these values: 1 and 6")


if __name__ == "__main__":
    main()