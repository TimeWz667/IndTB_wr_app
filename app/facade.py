import json
import pickle as pkl
import numpy as np
from functools import lru_cache
from app.model.dy import Model, Intervention
import numpy.random as rd

__author__ = 'Chu-Chang Ku'
__all__ = ['Simulator']


class Simulator:
    def __init__(self, dir_pars):
        self.DirPars = dir_pars
        self.Meta = []
        self.Models = dict()

        self.initialise_models()

    @lru_cache()
    def list_locations(self) -> list:
        return ['India']
        # return [d['Location'] for d in self.Meta]

    # def load_location_meta(self, loc) -> dict:
    #     for d in self.Meta:
    #         if d['Location'] == loc:
    #             return d
    #     else:
    #         raise KeyError('Location not available')

    def initialise_models(self):
        for loc in self.list_locations():
            m = Model()

            ps = []

            for _ in range(20):
                pars = {
                        'beta': rd.random() * 3 + 2,
                        'eta': 0.5,
                        'gamma': 0.2,
                        'dr': 0.03
                    }

                ps.append((pars, m.get_y0()))

            self.Models[loc] = {'model': m, 'ps_y0': ps}

        # with open(f'{self.DirPars}/{self.DirMeta}.json', 'r') as f:
        #     self.Meta = json.load(f)
        #
        # for loc in self.list_locations():
        #     inp = load_inputs(f'{self.DirPars}/demo/pars_demo_{loc}.json')
        #     self.Models[loc] = Model(inp, mdr=True, year0=1970)

    # @lru_cache
    # def load_pars(self, loc, gp='agg'):
    #     with open(f'{self.DirPars}/{self.DirY0s}/y0s_{loc}.pkl', 'rb') as f:
    #         pars = pkl.load(f)
    #     try:
    #         pars = pars[gp]
    #     except KeyError:
    #         pars = pars['agg']
    #     return pars

    def simulate_baseline(self, loc):
        # with open(f'{self.DirPars}/{self.DirBaseline}/ms_{loc}.json', 'r') as f:
        #     ms = json.load(f)
        m = self.Models[loc]
        m, ps_y0 = m['model'], m['ps_y0']

        ms = list()
        for ps, y0 in ps_y0:
            ms.append(m.simulate_onward(ps, y0=y0))

        return self.formulate_summary(ms)

    def validate_parse_intervention(self, intv):
        return Intervention.parse_obj(intv)

    def simulate_intervention(self, loc, intv):
        m = self.Models[loc]
        m, ps_y0 = m['model'], m['ps_y0']

        ms = list()
        for ps, y0 in ps_y0:
            ms.append(m.simulate_onward(ps, y0=y0, intv=intv))

        return self.formulate_summary(ms)

    @staticmethod
    def formulate_summary(mss):
        summary = list()
        for t in range(len(mss[0])):
            d = {'Year': mss[0][t]['Year']}
            for k in ['IncR', 'MorR']:
                l, m, u = np.quantile([ms[t][k] for ms in mss], [0.25, 0.5, 0.75])
                d[k] = {'M': m, 'L': l, 'U': u}
            summary.append(d)

        # todo modify the function for the input format needed
        return summary


# class ModelAdaptor:
#     def __init__(self, dir_pars):
#         self.DirPars = dir_pars
#         self.Meta = []
#         self.Models = dict()
#
#         self.initialise_models()
#
#     @lru_cache()
#     def list_locations(self) -> list:
#         return [d['Location'] for d in self.Meta]
#
#     def load_location_meta(self, loc) -> dict:
#         for d in self.Meta:
#             if d['Location'] == loc:
#                 return d
#         else:
#             raise KeyError('Location not available')
#
#     def initialise_models(self):
#         with open(f'{self.DirPars}/{self.DirMeta}.json', 'r') as f:
#             self.Meta = json.load(f)
#
#         for loc in self.list_locations():
#             inp = load_inputs(f'{self.DirPars}/demo/pars_demo_{loc}.json')
#             self.Models[loc] = Model(inp, mdr=True, year0=1970)
#
#     @lru_cache
#     def load_pars(self, loc, gp='agg'):
#         with open(f'{self.DirPars}/{self.DirY0s}/y0s_{loc}.pkl', 'rb') as f:
#             pars = pkl.load(f)
#         try:
#             pars = pars[gp]
#         except KeyError:
#             pars = pars['agg']
#         return pars
#
#     def simulate_baseline(self, loc):
#         with open(f'{self.DirPars}/{self.DirBaseline}/ms_{loc}.json', 'r') as f:
#             ms = json.load(f)
#         return ms
#         # m = self.Models[loc]
#         # ps = self.load_pars(loc)
#         #
#         # if self.Parallel:
#         #     with Parallel(n_jobs=self.N_Cores, verbose=8) as parallel:
#         #         mss = parallel(delayed(run)(m, y0, intv=None) for y0 in ps)
#         # else:
#         #     mss = [run(m, y0, intv=None) for y0 in ps]
#         # return self.formulate_summary(mss)
#
#     def validate_parse_intervention(self, intv):
#         return Intervention.parse_obj(intv)
#
#     def simulate_intervention(self, loc, intv):
#         m = self.Models[loc]
#
#         gp = 'agg' if intv.PrHi == 'Not restricted' else intv.PrHi
#         ps = self.load_pars(loc, gp=gp)
#
#         if self.Parallel:
#             with Parallel(n_jobs=self.N_Cores, verbose=8) as parallel:
#                 mss = parallel(delayed(run)(m, y0, intv) for y0 in ps)
#         else:
#             mss = [run(m, y0, intv) for y0 in ps]
#         return self.formulate_summary(mss)
#
#     @staticmethod
#     def formulate_summary(mss):
#         summary = list()
#         for t in range(len(mss[0])):
#             d = {'Time': mss[0][t]['Time']}
#             for k in ['IncR', 'MorR', 'Prev', 'IncR_remote']:
#                 l, m, u = np.quantile([ms[t][k] for ms in mss], [0.25, 0.5, 0.75])
#                 d[k] = {'M': m, 'L': l, 'U': u}
#             summary.append(d)
#
#         # todo modify the function for the input format needed
#         return summary


if __name__ == '__main__':
    import time
    models = Simulator('../db')

    print(models.list_locations())
    t0 = time.time()
    loc = 'India'

    mss0 = models.simulate_baseline(loc)
    print(mss0)
    t1 = time.time()
    print((t1 - t0))

    for d in mss0:
        print(d['Year'], d['IncR'])

