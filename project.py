#webscrapping
#requests header send request to url access
import requests
#pandas to efficient way to use datastructure or dataframe used convert any type data file
import pandas as pd
from bs4 import BeautifulSoup
#split data from certain webpage
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.Xgg7H0czbIU')
soup = BeautifulSoup(page.content,'html.parser')
target = soup.find(id ="seven-day-forecast-body")
items = target.find_all(class_="tombstone-container")
for i in (0,5):
    print(items[i].find(class_="period-name").get_text())
    print(items[i].find(class_="short-desc").get_text())
    print(items[i].find(class_="temp").get_text())

period_name = [i.find(class_ ='period-name').get_text() for i in items]
print(period_name)
short_desc = [i.find(class_ ='short-desc').get_text() for i in items]
print(short_desc)
temperature = [i.find(class_ = 'temp').get_text() for i in items]
print(temperature)
page_content = [period_name,short_desc,temperature]
print(page_content)

weather_details = pd.DataFrame(
    {
    'period-name' : period_name,
    'short-desc' : short_desc,
     'temp' : temperature
    }
)
print(weather_details)
weather_details.to_csv('result_1.csv')