class UserAuthenticator:
    def authenticate_user(self, username, password):
        print(username, password)

class ProfileManager:
    def update_user_profile(self, firstname, dob):
        print(firstname, dob)

class EmailNotifier:
    def send_email_notification(self, emailid):
        print(emailid)

UA = UserAuthenticator()
print(UA.authenticate_user('ajit', 'pwd'))

PM = ProfileManager()
print(PM.update_user_profile('ajith', '1 jan 1982'))

EN = EmailNotifier()
print(EN.send_email_notification('sajith@ymail.com'))