import sqlite3


def db_init():
    db = sqlite3.connect("cinemadb")
    cursor = db.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY,
                 name TEXT, rating REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                    projections(id INTEGER PRIMARY KEY,
                    movie_id INTEGER REFERENCES  movies(id),
                    type TEXT, date TEXT, time TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                    reservations(id INTEGER PRIMARY KEY,
                    username TEXT, projection_id INTEGER
                    REFERENCES projections(id),
                    row INTEGER, col INTEGER)''')
    db.commit()


def add_movie():
    db = sqlite3.connect("cinemadb")
    cursor = db.cursor()
    name = input("Name of movie: ")
    rating = float(input("Rating: "))
    cursor.execute(
        "INSERT INTO movies(name,rating) VALUES(?,?)", (name, rating))
    db.commit()


def add_projection():
    db = sqlite3.connect("cinemadb")
    cursor = db.cursor()
    movie_id = int(input("Enter movie id: "))
    type_movie = input("Enter type: ")
    date = input("Enter date in format yyyy-mm-dd: ")
    time = input("Enter time in format hh:mm: ")
    cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                    VALUES(?,?,?,?)''', (movie_id, type_movie, date, time))
    db.commit()


def add_reservation():
    db = sqlite3.connect("cinemadb")
    cursor = db.cursor()
    name = input("Enter name of reservator: ")
    projection_id = int(input("Enter the projection ID: "))
    availability = cursor.execute(
        "SELECT id FROM projections WHERE id = (?)", (projection_id,))
    # print(availability.fetchone())
    while (availability.fetchone() is None):
        projection_id = int(input("Enter a valid projection ID: "))
        availability = cursor.execute(
            "SELECT id FROM projections WHERE id = (?)", (projection_id,))
    row_col = input("Enter seat in the following format 'row,col': ")
    row_col = row_col_checker(row_col)
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                    VALUES (?,?,?,?)''', (name, projection_id, row_col[0], row_col[1]))
    db.commit()


# def if_available(row_col, projection_id):
#     db = sqlite3.connect("cinemadb")
#     cursor = db.currosor()
#     while check_position(row_col) is False:
#         row_col = input("Enter any number row and col from 1 to 10: ")
#         row_col = row_col.split(',')
#     availability = cursor.execute(
#         "SELECT projection_id, row, col FROM reservations")
#     for seat in availability:
#         if row_col == (seat[1], seat[2]) and projection_id == seat[0]:
#             print("This seat is already taken.")
#             row_col = input("Enter seat in the following format row,col: ")
#             row_col.split(',')
#             if_available(row_col, projection_id)
def row_col_checker(row_col):
    db = sqlite3.connect("cinemadb")
    cursor = db.cursor()
    row_col = row_col.split(',')
    while check_position(row_col) is not True:
        row_col = input("Enter any number row and col from 1 to 10: ")
        row_col = row_col.split(',')
    is_available_seat = cursor.execute("SELECT row, col FROM reservations")
    for seat in is_available_seat:
        if int(row_col[0]) == seat[0] and int(row_col[1]) == seat[1]:
            row_col = input("The seat is already taken! Enter different one: ")
            row_col_checker(row_col)
    return row_col


def check_position(row_col):
    if 0 < int(row_col[0]) < 11 and 0 < int(row_col[1]) < 11:
        return True
    return False


# def check_projection(projection_id):
#     db = sqlite3.connect("cinemadb")
#     cursor = db.cursor()
#     all_projections = cursor.execute("SELECT projection_id FROM projections")
#     for projection in all_projections:
#         if projection_id == projection:
#             return True
#     return False


# def main():
#     # add_movie()
#     # add_movie()
#     # add_projection()
#     # add_projection()
#     # add_projection()
#     # add_projection()
#     add_reservation()


# if __name__ == '__main__':
#     main()
