from db import sqlalchemydatabaseinstancev #get sqlalchemy database instance from db.py file

class StoreModel(sqlalchemydatabaseinstancev.Model):
    __tablename__ = "storestable"

    idcolumnv = sqlalchemydatabaseinstancev.Column(sqlalchemydatabaseinstancev.Integer, primary_key=True, nullable=False)
    namevolumnv = sqlalchemydatabaseinstancev.Column(sqlalchemydatabaseinstancev.String(100), nullable=False) #maps to one of values in line 12 in item.py
