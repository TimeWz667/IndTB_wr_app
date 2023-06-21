from wr.dy.sir import Model, Intervention

__all__ = ['list_locations',
           'get_schema_intv',
           'get_metadata',
           'run_baseline', 'run_intervention']


mod = Model()
p0 = {
        'beta': 1.5,
        'r_rec': 0.2,
        'r_die': 0.05
    }


def list_locations():
    return ['India', 'Delhi']


def get_schema_intv():
    return [
      {
        'Name': "SocDist",
        'Desc': "Social distancing",
        'Clicked': False,
        'Pars': [
          {
            'name': "BetaRed", 'label': "Reduction in transmission", 'value': 0, 'min': 0, 'max': 0.2
          }
        ]
      }
    ]



def get_metadata(location):
    return {'pdx': 0.5}


def run_baseline(location: str, time_end: int):
    return mod.simulate(p0)


def run_intervention(location: str, time_end: int, intv: dict):
    return mod.simulate(p0, intv=Intervention.parse_obj(intv))
