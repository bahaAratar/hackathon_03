from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_confirmation_email(order):
    subject = 'Order confirmation'
    message = render_to_string('order_confirmation.html', {'order': order})
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.email]
    send_mail(subject, message, from_email, recipient_list, html_message=message)