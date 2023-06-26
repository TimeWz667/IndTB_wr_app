import pandas as pd
import os

__author__ = 'Chu-Chang Ku'
__all__ = ['parse_locators']


class Locator:
    def __init__(self, locs):
        self.Locations = dict(locs)

    def find(self, loc, pattern):
        assert loc in self.Locations
        loc = self.Locations[loc]

        for k in loc['Chain']:
            path = pattern.format(k)
            if os.path.exists(path):
                break
        else:
            raise KeyError('Invalid location')
        return loc['Name'], path

    def get_name(self, loc):
        assert loc in self.Locations
        return self.Locations[loc]['Name']

def parse_locators(filepath):
    src = pd.read_csv(filepath)
    src = src.set_index('Location')
    print(src)
    src = {i: dict(row) for i, row in src.iterrows()}
    for row in src.values():
        row['Chain'] = row['Chain'].split(':')
    return Locator(src)


if __name__ == '__main__':
    loc = parse_locators('../db_src/locations.csv')

    print(loc.find('India', '../db/y0s/arch_{:s}.pkl'))
    print(loc.find('Delhi', '../db/y0s/arch_{:s}.pkl'))

    try:
        print(loc.find('London', '../db/y0s/arch_{:s}.pkl'))
    except AssertionError:
        print('London is not in India')
