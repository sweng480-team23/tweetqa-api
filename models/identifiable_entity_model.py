from controllers import db
from sqlalchemy import Integer

# class new class name (class inherit from)


class IdentifiableEntity(db.Model):
    __abstract__ = True

    id = db.Column(Integer, primary_key=True, autoincrement = True)