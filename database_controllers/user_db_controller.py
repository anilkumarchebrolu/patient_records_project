import sqlite3
import streamlit_authenticator as stauth

class UserDBController:
    def __init__(self) -> None:
        self._users_db_connection = sqlite3.connect('data/user_data/users.db')
        self._cursor = self._users_db_connection.cursor()

    def create_usertable(self):
        '''Creates a table to add users'''
        self._cursor.execute(
            '''CREATE TABLE IF NOT EXISTS usertable (
                username VARCHAR(30) NOT NULL, 
                full_name VARCHAR(30) NOT NULL, 
                password VARCHAR(255) NOT NULL
            )'''
        )
        self._users_db_connection.commit()

    def _create_credentials(self, data):
        _usernames = {}
        _credentials = {}
        for user_name, full_name, hashed_password in data:
            info = {"name": full_name, "password": hashed_password}
            _usernames[user_name] = info
        
        _credentials['usernames'] = _usernames
        return _credentials

    def fetch_users(self):
        '''Fetches all the available users'''
        self._cursor.execute('SELECT * FROM usertable')
        _data = self._cursor.fetchall()
        _credentials = self._create_credentials(_data)
        return _credentials

    def create_user(self, user_name, full_name, password):
        '''Create a new user'''
        self.create_usertable()
        hashed_password = stauth.Hasher(passwords=[password]).generate()[0]
        self._cursor.execute(
            'INSERT INTO usertable (username, full_name, password) VALUES  (?, ?, ?)', (user_name, full_name, hashed_password)
        )
        self._users_db_connection.commit()

if __name__ == '__main__':
    user_db_controller = UserDBController()
    # user_db_controller.create_user('Hema', 'Hema Krishna Sai', 'saiclinic')
    # user_db_controller.create_user('Anil', 'Anil Kumar', 'password')
    credentials = user_db_controller.fetch_users()
    print(credentials)