import numpy as np

__author__ = 'Chu-Chang Ku'
__all__ = ['flatten_ms', 'summarise_mss']

SelectedKeys = ['IncR', 'MorR', 'PrevUt']


def flatten_ms(ms, ks=None):
    ks = ks if ks is not None else SelectedKeys
    return [dict(row) for _, row in ms[ks].reset_index().iterrows()]


def summarise_mss(mss, ci=0.5):
    ks = mss[0][0].keys()
    ks = [k for k in ks if k != 'Year']
    stats = list()
    for t in range(len(mss[0])):
        stat = {'Year': mss[0][t]['Year']}
        for k in ks:
            vs = np.array([ms[t][k] for ms in mss])
            mlu = np.quantile(vs, [0.5, 0.5 - ci / 2, 0.5 + ci / 2])
            stat[f'{k}_M'], stat[f'{k}_L'], stat[f'{k}_U'] = mlu
        stats.append(stat)
    return stats
