from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

while True:
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.investing.com/equities/trending-stocks')

        res = driver.execute_script("return document.documentElement.outerHTML")

        driver.quit()

        soup = BeautifulSoup(res,'lxml')
        soup = soup.find('div',attrs = {'class':'trendingStocks'})
        soup = soup.find('div',attrs = {'class' : 'chartContainer'})
        soup = soup.find('div',attrs = {'id':'trendingByPopularityChart','class':'dirLtr trendingStocksChart'})
        soup = soup.find('div',attrs = {'id':'highcharts-0','class':'highcharts-container'})
        soup = soup.find('svg',attrs = {'style':'font-family:"Lucida Grande", "Lucida Sans Unicode", Arial, Helvetica, sans-serif;font-size:12px;'})
        soup = soup.find('g',attrs = {'class':'highcharts-axis-labels highcharts-xaxis-labels'})

        company = [[rows.text] for rows in soup.findAll('text')]
        soup = BeautifulSoup(res,'lxml')
        soup = soup.find('div',attrs = {'class':'trendingStocks'})
        soup = soup.find('div',attrs = {'class' : 'chartContainer'})
        soup = soup.find('div',attrs = {'id':'trendingByPopularityChart','class':'dirLtr trendingStocksChart'})
        soup = soup.find('div',attrs = {'id':'highcharts-0','class':'highcharts-container'})
        soup = soup.find('svg',attrs = {'style':'font-family:"Lucida Grande", "Lucida Sans Unicode", Arial, Helvetica, sans-serif;font-size:12px;'})
        soup = soup.find('g',attrs = {'class':'highcharts-series-group'})
        soup = soup.find('g',attrs = {'class': 'highcharts-series highcharts-tracker'})

        for index, rows in enumerate(soup.findAll('rect')):
            company[index].append(int(rows['height']))
        print(company)
    except:
        print('Let me sleep for some time')
        time.sleep(random.uniform(0.2,5))
