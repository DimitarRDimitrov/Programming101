import sys
import unittest
import hashlib

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.start_protection()
        sql_manager.register('Tester', '123Asdasd')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', 'Aa111111')
        passche = 'Aa111111'
        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', (hashlib.sha1(passche.encode('UTF-8'))).hexdigest()))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123Asdasd')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123Asdasds')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123Asdasd')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_dumbshit(self):
        logged_user = sql_manager.login('Tester', '123Asdasds')
        

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123Asdasd')
        new_password = "12345Asdasd"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
