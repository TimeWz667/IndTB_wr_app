import hashlib
import json

__author__ = 'Chu-Chang Ku'
__all__ = ['Database']


class Database:
    def __init__(self):
        self.Runs = dict()

    def check_existence(self, loc, intv) -> bool:
        intv_hash = intv if intv is 'baseline' else self.get_intv_hash(intv)
        return intv_hash in self.Runs

    def get_intv_hash(self, intv):
        return hashlib.sha256(json.dumps(intv.json()).encode()).hexdigest()

    def load_simulation(self, loc, intv: str) -> bool:
        if intv is 'baseline':
            return self.Runs['baseline']
        else:
            intv_hash = self.get_intv_hash(intv)
            return self.Runs[intv_hash]

    def save_simulation(self, sim, loc, intv='baseline'):
        intv = intv if intv is 'baseline' else self.get_intv_hash(intv)
        self.Runs[intv] = sim
