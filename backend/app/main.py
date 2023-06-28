from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.simulators import Simulator

simulator = Simulator.load('db')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/locs')
def list_locations():
    return simulator.list_locations()


@app.get('/intv')
def list_intv():
    return simulator.get_schema_intv()


@app.get('/run/{location}/')
def run_baseline(location: str = "India", time_end: int = 2030):
    sim = simulator.run_baseline(location)
    sim = [s for s in sim if s['Year'] <= time_end]
    return sim


@app.put('/run/{location}/')
def run_intervention(location: str = "India", time_end: int = 2030, intv: dict = None):
    sim = simulator.run_intv(location, intv)
    sim = [s for s in sim if s['Year'] <= time_end]
    return sim


@app.get('/')
def top():
    return 'Hello WarRoom'
