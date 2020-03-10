import hashlib
import dbConnection


con, cur = dbConnection.getDB()


class LoginSystem:
    def login(self, username, passw):
        # need to check if user is in database first!!!!!
        checkUser = 'select username from "Users"' \
                    "where username='%s'" % username
        cur.execute(checkUser)
        user = cur.fetchone()

        if user is not None and self.check_password(username, passw):
            print('Login successful')
            return True
        else:
            print('Credentials invalid')
            return False

    def create_hash_password(self, passw):
        return hashlib.sha3_256(str.encode(passw)).hexdigest()

    def check_password(self, username, passw):
        query = 'select password from "Users" ' \
                    "where username='%s'" % username
        print(query)
        cur.execute(query)
        password_db = cur.fetchone()
        print(password_db)
        # if self.Users[username] == self.create_hash_password(passw):
        if password_db[0] == self.create_hash_password(passw):
            return True
        else:
            return False

