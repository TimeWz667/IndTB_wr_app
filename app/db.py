import json
import hashlib
import os
from os.path import exists


__all__ = ['Database']


class Database:
    def __init__(self, dir_data):
        self.DirData = dir_data
        os.makedirs(self.DirData, exist_ok=True)

    def get_filename(self, loc, intv='baseline'):
        # encoding then hashing
        if intv == 'baseline':
            intv_hash = 'baseline'
        else:
            intv_hash = hashlib.sha256(json.dumps(intv.json()).encode()).hexdigest()
        return f'{self.DirData}/results#{loc}#{intv_hash}.json'

    def check_existence(self, loc, intv='baseline') -> bool:
        return exists(self.get_filename(loc, intv))

    def load_simulation(self, loc, intv='baseline') -> bool:
        file = self.get_filename(loc, intv)
        with open(file, 'r') as f:
            return json.load(f)

    def save_simulation(self, sim, loc, intv='baseline'):
        file = self.get_filename(loc, intv)
        # todo check disk/folder space if needed. When the upper limit reached -> delete oldest file before saving

        with open(file, 'w') as f:
            json.dump(sim, f)
