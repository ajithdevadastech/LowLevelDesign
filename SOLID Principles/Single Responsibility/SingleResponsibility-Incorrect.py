class UserManager:
    def authenticate_user(self, username, password):
        print(username, password)

    def update_user_profile(self, firstname, dob):
        print(firstname, dob)

    def send_email_notification(self, emailid):
        print(emailid)

obj = UserManager()
obj.authenticate_user('ajit', 'pwd')
obj.update_user_profile('ajith', '1 Jan 1982')
obj.send_email_notification('sajith@ymail.com')
