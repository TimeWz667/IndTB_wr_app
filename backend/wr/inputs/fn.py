import json
from collections import namedtuple
from wr.inputs.cascade import *
from wr.inputs.demography import *

__author__ = 'Chu-Chang Ku'
__all__ = ['load_inputs']


Inputs = namedtuple("Inputs", ('Demography', 'Cascade'))


def load_inputs(root):
    with open(f'{root}/pars_pop.json', 'r') as f:
        demo = Demography(json.load(f))
    cr = CasRepo.load(f'{root}/pars_tx.json')

    return Inputs(demo, cr)
