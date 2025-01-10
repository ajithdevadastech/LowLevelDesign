class gmail_client(object):
    def send_email(self, subject, body, fromEmail, toEmail):
        raise NotImplementedError

class email_service(object):
    def __init__(self):
        self.email_client = gmail_client()

    def send_email(self, subject, body, fromEmail, toEmail):
        self.email_client.send_email(subject, body, fromEmail, toEmail)


"""
violates DI because, email_service is strongly coupled with a lowe level service gmail_client.
"""