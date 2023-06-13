from selenium import webdriver
from bs4 import BeautifulSoup
import csv 
import time

start_url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("C:/Users/ME/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(start_url)

def scrape():
    headers=["name","light_years_from_Earth","planet_mass","stellar_magnitude","discovery_data"]
    planet_data=[]
    for i in range(0,10):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            #print(ul_tag)
            li_tags=ul_tag.find_all("li") 
            templist=[] 
            for index,li_tag in enumerate(li_tags): 
                # print(index) 
                if index == 0: 
                    templist.append(li_tag.find_all("a")[0].contents[0]) 
                else: 
                    try: 
                        templist.append(li_tag.find_all.contents[0]) 
                    except: 
                        templist.append("") 
            planet_data.append(templist) 
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click() 
    with open("scrapper.csv","w",newline="") as f: 
            csvwriter= csv.writer(f) 
            csvwriter.writerow(headers) 
            csvwriter.writerows(planet_data)
scrape()

