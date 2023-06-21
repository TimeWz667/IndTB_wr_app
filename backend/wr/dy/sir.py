from scipy.integrate import solve_ivp
import numpy as np
from pydantic.types import confloat
from pydantic import BaseModel, schema_json_of

__author__ = 'Chu-Chang Ku'
__all__ = ['Model', 'Intervention']


class Model:
    def get_y0(self):
        return np.array([990, 10, 0])

    def __call__(self, t, y, pars, intv=None):
        s, i, r = y
        n = y.sum()
        beta, r_rec, r_die = pars['beta'], pars['r_rec'], pars['r_die']
        if intv is not None and t > 3:
            beta = beta * (1 - intv.SocDist.BetaRed)
        foi = beta * i / n

        dy = np.array([
            r_die * (i + r) - foi * s,
            foi * s - (r_rec + r_die) * i,
            r_rec * i - r_die * r
        ])

        return dy

    def measure(self, t, y, pars, intv):
        s, i, r = y
        n = y.sum()
        beta, r_rec, r_die = pars['beta'], pars['r_rec'], pars['r_die']
        if intv is not None and t > 3:
            beta = beta * (1 - intv.SocDist.BetaRed)
        foi = beta * i / n

        return {
            'Year': t,
            'IncR': foi * s / n,
            'MorR': r_die * i / n
        }

    def simulate(self, pars, intv=None):
        y0 = self.get_y0()
        ys = solve_ivp(self, [0, 10], y0, args=(pars, intv,), dense_output=True)

        ms = [self.measure(t, ys.sol(t), pars, intv,) for t in np.linspace(0, 10, 11)]

        return ms


class SocDist(BaseModel):
    BetaRed: confloat(ge=0, le=0.2) = 0


class Intervention(BaseModel):
    SocDist: SocDist = SocDist()


if __name__ == '__main__':
    p = {
        'beta': 1.5,
        'r_rec': 0.2,
        'r_die': 0.05
    }

    mod = Model()

    ms0 = mod.simulate(p, intv=None)

    intv1 = Intervention.parse_obj({'SocDist': {'BetaRed': 0.05}})
    ms1 = mod.simulate(p, intv=intv1)

    intv2 = Intervention.parse_obj({'SocDist': {'BetaRed': 0.1}})
    ms2 = mod.simulate(p, intv=intv2)

    for m0, m1, m2 in zip(ms0, ms1, ms2):
        print(m0['Year'], m0['IncR'], m1['IncR'], m2['IncR'])
