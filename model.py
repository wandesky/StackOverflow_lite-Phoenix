from werkzeug.security import generate_password_hash, check_password_hash
USER_DICT = {}


class Users():
    '''class to represent user model'''

    def put(self, name, username, email, password):
        '''add a user to USERS'''
        self.user = {}
        if username in USER_DICT:
            return {"message": "User with the given username already exists"}
        self.user["name"] = name
        self.user["email"] = email
        pw_hash = generate_password_hash(password)
        self.user["password"] = pw_hash

        USER_DICT[username] = self.user

        return {"message": 'successfully registered as {}'.format(username)}
