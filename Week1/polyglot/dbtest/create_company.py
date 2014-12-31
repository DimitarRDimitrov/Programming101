import sqlite3


db = sqlite3.connect('mydb')
cursor = db.cursor()


def init():
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(id INTEGER
                            PRIMARY KEY, name TEXT, monthly_salary INTEGER,
                             yearly_bonus INTEGER, position TEXT)''')
    db.commit()


def add_company_member():
    name = input("Name: ")
    salary = input("Salary: ")
    bonus = input("Bonus: ")
    position = input("Position: ")
    cursor.execute('''INSERT INTO employees(name, monthly_salary,
                    yearly_bonus, position)
                    VALUES(?,?,?,?)''', (name, salary, bonus, position))
    db.commit()


def main():
    init()
    # add_company_member()  
    result = cursor.execute("SELECT * FROM employees")
    for row in result:
        print(row)
    db.close()


if __name__ == '__main__':
    main()

