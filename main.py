from fastapi import FastAPI
from openoa.analysis import ElectricalLosses
import examples.project_ENGIE as project_ENGIE

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API working"}

@app.get("/run")
def run_analysis():
    project = project_ENGIE.prepare('./examples/data/la_haute_borne', use_cleansed=False)
    project.analysis_type.append("ElectricalLosses")
    project.validate()

    el = ElectricalLosses(project, UQ=False)
    el.run()

    result = el.electrical_losses[0][0]

    return {"result": float(result)}