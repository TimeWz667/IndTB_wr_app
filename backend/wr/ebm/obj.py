from sims_pars import bayes_net_from_script
from sims_pars.fit.targets import read_targets
from sims_pars.fit.base import DataModel, Particle
from wr.inputs import load_inputs
from wr.ebm.dy import ModelBaseline
from wr.ebm.dy_risk import ModelRisk
import pandas as pd
import numpy as np

__all__ = ['load_obj_baseline', 'load_obj_risk']


class Obj(DataModel):
    def __init__(self, model, file_prior, file_target, exo=None):
        with open(file_prior, 'r') as f:
            scr = f.read()
        bn = bayes_net_from_script(scr)

        d_ts = pd.read_csv(file_target)
        dat = self.read_data(d_ts)

        DataModel.__init__(self, dat, bn, exo=exo)

        self.Model = model
        self.Cas = self.Model.Inputs.Cascade

    @staticmethod
    def read_data(d_ts):
        d_ts = d_ts.rename(columns={'M': 'm', 'L': 'l', 'U': 'u'})

        dat = dict()

        ds = d_ts[d_ts.Index == 'Inc']
        ds = ds[ds.Year >= 2017]
        ds = ds[ds.Year <= 2019]
        dat.update({f"IncR_All_{row['Year']}": dict(row) for _, row in ds.iterrows()})

        dat['PrevUt_All_2019'] = dict(d_ts[d_ts.Index == 'PrevUt'].iloc[0, :])
        dat['PrA_All_2019'] = dict(d_ts[d_ts.Index == 'PrAsym'].iloc[0, :])
        dat['PrS_All_2019'] = dict(d_ts[d_ts.Index == 'PrSym'].iloc[0, :])
        dat['PrC_All_2019'] = dict(d_ts[d_ts.Index == 'PrExCS'].iloc[0, :])

        dat = read_targets(dat)
        for d in dat.values():
            try:
                d.Range = np.abs(d.Range)
            except AttributeError:
                pass
        return dat

    @staticmethod
    def map_sim_data(ms):
        ext = dict()

        for t in range(2017, 2020):
            ext[f'IncR_All_{t:d}'] = ms.IncR[t]
            # ext[f'MorR_All_{t:d}'] = ms.MorR[t]
            # ext[f'CNR_All_{t:d}'] = ms.CNR[t]
        ext['PrevUt_All_2019'] = ms.PrevUt[2019]
        ext['PrA_All_2019'] = ms.PrA[2019]
        ext['PrS_All_2019'] = ms.PrS[2019]
        ext['PrC_All_2019'] = ms.PrC[2019]

        return ext

    def simulate(self, pars) -> Particle:
        p = self.Cas.prepare_pars(exo=pars)
        _, ms, _ = self.Model.simulate_to_fit(p, t_eval=np.linspace(2014, 2020, 7))
        ext = self.map_sim_data(ms)
        return Particle(pars, ext)


def load_obj_baseline(folder_input, file_prior, file_targets, has_mig=False, year0=2000, exo=None):
    inp = load_inputs(folder_input)
    inp.Demography.HasMigration = has_mig
    inp.Demography.set_year0(year0)
    model = ModelBaseline(inp)
    return Obj(model, file_prior, file_targets, exo=exo)


class ObjRisk(Obj):
    @staticmethod
    def read_data(d_ts):
        d_ts = d_ts.rename(columns={'M': 'm', 'L': 'l', 'U': 'u'})

        dat = dict()

        ds = d_ts[d_ts.Index == 'CNR']
        ds = ds[ds.Year >= 2015]
        ds = ds[ds.Year <= 2019]
        dat.update({f"CNR_All_{row['Year']}": dict(row) for _, row in ds.iterrows()})

        ds = d_ts[d_ts.Index == 'PrevUt']
        ds = ds[ds.Year >= 2015]
        ds = ds[ds.Year <= 2019]
        dat.update({f"PrevUt_{row['Tag']}_{row['Year']}": dict(row) for _, row in ds.iterrows()})

        # dat['PrevUt_All_2019'] = dict(d_ts[d_ts.Index == 'PrevUt'].iloc[0, :])
        # dat['PrA_All_2019'] = dict(d_ts[d_ts.Index == 'PrAsym'].iloc[0, :])
        # dat['PrS_All_2019'] = dict(d_ts[d_ts.Index == 'PrSym'].iloc[0, :])
        # dat['PrC_All_2019'] = dict(d_ts[d_ts.Index == 'PrExCS'].iloc[0, :])

        dat = read_targets(dat)
        for d in dat.values():
            try:
                d.Range = np.abs(d.Range)
            except AttributeError:
                pass
        return dat

    @staticmethod
    def map_sim_data(ms):
        ext = dict()

        for t in range(2015, 2020):
            ext[f'CNR_All_{t:d}'] = ms.NotiR[t]
            ext[f'PrevUt_All_{t:d}'] = ms.PrevUt[t]
        ext['PrevUt_P10%_2019'] = ms.PrevUt_T3[2019]
        ext['PrevUt_P20%_2019'] = ms.PrevUt_T2[2019]
        ext['PrevUt_P30%_2019'] = ms.PrevUt_T1[2019]
        ext['PrevUt_P100%_2019'] = ms.PrevUt_T0[2019]

        return ext


def load_obj_risk(folder_input, file_prior, file_targets, has_mig=False, year0=2000, exo=None):
    inp = load_inputs(folder_input)
    inp.Demography.HasMigration = has_mig
    inp.Demography.set_year0(year0)
    model = ModelRisk(inp)
    return ObjRisk(model, file_prior, file_targets, exo=exo)
