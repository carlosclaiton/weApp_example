import datetime as _dt
import sqlalchemy as _sql

import database as _db


class Clients(_db.Base):
    __tablename__ = "clients"
    client_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    firstname = _sql.Column(_sql.String, index=True)
    surname = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, index=True)
    created_on = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow )