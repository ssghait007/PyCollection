import requests
from bs4 import BeautifulSoup as bs
import smtplib
import time

from secrets import email, passcode


URL = 'https://www.amazon.in/American-Tourister-FS0-11-001/dp/B07S13P8BW/ref=sr_1_6?crid=2G4LXGHRTY7BG&keywords=american+tourister+backpacks&qid=1564333909&s=gateway&sprefix=american+tourister+ba%2Caps%2C307&sr=8-6'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = bs(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()

    price = soup.find(id="priceblock_ourprice").get_text(
    ).strip().strip('₹').strip().replace(',', '')
    price = float(price)
    print(price)
    if(price < 1000.0):
        print('sending email.....')
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, passcode)
    sub = 'price is affordable now'
    body = 'check the amazon link https://www.amazon.in/American-Tourister-FS0-11-001/dp/B07S13P8BW/ref=sr_1_6?crid=2G4LXGHRTY7BG&keywords=american+tourister+backpacks&qid=1564333909&s=gateway&sprefix=american+tourister+ba%2Caps%2C307&sr=8-6'
    msg = 'Subject:{} \n\n{}'.format(sub, body)
    server.sendmail(
        email,
        email,
        msg
    )
    print('Email sent...')
    server.quit()


while(True):
    check_price()
    time.sleep(3600*12)
