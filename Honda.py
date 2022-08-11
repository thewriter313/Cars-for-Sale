from Cars import Car
from bs4 import BeautifulSoup
import requests
import numpy as np

class Honda(Car):

    def __init__(self, make):
        super().__init__(make)

    def read(self):

        dataframe = np.array(['Make', 'Model', 'Year', 'Mileage', 'Price', 'Transmission', 'Location', 'Link'])            
        self.make = 'Honda'

        maxpage = 8
        page = 0

        while page in range(0, maxpage):
            print('Getting list of cars from '+ self.make + '\'s website page ' + str(page + 1))
            url =  'https://cuv.honda.ca/inventory.html?filterid=a2b1c1d1Bp1q' + str(page) + '-10v0-Ax3SKXJ4-0-0'
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')

            cars = soup.select("div[class = 'divSpan divSpan12 carBoxInner']")
            page += 1
            
            for car in cars:

                row = []
                year_model = car.find('span', class_ = 'divModelYear elIsGreyable').text
                model = year_model.split(' ', 1)[1]
                year = year_model.split(' ', 1)[0]
                mileage = car.find('span', class_ = 's-km')
                if mileage == None:
                    mileage = '-'
                else:
                    mileage = mileage.text
                price = car.find('span', class_ = 'p-base').text
                price = '$' + price.split('$')[0]
                transmission = car.find('span', class_ = 's-desc').text
                if 'Man.' in transmission:
                    transmission = 'Manual'
                elif 'Auto.' in transmission:
                    transmission = 'Automatic'
                else:
                    transmission = '-'
                location = car.find('span' , class_ = 'divCity elIsGreyable').text
                location = location.split(' ', 1)[1]
                link = car.find('a', class_ = 'divSpan carTitle')
                row = np.append(row, [self.make, model, int(year), mileage, price, transmission, location, 'https://cuv.honda.ca' + link['href']])
                dataframe = np.vstack((dataframe, row))
        return dataframe