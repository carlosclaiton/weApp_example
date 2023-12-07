import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session
# from pssk_model import PSSKmodel

from typing import List


import schema as _schema
import services as _services

app = FastAPI()

@app.get("/")
async def root():
    return "Home page is working"

# @app.post("/api/clients/", response_model=_schema.Clients)
# async def create_domain( domain: _schema.CreateDomains, db: Session = Depends(_services.get_db), ):
#     return await _services.create_domain(domain=domain,db=db)

@app.get("/api/clients/", response_model=List[_schema.Clients])
async def get_clients( db: Session = Depends(_services.get_db)):
    return await _services.get_all_clients(db=db)


# @app.get("/api/nature_id/{natureID}", response_model=List[_schema.Natures])
# async def get_nature(natureID:int, db: Session = Depends(_services.get_db)):
#     return await _services.get_nature_name(natureID, db=db)

# @app.get("/pssk/{desired_kil_prob}/{narrativeID}")
# def pssk_display(desired_kil_prob:float, narrativeID:int, db: Session = Depends(_services.get_db)):
#     params = _services.get_pssk_parameters(narrativeID, db=db)
#     target_numbers = _services.get_narrative_targets(narrativeID, db=db)
    
    # # return f"deired to kill probablility {desired_kil_prob}, Domain involved {pssk_model_test.list_domains()}"
    # if len(params) == 0:
    #     raise HTTPException(status_code=400, detail=f'Narrative with id {narrativeID} does not exist' )
    
    # else:
    #     pssk_model = PSSKmodel(desired_kil_prob, params, target_numbers)

    # return pssk_model.total_nature_number()

if __name__=='__main__':
    uvicorn.run('main:app',
                host="0.0.0.0",
                port=8000,
                reload=True
                )