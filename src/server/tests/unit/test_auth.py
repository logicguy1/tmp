import pytest
from sql.databaseMGR import DatabaseManager
from sql.user import User
import random
import string


class TestDbManager(DatabaseManager):
    def get_username_from_email(self, email: str) -> str:
        db, cursor = self._connect()
        username = self._execute_query(db, cursor, 
                                       "SELECT username FROM users WHERE email = %s",
                                       [email])[0]["username"]
        self._close(db)
        return username
    
    def delete_user(self, username: str):
        db, cursor = self._connect()
        self._commit_data(db, cursor, "DELETE FROM users WHERE username = %s;", [username])
        self._close(db)



def random_word(length) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))



DBMGR = TestDbManager()

USERNAME = random_word(10)
EMAIL = f"{random_word(10)}@{random_word(10)}.com"
PASSWORD = random_word(10)




def test_user_signup():
    """
    Test user signup using the User class
    """
    user = User(-1)
    user.register(USERNAME, EMAIL, PASSWORD)
    
    username_from_db = DBMGR.get_username_from_email(EMAIL)
    DBMGR.delete_user(USERNAME)

    assert USERNAME == username_from_db



def test_user_signup_errors():
    """
    Test errors on user signup using the User class
    """
    pass

def test_user_login():
    """
    Test user login using the User class
    """
    pass

def test_user_login_errors():
    """
    Test errors on user login using the User class
    """
    pass