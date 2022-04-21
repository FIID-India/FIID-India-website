from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        self.email.send(fail_silently=False)


def contact_email(name, message, email_to, email_from, email_subject, email_template):
    html_content = render_to_string(email_template, {'name':name,'message':message, 'email':email_from, 'subject':email_subject})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        email_subject,
        text_content,
        None,
        email_to
    )
    email.attach_alternative(html_content, 'text/html')
    EmailThread(email).start()

def subscriber_welcome_email(full_name, subject, to_email, email_template):
    html_content = render_to_string(email_template, {'full_name':full_name, 'email':to_email})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject,
        text_content,
        None,
        to_email
    )
    email.attach_alternative(html_content, 'text/html')
    EmailThread(email).start()


def subscriber_email(full_name, subject, to_email, message, email_template, file):
    html_content = render_to_string(email_template, {'full_name':full_name, 'message':message})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject,
        text_content,
        None,
        to_email
    )

    email.attach_alternative(html_content, 'text/html')
    EmailThread(email).start()