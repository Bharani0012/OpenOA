from fastapi import FastAPI, HTTPException
from openoa.analysis import ElectricalLosses
import examples.project_ENGIE as project_ENGIE

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API working"}

@app.get("/run")
def run_analysis():
    try:
        print("STARTING ANALYSIS")

        project = project_ENGIE.prepare("./examples/data/la_haute_borne", use_cleansed=False)
        project.analysis_type.append("ElectricalLosses")
        project.validate()

        el = ElectricalLosses(project)
        el.run()

        return {    
            "loss": float(el.electrical_losses.mean()),
            "uncertainty": float(el.electrical_losses.std())
        }

    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))