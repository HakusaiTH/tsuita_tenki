import tweepy
import requests
from bs4 import BeautifulSoup
import openai
from googletrans import Translator
import datetime, pytz
import schedule
import time

#genarate_text
openai.api_key = "openai_key"

def genarate_text(promt) :
    model = "text-davinci-002"
    temperature = 0.5
    max_tokens = 100

    response = openai.Completion.create(
        engine=model,
        prompt=f'Weather reports and pm 2.5 based on this information [{promt}]',
        temperature=temperature,
        max_tokens=max_tokens
    )
    return translate(response.choices[0].text,'th')

#tran
def translate(text,la) :
    translator = Translator()
    translation = translator.translate(text, dest=la).text
    return translation

consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

def creat_post(text) :
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )

    response = client.create_tweet(
        text=text
    )
    print(f"https://twitter.com/user/status/{response.data['id']}")


def main() :
    print("start main")
    # Scrape PM2.5 value
    url_pm = 'https://aqicn.org/city/beijing/'
    response_pm = requests.get(url_pm)

    soup_pm = BeautifulSoup(response_pm.content, 'html.parser')
    aqi_element = soup_pm.find('div', {'class': 'aqivalue'})

    if aqi_element:
        pm_value = aqi_element.text.strip()
        info_element = soup_pm.find('div', {'id': 'aqiwgtinfo'})

        if info_element:
            info_text = info_element.text.strip()
        else:
            print("Information element not found.")
    else:
        print("AQI element not found.")

    # Scrape temperature value
    url_temp = 'http://www.metalarm.tmd.go.th/monitor/media'
    response_temp = requests.get(url_temp)

    soup_temp = BeautifulSoup(response_temp.content, 'html.parser')

    div = soup_temp.find('div', {'class': 'view_media_desc'})

    temp_response = translate(div.text, 'en')

    #time   https://gist.github.com/korakot/ccd8970c5eaa3f82f8a7cc4f6c36f9ac
    tz = pytz.timezone('Asia/Bangkok')
    def now():
        now1 = datetime.datetime.now(tz)
        month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now1.month]
        thai_year = now1.year + 543
        time_str = now1.strftime('%H:%M:%S')
        return "%d %s %d %s"%(now1.day, month_name, thai_year, time_str) # 30 ตุลาคม 2560 20:45:30

    #the_result
    tran_response = genarate_text(f"PM2.5 value: {pm_value} Temperature value: {temp_response}")
    creat_post(f"{now()} {tran_response}")

schedule.every().day.at('07:40').do(main)
while True:
   schedule.run_pending()
   time.sleep(1)