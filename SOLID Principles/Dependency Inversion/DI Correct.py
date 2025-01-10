class email_client(object):
    def send_email(self, subject, body, frommail, toEmail):
        raise NotImplementedError

class gmail_client(email_client):
    def send_email(self, subject, body, frommail, toEmail):
        raise NotImplementedError

class outlook_client(email_client):
    def send_email(self, subject, body, frommail, toEmail):
        raise NotImplementedError

"""
parent class email_client with 2 children gmail_client & outlook_client
"""

class email_service(object):
    def __init__(self, emailClient):
        self.emailClient = emailClient

    def send_email(self, subject, body, frommail, toEmail):
        self.emailClient.send_email(subject, body, frommail, toEmail)

#usage
gmailClient = gmail_client()
emailService = email_service(gmailClient)
emailService.send_email("subject", "body", "frommail", "toEmail")


