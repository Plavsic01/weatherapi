from bs4 import BeautifulSoup
import requests
import json

def scrape_data():
    headers = {"Accept-Language": "en-US,en;q=0.5"}
    req = requests.get("https://www.timeanddate.com/weather/?sort=1&low=4",headers=headers)
    req = req.text
    soup = BeautifulSoup(req,"html.parser")
    data = []
    table = soup.find("table")

    for row in table.find_all('tr')[1:]:

        name = row.find_all('td')[0].text
        day_time = row.find_all('td')[1].text
        weather = row.find_all('td')[2].find("img").get("title")
        temperature = row.find_all('td')[3].text

        dict = {
            "name":name,
            "day and time":day_time,
            "weather":weather,
            "temperature":temperature
        }

        data.append(dict)

    return data


def get_data(name):
    data_found = []
    json_data = scrape_data()
    for i in json_data:
        if name in i["name"]:
            data_found.append(i)

    return data_found


if __name__ == "__main__":
    data = scrape_data()
    specific_data = get_data("Serbia")











    
    
    

