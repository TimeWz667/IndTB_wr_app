from scipy.integrate import solve_ivp
import numpy as np
from pydantic import BaseModel
from pydantic.types import confloat

__author__ = 'Chu-Chang Ku'
__all__ = ['Intervention', 'Model']


class I:
    Sus = 0
    Exp = 1
    Inf = 2
    Rec = 3


class BC(BaseModel):
    prot: confloat(le=1, ge=0) = 0


class Intervention(BaseModel):
    BC: BC = BC()
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
            foi *= (1 - intv.BC.prot)

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

    i0 = None

    ms0 = model.simulate_onward(p0, intv=i0)
    print(ms0[-1])

    i1 = Intervention.parse_obj({
        'BC': {'prot': 0.8}
    })

    ms1 = model.simulate_onward(p0, intv=i1)
    print(ms1[-1])

