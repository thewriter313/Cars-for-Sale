from Cars import Car
from bs4 import BeautifulSoup
import requests
import numpy as np

class Mazda(Car):

    def __init__(self, make):
        super().__init__(make)
    
    def read(self):

        dataframe = np.array(['Make', 'Model', 'Year', 'Mileage', 'Price', 'Transmission', 'Location', 'Link'])            
        self.make = 'Mazda'

        maxpage = 100
        page = 1
        while page in range(1, maxpage):
            print('Getting list of cars from '+ self.make + '\'s website page ' + str(page))

            url =  'https://cpo.mazda.ca/en/vehicle-listings/?p=M5J&lat=43.6408&long=-79.3818&d=100&v%5B%5D=M3S&v%5B%5D=MZ6&v%5B%5D=CX3&v%5B%5D=CX5&v%5B%5D=CX9&v%5B%5D=MX5&page=' + str(page)
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')

            cars = soup.select("div[class = 'card-block']")
            pages = soup.select("ul[class = 'pagination']")

            page += 1
            
            for p in pages:
                maxpage = int(p.find_all('a')[-2].get_text()) + 1
            
            for car in cars:
                row = []
                year_model = car.find('div', class_ = 'listing-name').text
                model = year_model.split('  ', 1)[1]
                year = year_model.split('  ', 1)[0]
                mileage = car.find('div', class_ = 'listing-field listing-mileage').text
                price = car.find('h4', class_ = 'listing-price').text
                transmission = car.find_all('div', class_ = 'listing-field listing-seating')[1].get_text()
                location = '-'
                link = car.find()
                row = np.append(row, [self.make, model, int(year), mileage, price, transmission, location, 'https://cpo.mazda.ca' + link['href']])
                dataframe = np.vstack((dataframe, row))
        return dataframe