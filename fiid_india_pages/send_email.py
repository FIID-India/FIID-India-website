from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def contact_email(name, message, email_to, email_from, email_subject, email_template):
    html_content = render_to_string(email_template, {'name':name,'message':message, 'email':email_from})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        email_subject,
        text_content,
        None,
        email_to
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()

def subscriber_email(full_name, subject, to_email, message, email_template):
    html_content = render_to_string(email_template, {'full_name':full_name, 'email':to_email, 'message':message})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject,
        text_content,
        None,
        to_email
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()