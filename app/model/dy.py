from scipy.integrate import solve_ivp
import numpy as np
from pydantic import BaseModel


__author__ = 'Chu-Chang Ku'
__all__ = ['Intervention', 'Model']


class I:
    Sus = 0
    Exp = 1
    Inf = 2
    Rec = 3


class Intervention(BaseModel):
    prot: float = 0
    t_intv: int = 6


class Model:
    def get_y0(self):
        y0 = np.zeros(4)
        y0[I.Sus] = 990
        y0[I.Inf] = 10
        return y0

    def __call__(self, t, y, pars, intv):
        dy = np.zeros_like(y)
        foi = y[I.Inf] / y.sum() * pars['beta']

        if t >= intv.t_intv:
            foi *= (1 - intv.prot)

        s, e, i, r = y
        dy[I.Sus] = - foi * s
        dy[I.Exp] = + foi * s - pars['eta'] * e
        dy[I.Inf] = + pars['eta'] * e - pars['gamma'] * i
        dy[I.Rec] = pars['gamma'] * i
        dy -= y * pars['dr']
        dy[I.Sus] -= dy.sum()

        return dy

    def measure(self, t, y, pars, intv):
        return {
            'Year': t,
            'N': y.sum(),
            'Prev': y[I.Inf] / y.sum(),
            'IncR': pars['eta'] * y[I.Exp] / y.sum(),
            'MorR': pars['dr'] * y[I.Inf] / y.sum()
        }

    def simulate_onward(self, pars, y0=None, intv=None):
        if y0 is None:
            y0 = self.get_y0()

        if intv is None:
            intv = Intervention()
        ys = solve_ivp(self, [0, 10], y0=y0, args=(pars, intv), dense_output=True)
        mss = [self.measure(t, ys.sol(t), pars, intv) for t in np.linspace(0, 10, 11)]
        return mss


if __name__ == '__main__':
    model = Model()

    p0 = {
        'beta': 3,
        'eta': 0.5,
        'gamma': 0.2,
        'dr': 0.03
    }

    i0 = Intervention(prot=0.1)

    ms0 = model.simulate_onward(p0, intv=i0)
    print(ms0[-1])

    i1 = Intervention(prot=0.8)

    ms1 = model.simulate_onward(p0, intv=i1)
    print(ms1[-1])

