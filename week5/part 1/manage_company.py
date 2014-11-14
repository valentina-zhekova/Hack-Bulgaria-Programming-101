# to fix -> raise exception when id out of range
#        -> set_new_data_employee()
#        -> interface function ...
import sqlite3

DATABASE_FILE = "company_database"


def list_employees(database):
    cursor = database.cursor()

    data = cursor.execute("SELECT id, name, position FROM employees")
    for row in data:
        print("{} - {} - {}".format(row["id"], row["name"], row["position"]))


def monthly_spending(database):
    cursor = database.cursor()

    cursor.execute("""SELECT sum(monthly_salary) AS monthly_spending
                      FROM employees""")
    data = cursor.fetchone()
    print("The company is spending ${} every month!".format(
        data['monthly_spending']))


def yearly_spending(database):
    cursor = database.cursor()

    cursor.execute("""SELECT
                      sum(monthly_salary * 12) AS yearly_salaries_spending,
                      sum(yearly_bonus) AS yearly_bonus_spending
                      FROM employees""")
    data = cursor.fetchone()
    print("The company is spending ${} every year!".format(
        data['yearly_salaries_spending'] + data['yearly_bonus_spending']))


def add_employee(database):
    cursor = database.cursor()

    name = input("name> ")
    monthly_salary = input("monthly_salary> ")
    yearly_bonus = input("yearly_bonus> ")
    position = input("position> ")

    cursor.execute("""INSERT INTO employees(name, monthly_salary,
                                            yearly_bonus, position)
                      VALUES(?,?,?,?)""",
                  (name, monthly_salary, yearly_bonus, position))
    database.commit()


def delete_employee(database, emplyee_id):
    cursor = database.cursor()

    cursor.execute("""SELECT name FROM employees WHERE id = ?""",
                  (emplyee_id,))
    data = cursor.fetchone()
    print("{} was deleted.".format(data['name']))
    cursor.execute("""DELETE FROM employees WHERE id = ?""", (emplyee_id,))
    database.commit()


def update_employee(database, emplyee_id):
    cursor = database.cursor()

    name = input("name> ")
    monthly_salary = input("monthly_salary> ")
    yearly_bonus = input("yearly_bonus> ")
    position = input("position> ")

    cursor.execute("""UPDATE employees SET name = ?, monthly_salary = ?,
                                           yearly_bonus = ?, position = ?
                      WHERE id = ?""",
                  (name, monthly_salary, yearly_bonus, position, emplyee_id))
    database.commit()


def interface():

    print("You can use one of the following commands:"
          "\nlist_employees -> to see all employees"
          "\nmonthly_spending -> prints the total monthly"
          " spending of the comapny for salaries"
          "\nyearly_spending -> prints the total yaerly"
          " spending of the comapny for salaries"
          "\nadd_employee -> to add an employee in the database"
          "\ndelete_employee <emplyee_id> -> delete the given"
          " employee from the database"
          "\nupdate_emplyee <employee_id> -> to update an employee"
          " in the database"
          "\nexit -> to exit the program")

    database = sqlite3.connect(DATABASE_FILE)
    database.row_factory = sqlite3.Row

    while True:
        user_command = input("\ncommand> ")

        if user_command == 'exit':
            break
        elif user_command == 'list_employees':
            list_employees(database)
        elif user_command == 'monthly_spending':
            monthly_spending(database)
        elif user_command == 'yearly_spending':
            yearly_spending(database)
        elif user_command == 'add_employee':
            add_employee(database)
        elif user_command.split()[0] == 'delete_employee':
            delete_employee(database, user_command.split()[1])
        elif user_command.split()[0] == 'update_employee':
            update_employee(database, user_command.split()[1])
        else:
            print("There is no such command, try again!")

    database.close()


def main():
    interface()

if __name__ == '__main__':
    main()
