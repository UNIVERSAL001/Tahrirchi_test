#import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime



#input URL
source_urls =[
"https://kun.uz/uz/news/2022/11/30/parda-ortidagi-xususiylashtirish-yirik-aktivlar-qanday-qilib-ofshor-kompaniyalarga-otib-ketmoqda",
"https://kun.uz/uz/news/2022/12/01/samarqandda-pogonini-ozi-yulib-tashlab-bunda-ayolni-ayblagan-iib-xodimi-jazosiz-qolgani-malum-boldi",
"https://kun.uz/uz/news/2022/12/01/kocha-qonunlari-boyicha-undiruv-rossiyada-ish-haqi-berilmay-qiyin-vaziyatda-qolgan-ozbek-hikoyasi"
]

def start(url:str)->tuple: #list and access_datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    wordlist = []
    source_code = requests.get(url).text
   
    soup = BeautifulSoup(source_code, 'html.parser')

    for each_text in soup.findAll('p'):
    
        content = each_text.text
        words = content.lower().split()
 
        for each_word in words:
            wordlist.append(each_word)

        cleaned_words = clean_wordlist(wordlist)
    return cleaned_words,current_time

 

def clean_wordlist(wordlist:list)->list:

    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
 
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
 
        if len(word) > 0:
            clean_list.append(word)
    return clean_list



#save to file a words
access_datetimes = []

for i in source_urls:
    data,time = start(i)
    access_datetimes.append(time)
    with open('words.csv', mode='a') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(data)

with open('times.csv', 'a') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(access_datetimes)



# print("Current Time =", access_datetimes)

