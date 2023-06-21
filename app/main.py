from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
import numpy.random as rd
from app.repo import Database
from app.model.dy import Intervention
from app.facade import Simulator

simulator = Simulator("")
db = Database()
OverrideSimulation = True

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/locs")
def list_locations():
    return simulator.list_locations()


# def get_metadata(location):
#     return mod.load_location_meta(location)

@app.get("/{location}/")
def run_baseline(location: str = "India", time_end: int = 2030):
    if db.check_existence(location, 'baseline') and not OverrideSimulation:
        return db.load_simulation(location, 'baseline')
    sim = simulator.simulate_baseline(location)
    db.save_simulation(sim, location, 'baseline')
    sim = [d for d in sim if d['Year'] <= time_end]
    return sim


@app.put("/{location}/")
def run_intervention(location: str = "India", time_end: int = 2030, intv: dict = None):
    intv = simulator.validate_parse_intervention(intv)
    if db.check_existence(location, intv) and not OverrideSimulation:
        return db.load_simulation(location, intv)
    sim = simulator.simulate_intervention(location, intv)
    db.save_simulation(sim, location, intv)
    sim = [d for d in sim if d['Year'] <= time_end]
    return sim

@app.get("/")
def read_root():
    return {"Hello": "World 2d", "k": rd.random()}
