import yaml
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

with open("datatest.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    browser_name = testdata["browser_name"]

@pytest.fixture(scope="session")
def browser():
    if browser_name == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def send_mail():

    fromaddr = 'eptit@mail.ru'
    toaddr = 'eptit@mail.ru'
    mypass = 'SxCeK97dkxnwxEeadx9H'
    reportname = 'log.txt'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Hello from Python'

    with open(reportname, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename="%s' % basename(reportname)
        msg.attach(part)

    body = 'Это пробное сообщение'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

@pytest.fixture(scope="session")
def auth_token():
    login_url = f"{testdata['address']}/gateway/login"
    username = testdata['username']
    password = testdata['password']
    response = requests.post(login_url, data={"username": username, "password": password})
    return response.json()['token']