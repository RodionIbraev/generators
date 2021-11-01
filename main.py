import json


class CountriesIterator:
    def __iter__(self):
        return self

    def __init__(self, file):
        self.links_and_countries = []
        self.counter = 0
        try:
            with open(file, "r") as f:
                f_json = json.load(f)
                for elem in f_json:
                    country = elem['name']['common']
                    link = 'https://en.wikipedia.org/wiki/' + '_'.join(country.split())
                    self.links_and_countries.append(country + ' - ' + link)
            self.limit = len(self.links_and_countries)
        except:
            print('Error. Could not open the file...')

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.links_and_countries[self.counter - 1]
        else:
            raise StopIteration


if __name__ == '__main__':
    countries_iter = CountriesIterator('countries.json')
    with open('links_and_countries.txt', 'w', encoding='utf8') as f:
        for i in countries_iter:
            f.write(i + '\n')
