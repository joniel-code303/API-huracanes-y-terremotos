import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'tu_email@gmail.com'
EMAIL_PASSWORD = 'tu_contraseña'

def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS  # Cambia esto a otro destinatario

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    print("Notificación enviada por correo electrónico.")
