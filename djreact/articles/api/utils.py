from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject='Welcome to the Wall', body=data['message'], to=[data['to']])
        email.send()
