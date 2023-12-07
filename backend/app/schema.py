import datetime as _dt
import pydantic as _pydantic

class _BaseClients(_pydantic.BaseModel):
    firstname: str
    surname: str
    email: str
    
class Clients(_BaseClients):
    client_id : int
    # added_by: str
    created_on: _dt.datetime

    class Config:
        from_attributes = True
        # populate_by_name = True

class CreateClient(_BaseClients):
    pass

