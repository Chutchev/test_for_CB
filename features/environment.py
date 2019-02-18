from selenium import webdriver
import os
import dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def before_all(context):
    context.browser = webdriver.Chrome(os.path.abspath("chromedriver.exe"))
    context.browser.maximize_window()


def after_all():
    send_email('') #Указать кому необходимо отправлять письмо
    screens_directory = os.path.abspath("Screenshots")
    for image in os.listdir(screens_directory):
        os.remove(os.path.join(screens_directory, image))


def send_email(email_to):
    dotenv.load_dotenv()
    login = os.getenv('login')
    password = os.getenv('password')
    msg = MIMEMultipart()
    msg['Subject'] = 'Результаты теста'
    msg['From'] = login
    msg['To'] = email_to
    text = MIMEText("Результаты теста")
    msg.attach(text)
    screens_directory = os.path.abspath("Screenshots")
    for image in os.listdir(screens_directory):
        part = MIMEApplication(open(os.path.join(screens_directory, image), 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=os.path.join(screens_directory, image))
        msg.attach(part)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(login, password)
    s.sendmail(login, email_to, msg.as_string())
    s.quit()