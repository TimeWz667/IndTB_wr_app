from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import wr.main as wr


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/locs')
def list_locations():
    return wr.list_locations()


@app.get('/intv')
def list_intv():
    return wr.get_schema_intv()


@app.get('/run/{location}/')
def run_baseline(location: str = "India", time_end: int = 2030):
    return wr.run_baseline(location, time_end)


@app.put('/run/{location}/')
def run_intervention(location: str = "India", time_end: int = 2030, intv: dict = None):
    return wr.run_intervention(location, time_end, intv)


@app.get('/')
def top():
    return 'Hello WarRoom'
