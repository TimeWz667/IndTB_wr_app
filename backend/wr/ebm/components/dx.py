from wr.ebm.components.proc import Process
import numpy as np

__author__ = 'Chu-Chang Ku'
__all__ = ['Dx']


class Dx(Process):
    def __init__(self, keys):
        Process.__init__(self, 'dx', keys)

    def calculate_calc(self, t, y, pars, calc: dict, **kwargs):
        I = self.Keys

        r_csi, r_recsi = pars['r_csi'], pars['r_recsi']

        k = np.exp(pars['rt_cs'] * max(t - 2019, pars['t0_decline'] - 2019))
        r_csi *= k
        r_recsi *= k

        p_ent, p_txi = pars['p_ent'], pars['p_txi']

        p_pdx0, p_pdx1 = pars['p_dx0'], pars['p_dx1']

        if 'intv' in kwargs and kwargs['intv'] is not None:
            r_csi, r_recsi = kwargs['intv'].modify_cs(t, r_csi, r_recsi)
            p_ent = kwargs['intv'].modify_access(t, p_ent)
            p_pdx0, p_pdx1 = kwargs['intv'].modify_dx(t, p_pdx0, p_pdx1)

        pdx0 = p_ent * p_pdx0 * p_txi
        pdx1 = p_ent * p_pdx1 * p_txi

        calc['tp0'] = tp0 = r_csi * pdx0.reshape((-1, 1)) * y[I.Sym].reshape((1, -1))
        calc['fn0'] = r_csi * (p_ent - pdx0).reshape((-1, 1)) * y[I.Sym].reshape((1, -1))
        calc['tp1'] = tp1 = r_recsi * pdx1.reshape((-1, 1)) * y[I.ExCS].reshape((1, -1))

        tp, alo = (tp0 + tp1).reshape((3, 1, -1)), pars['tx_alo']

        calc['txi'] = (tp * alo.reshape((3, -1, 1))).sum(0)

        ppv = pars['ppv'].reshape((-1, 1))
        calc['fp'] = (tp0 + tp1) * (1 - ppv) / ppv

        return calc

    def compose_dya(self, ya, calc: dict):
        I = self.Keys

        y, aux = ya
        dy, da = np.zeros_like(y), np.zeros_like(aux)

        tp0, fn0, tp1 = calc['tp0'], calc['fn0'], calc['tp1']

        txi = calc['txi']

        dy[I.Sym] += - tp0.sum(0) - fn0.sum(0)
        dy[I.ExCS] += fn0.sum(0) - tp1.sum(0)
        dy[I.TxPub] += txi[0]
        dy[I.TxPri] += txi[1]

        fp = calc['fp']

        da[I.A_NotiPub] += (tp0[0] + tp1[0] + fp[0]).sum()
        da[I.A_NotiPri] += (tp0[1] + tp1[1] + fp[1]).sum()

        return dy, da

    def measure(self, mea, t, y, pars, calc, **kwargs):
        n = mea['N']

        mea.update({
            'Tp_pub': calc['tp0'][0] + calc['tp1'][0],
            'Tp_eng': calc['tp0'][1] + calc['tp1'][1],
            'Tp_pri': calc['tp0'][2] + calc['tp1'][2],
            'Fp_pub': calc['fp'][0],
            'Fp_eng': calc['fp'][1],
            'Fp_pri': calc['fp'][2]
        })
        mea['CNR_Pub'] = (mea['Tp_pub'] + mea['Fp_pub']) / n
        mea['CNR_Pri'] = (mea['Tp_eng'] + mea['Fp_eng']) / n
        mea['CNR'] = mea['CNR_Pub'] + mea['CNR_Pri']
