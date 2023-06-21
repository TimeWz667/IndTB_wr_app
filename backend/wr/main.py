__all__ = ['list_locations',
           'get_schema_intv',
           'get_metadata',
           'run_baseline', 'run_intervention']


def list_locations():
    return ['India', 'Delhi']


def get_schema_intv():
    return []


def get_metadata(location):
    return {'pdx': 0.5}


def run_baseline(location: str, time_end: int):
    return [
        {'Year': 2023, 'IncR': 0.003, 'MorR': 0.0003},
        {'Year': 2025, 'IncR': 0.0025, 'MorR': 0.00025},
    ]


def run_intervention(location: str, time_end: int, intv: dict):
    return [
        {'Year': 2023, 'IncR': 0.003, 'MorR': 0.0003},
        {'Year': 2025, 'IncR': 0.002, 'MorR': 0.0002},
    ]

