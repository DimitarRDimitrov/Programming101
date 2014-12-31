import sqlite3
from create_company import add_company_member


user_input = ""


def check_input(user_input):
    if (user_input == "list employees" or user_input == "monthly spending" or
            user_input == "yearly spending" or user_input == "add employee" or
            user_input == "delete employee" or user_input == "update employee"
            or user_input == "available commands"):
        return True
    return False


def list_employees():
    db = sqlite3.connect("mydb")
    cursor = db.cursor()
    employees = cursor.execute("SELECT id, name, position FROM employees")
    for row in employees:
        print("%d - %s - %s" % (row[0], row[1], row[2]))


def monthly_spending():
    total = 0
    db = sqlite3.connect("mydb")
    # db_row_factory = sqlite3.Row
    cursor = db.cursor()
    expenses = cursor.execute("SELECT monthly_salary FROM employees")
    for value in expenses:
        total += value[0]
    return total


def yearly_spending():
    total = 0
    for month in range(1, 12):
        total += monthly_spending()
    db = sqlite3.connect("mydb")
    cursor = db.cursor()
    yearly_bonus_expense = cursor.execute("SELECT yearly_bonus FROM employees")
    for bonus in yearly_bonus_expense:
        total += bonus[0]
    return total


def add_employee():
    add_company_member()


def delete_employee(employee_id):
    db = sqlite3.connect("mydb")
    cursor = db.cursor()
    fired_name = cursor.execute(
        "SELECT name FROM employees WHERE id = ?", (employee_id,)).fetchone()
    # print("%s was deleted." % fired_name)
    print("{} was deleted.".format(fired_name[0]))
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    db.commit()
# {}.format()


def update_employee(employee_id):
    name = input("Name: ")
    salary = input("Salary: ")
    bonus = input("Bonus: ")
    position = input("Position: ")
    db = sqlite3.connect("mydb")
    cursor = db.cursor()
    cursor.execute("UPDATE employees SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?",
                   (name, salary, bonus, position, employee_id))
    db.commit()


def available_commands():
    print(
        '''Avaliable commands:\n list employees\n monthly spending\n yearly spending\n add employee\n delete employee\n update employee\n''')
    print("Type 'available commands' to review them again\nor 'quit' to exit the management tool.")


def main():
    # list_employees()
    # print(monthly_spending())
    # print(yearly_spending())
    # add_employee()
    # update_employee(6)
    # delete_employee(6)
    list_employees()
    available_commands()
    user_input = input("Enter a command: ")
    while user_input != "quit":
        while check_input(user_input) is False:
            user_input = input("Please enter a valid command: ")
        if user_input == "list employees":
            list_employees()
            user_input = input("Enter a command: ")
        elif user_input == "monthly spending":
            print(monthly_spending())
            user_input = input("Enter a command: ")
        elif user_input == "yearly spending":
            print(yearly_spending())
            user_input = input("Enter a command: ")
        elif user_input == "add employee":
            add_employee()
            user_input = input("Enter a command: ")
        elif user_input == "delete employee":
            to_be_deleted = input("Please enter the specific ID: ")
            delete_employee(to_be_deleted)
            user_input = input("Enter a command: ")
        elif user_input == "update employee":
            to_be_updated = input("Please enter the specific ID: ")
            update_employee(to_be_updated)
            user_input = input("Enter a command: ")
        elif user_input == "available commands":
            available_commands()
            user_input = input("Enter a command: ")
    print("\nThank you for using the management tool!")

if __name__ == '__main__':
    main()
