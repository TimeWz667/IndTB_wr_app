from wr import *
import pickle as pkl

__author__ = 'Chu-Chang Ku'
__all__ = ['Simulator']


class Simulator:
    def __init__(self, locator, models):
        self.Models = dict(models)
        self.Locator = locator

    def list_locations(self):
        return list(self.Locator.Locations.keys())

    def list_schema_intv(self):
        return {'ACF': {'Scale': 10}}

    def run_baseline(self, loc):
        return self.Models[loc]['Baseline']

    def run_intv(self, loc, intv: dict):
        if len(intv) == 0:
            return self.run_baseline(loc)

        intv = Intervention.parse_obj(intv)
        m = self.Models[loc]
        model = m['Model']
        pss = m['Parameters']
        mss = list()
        for y0_ps in pss:
            _, ms, _ = model.simulate_onward(y0=y0_ps['y0'], pars=y0_ps['pars'], intv=intv)
            mss.append(flatten_ms(ms))
        return summarise_mss(mss)

    @staticmethod
    def load(folder_db, n_pick=10):
        with open(f'{folder_db}/locators.pkl', 'rb') as f:
            locator = pkl.load(f)

        locs = locator.Locations

        models = dict()
        for loc in locs:
            name, src = locator.find(loc, f'{folder_db}/y0s' + '/arch_{}.pkl')
            with open(src, 'rb') as f:
                src = pkl.load(f)
            model = ModelRisk(src['inputs'])
            atoms = src['atoms'][:n_pick]
            mss = [atom['ms'] for atom in atoms]
            mss = summarise_mss(mss, 0.5)

            models[loc] = {
                'Name': name,
                'Model': model,
                'Parameters': atoms,
                'Baseline': mss
            }
        return Simulator(locator, models)


if __name__ == '__main__':
    sim = Simulator.load('../db')
    print(sim.list_locations())

    print('Baseline')
    for m in sim.run_baseline('India'):
        print(m['Year'], m['IncR_M'])

    intv = {
        'TPT': {'Scale': 5}
    }

    print('Intervention')
    for m in sim.run_intv('India', intv):
        print(m['Year'], m['IncR_M'])
