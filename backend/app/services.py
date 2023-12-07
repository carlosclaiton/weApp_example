from typing import TYPE_CHECKING, List

import database as _db
import schema as _schema
import models as _models


def get_db():
    """Make the connection with the database"""
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_client(client: _schema.Clients, db: 'Session') -> _schema.Clients:
    """Function to add new domain into the data base"""
    # client = _models.Client(**client.dict())
    client = _models.Client(**client.model_dump())
    db.add(client)
    db.commit()
    db.refresh(client)
    return _schema.Clients.from_orm(client) 

async def get_all_clients(db:'Session') -> List[_schema.Clients]:
    client = db.query(_models.Clients).all()
    return list(map(_schema.Clients.from_orm, client))


# def get_pssk_parameters(narrativeID, db:'Session') -> List[_schema.NarrativeParameters]:
#     params = db.query(_models.NarrativeParameters).filter(getattr(_models.NarrativeParameters,"narrative_id")==narrativeID).all()
#     return list(map(_schema.NarrativeParameters.from_orm, params))
