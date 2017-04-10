import smtplib
import email.utils
from email.mime.text import MIMEText

from weather import get_avg_temp, get_curr_temp, get_curr_weather
from db_helper import get_users
from klaviyo_app import cities


WARM_WEATHER = "It's nice out! Enjoy a discount on us."
COOL_WEATHER = "Not so nice out? That's okay, enjoy a discount on us."
AVG_WEATHER = "Enjoy a discount on us."


def send_email(recipient, subject, body):
    """
    :param recipient: recipient of the email
    :param subject: subject of the email
    :param body: body of the email
    """
    msg = MIMEText(body)
    msg['To'] = email.utils.formataddr(('Recipient', recipient))
    msg['From'] = email.utils.formataddr(('Admin', 'admin@weather.com'))
    msg['Subject'] = subject

    server = smtplib.SMTP('127.0.0.1', 1025)
    server.set_debuglevel(True)
    try:
        server.sendmail('admin@weather.com', [recipient], msg.as_string())
    finally:
        server.quit()


def get_text():
    """
    Get the text to be sent in the email
    """
    subscribers = get_users()
    for user_email, city in subscribers.iteritems():
        loc = [c[0] for c in cities.cities if c[1] == city]
        avg_temp = get_avg_temp(loc[0])
        curr_temp = get_curr_temp(loc[0])
        weather_text = get_curr_weather(loc[0])
        if (curr_temp - avg_temp > 5):
            send_email(user_email, WARM_WEATHER, weather_text)
        elif (avg_temp - curr_temp > 5):
            send_email(user_email, COOL_WEATHER, weather_text)
        else:
            send_email(user_email, AVG_WEATHER, weather_text)



